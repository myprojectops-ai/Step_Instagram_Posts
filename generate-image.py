#!/usr/bin/env python3
"""
generate-image.py — Generate images via Gemini API (Nano Banana 2).

Usage:
  python generate-image.py --prompt "A professional headshot of a tech CEO" --output Assets/Personas/ceo.png
  python generate-image.py --prompt "OpenAI logo, clean, white background" --output Logos/openai_logo.png
  python generate-image.py --prompt "Abstract AI background with circuits" --output PostTypes/news/Outputs/topic/bg.png
  python generate-image.py --prompt "..." --reference input.png --output output.png   # image editing mode

Options:
  --prompt       Text prompt describing the image to generate (required)
  --output       Path to save the generated PNG (required)
  --reference    Optional input image for editing/style transfer
  --model        Model ID (default: gemini-2.5-flash-image)
  --aspect-ratio Aspect ratio: "1:1", "4:5", "16:9", etc. (default: 1:1)

Models available:
  gemini-3.1-flash-image-preview  — Nano Banana 2 (default, recommended)
  gemini-2.5-flash-image          — Nano Banana 1 (older, faster)
  gemini-3-pro-image-preview      — Pro quality, slower

Environment:
  GEMINI_API_KEY  — required. Set in .env at project root or as env var.
"""

import argparse
import base64
import json
import os
import sys
from pathlib import Path

# Load .env from project root if present
PROJECT_ROOT = Path(__file__).resolve().parent
env_file = PROJECT_ROOT / ".env"
if env_file.exists():
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())

API_KEY = os.environ.get("GEMINI_API_KEY", "")

if not API_KEY or API_KEY == "tu-api-key-aqui":
    print("ERROR: GEMINI_API_KEY not set or still placeholder.", file=sys.stderr)
    print("Set it in .env at the project root or as an environment variable.", file=sys.stderr)
    sys.exit(1)


def generate_image(prompt: str, output_path: str, model: str, aspect_ratio: str, reference_path: str | None = None):
    """Call the Gemini API to generate an image and save it as PNG."""
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("ERROR: google-genai package not installed.", file=sys.stderr)
        print("Install it with: pip install google-genai", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=API_KEY)

    # Build the contents
    contents = []

    # If there's a reference image, include it first
    if reference_path:
        ref = Path(reference_path)
        if not ref.exists():
            print(f"ERROR: Reference image not found: {reference_path}", file=sys.stderr)
            sys.exit(1)

        ref_bytes = ref.read_bytes()
        suffix = ref.suffix.lower()
        mime_map = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}
        mime = mime_map.get(suffix, "image/png")

        contents.append(types.Part.from_bytes(data=ref_bytes, mime_type=mime))

    contents.append(prompt)

    # Generate
    print(f"Generating image with {model}...")
    print(f"Prompt: {prompt[:120]}{'...' if len(prompt) > 120 else ''}")

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio=aspect_ratio,
            ),
        ),
    )

    # Extract and save the image
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    image_saved = False
    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            image_data = part.inline_data.data
            out.write_bytes(image_data)
            size_kb = len(image_data) / 1024
            print(f"Saved: {out} ({size_kb:.0f} KB)")
            image_saved = True
            break
        elif part.text:
            print(f"Model note: {part.text}")

    if not image_saved:
        print("ERROR: No image was generated. The model returned only text.", file=sys.stderr)
        print("Try a different prompt or model.", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Generate images via Gemini API (Nano Banana 2)")
    parser.add_argument("--prompt", required=True, help="Text prompt for image generation")
    parser.add_argument("--output", required=True, help="Output PNG path")
    parser.add_argument("--reference", default=None, help="Optional reference image for editing")
    parser.add_argument("--model", default="gemini-3.1-flash-image-preview", help="Model ID (default: gemini-3.1-flash-image-preview / Nano Banana 2)")
    parser.add_argument("--aspect-ratio", default="1:1", help="Aspect ratio (default: 1:1)")
    args = parser.parse_args()

    generate_image(
        prompt=args.prompt,
        output_path=args.output,
        model=args.model,
        aspect_ratio=args.aspect_ratio,
        reference_path=args.reference,
    )


if __name__ == "__main__":
    main()
