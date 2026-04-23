#!/usr/bin/env python3
"""
generate-image.py — Generate images via OpenAI API (gpt-image-1).

Usage:
  python generate-image.py --prompt "A professional headshot of a tech CEO" --output Assets/Personas/ceo.png --aspect-ratio 4:5
  python generate-image.py --prompt "OpenAI logo, clean, white background" --output Logos/openai_logo.png --aspect-ratio 1:1
  python generate-image.py --prompt "Abstract AI background with circuits" --output PostTypes/news/Outputs/topic/bg.png --aspect-ratio 16:9
  python generate-image.py --prompt "..." --reference input.png --output output.png --aspect-ratio 4:5   # image editing mode

Options:
  --prompt         Text prompt describing the image to generate (required)
  --output         Path to save the generated PNG (required)
  --reference      Optional input image for editing / reference-based generation
  --model          Model ID (default: gpt-image-1)
  --aspect-ratio   Aspect ratio: "1:1", "4:5", or "16:9" (default: 1:1)
  --quality        Image quality: "low", "medium", "high", "auto" (default: high)
  --crop           Crop direction when downsizing: "top", "center", "bottom" (default: top).
                   Use "top" for portraits to avoid cutting off heads.

Models available:
  gpt-image-1   — Default. OpenAI's current image generation model.
  (Legacy Gemini model IDs are soft-warned and silently remapped to gpt-image-1.)

Final output dimensions (after internal crop + resize):
  1:1   → 1080 x 1080
  4:5   → 1080 x 1350
  16:9  → 1080 x 608

Environment:
  OPENAI_API_KEY  — required. Set in .env at project root or as env var.
                    Note: a ChatGPT Plus/Pro subscription does NOT cover the API.
                    The Images API is billed separately per image.
"""

import argparse
import base64
import os
import sys
import time
from io import BytesIO
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
env_file = PROJECT_ROOT / ".env"
if env_file.exists():
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())

API_KEY = os.environ.get("OPENAI_API_KEY", "")

if not API_KEY or API_KEY == "tu-api-key-aqui":
    print("ERROR: OPENAI_API_KEY not set or still placeholder.", file=sys.stderr)
    print("Set it in .env at the project root or as an environment variable.", file=sys.stderr)
    print("Note: ChatGPT Plus/Pro does NOT include API access — a separate billing key is required.", file=sys.stderr)
    sys.exit(1)


ASPECT_TO_SIZE = {
    "1:1": "1024x1024",
    "4:5": "1024x1536",
    "16:9": "1536x1024",
}

ASPECT_TO_FINAL = {
    "1:1": (1080, 1080),
    "4:5": (1080, 1350),
    "16:9": (1080, 608),
}

VALID_QUALITIES = {"low", "medium", "high", "auto"}
VALID_CROPS = {"top", "center", "bottom"}


def crop_to_target_ratio(img, target_w: int, target_h: int, crop_mode: str):
    """Crop `img` (PIL.Image) to match the target_w/target_h aspect ratio before resizing.

    crop_mode controls which portion is preserved when the source aspect is taller or
    wider than the target. For portraits, 'top' keeps heads in frame.
    """
    src_w, src_h = img.size
    target_ratio = target_w / target_h
    src_ratio = src_w / src_h

    if abs(src_ratio - target_ratio) < 1e-3:
        return img

    if src_ratio > target_ratio:
        new_w = int(round(src_h * target_ratio))
        delta = src_w - new_w
        if crop_mode == "top":
            left = 0
        elif crop_mode == "bottom":
            left = delta
        else:
            left = delta // 2
        return img.crop((left, 0, left + new_w, src_h))
    else:
        new_h = int(round(src_w / target_ratio))
        delta = src_h - new_h
        if crop_mode == "top":
            top = 0
        elif crop_mode == "bottom":
            top = delta
        else:
            top = delta // 2
        return img.crop((0, top, src_w, top + new_h))


def call_openai_with_retry(client, use_edit: bool, reference_path: str | None, **params):
    """Call images.edit or images.generate with a single retry on 429 rate limit."""
    try:
        from openai import APIStatusError, RateLimitError
    except ImportError:
        APIStatusError = RateLimitError = Exception  # fallback; we still catch broadly

    for attempt in (1, 2):
        try:
            if use_edit:
                with open(reference_path, "rb") as ref_f:
                    return client.images.edit(image=ref_f, **params)
            return client.images.generate(**params)
        except RateLimitError as e:
            if attempt == 1:
                print("Rate limited (429). Waiting 20s and retrying once...", file=sys.stderr)
                time.sleep(20)
                continue
            print(f"ERROR: Rate limit still active after retry: {e}", file=sys.stderr)
            sys.exit(1)
        except APIStatusError as e:
            body_text = getattr(e, "message", "") or str(e)
            code = getattr(getattr(e, "response", None), "status_code", None)
            if "content_policy" in body_text.lower() or code == 400:
                print("ERROR: OpenAI rejected the prompt (likely content policy).", file=sys.stderr)
                print(f"Prompt: {params.get('prompt', '')[:200]}", file=sys.stderr)
                print("Hint: OpenAI's image policy blocks named real public figures more aggressively than Gemini.", file=sys.stderr)
                print("      Try rephrasing as 'a person who looks like X', or describe role/setting without the name.", file=sys.stderr)
                sys.exit(1)
            print(f"ERROR: OpenAI API error: {e}", file=sys.stderr)
            sys.exit(1)


def generate_image(prompt: str, output_path: str, model: str, aspect_ratio: str,
                   quality: str, crop: str, reference_path: str | None = None):
    """Call the OpenAI Images API (gpt-image-1) to generate an image and save it as PNG."""
    try:
        from openai import OpenAI
    except ImportError:
        print("ERROR: openai package not installed.", file=sys.stderr)
        print("Install it with: pip install openai pillow", file=sys.stderr)
        sys.exit(1)

    try:
        from PIL import Image
    except ImportError:
        print("ERROR: Pillow package not installed.", file=sys.stderr)
        print("Install it with: pip install openai pillow", file=sys.stderr)
        sys.exit(1)

    if aspect_ratio not in ASPECT_TO_SIZE:
        print(f"ERROR: Unsupported --aspect-ratio '{aspect_ratio}'.", file=sys.stderr)
        print(f"Supported values: {', '.join(ASPECT_TO_SIZE.keys())}", file=sys.stderr)
        sys.exit(1)

    if quality not in VALID_QUALITIES:
        print(f"ERROR: Unsupported --quality '{quality}'. Valid: {', '.join(sorted(VALID_QUALITIES))}", file=sys.stderr)
        sys.exit(1)

    if crop not in VALID_CROPS:
        print(f"ERROR: Unsupported --crop '{crop}'. Valid: {', '.join(sorted(VALID_CROPS))}", file=sys.stderr)
        sys.exit(1)

    if model.startswith("gemini-"):
        print(f"WARNING: Gemini backend removed; ignoring --model {model} and using gpt-image-1.", file=sys.stderr)
        model = "gpt-image-1"

    if reference_path:
        ref = Path(reference_path)
        if not ref.exists():
            print(f"ERROR: Reference image not found: {reference_path}", file=sys.stderr)
            sys.exit(1)

    client = OpenAI(api_key=API_KEY)

    size = ASPECT_TO_SIZE[aspect_ratio]
    final_w, final_h = ASPECT_TO_FINAL[aspect_ratio]

    print(f"Generating image with {model} ({size}, quality={quality})...")
    print(f"Prompt: {prompt[:120]}{'...' if len(prompt) > 120 else ''}")
    if reference_path:
        print(f"Reference: {reference_path}")

    params = {
        "model": model,
        "prompt": prompt,
        "size": size,
        "quality": quality,
        "n": 1,
    }

    response = call_openai_with_retry(
        client,
        use_edit=bool(reference_path),
        reference_path=reference_path,
        **params,
    )

    if not response.data or not response.data[0].b64_json:
        print("ERROR: OpenAI returned no image data.", file=sys.stderr)
        sys.exit(1)

    raw_png = base64.b64decode(response.data[0].b64_json)
    img = Image.open(BytesIO(raw_png)).convert("RGB")

    img = crop_to_target_ratio(img, final_w, final_h, crop)
    img = img.resize((final_w, final_h), Image.LANCZOS)

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, format="PNG")

    size_kb = out.stat().st_size / 1024
    print(f"Saved: {out} ({final_w}x{final_h}, {size_kb:.0f} KB)")


def main():
    parser = argparse.ArgumentParser(description="Generate images via OpenAI API (gpt-image-1)")
    parser.add_argument("--prompt", required=True, help="Text prompt for image generation")
    parser.add_argument("--output", required=True, help="Output PNG path")
    parser.add_argument("--reference", default=None, help="Optional reference image for editing mode")
    parser.add_argument("--model", default="gpt-image-1", help="Model ID (default: gpt-image-1)")
    parser.add_argument("--aspect-ratio", default="1:1",
                        help="Aspect ratio: 1:1, 4:5, or 16:9 (default: 1:1)")
    parser.add_argument("--quality", default="high",
                        help="Image quality: low | medium | high | auto (default: high)")
    parser.add_argument("--crop", default="top",
                        help="Crop direction: top | center | bottom (default: top; preserves faces in portraits)")
    args = parser.parse_args()

    generate_image(
        prompt=args.prompt,
        output_path=args.output,
        model=args.model,
        aspect_ratio=args.aspect_ratio,
        quality=args.quality,
        crop=args.crop,
        reference_path=args.reference,
    )


if __name__ == "__main__":
    main()
