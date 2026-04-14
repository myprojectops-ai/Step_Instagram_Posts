---
name: news-post-design
description: Visual system for AI news Instagram posts — dark editorial style with real person photos, bold white headlines, and brand-consistent Inter typography. The primary post type for breaking AI announcements, model releases, and industry events.
type: skill
---

# News Post Design Skill

> **Project root:** `c:/Visual_posts/`. The autoloaded **[`CLAUDE.md`](../../../CLAUDE.md)** at the project root contains the trigger phrases and routes to per-type workflows. The news workflow lives in [`../README.md`](../README.md). Read those for the *process*; read this skill for the *visual system*.

This skill defines the complete visual language for **AI news posts** — single-image posts (not carousels) that announce breaking AI news with a bold, editorial feel. The style is inspired by the references in [`../Inspiracion/`](../Inspiracion/).

---

## 0. Relationship to the step-by-step visual system

News posts share the **brand-wide typography** (Inter family) and brand elements (`@lucianomusellaa`, Alta Studio logo) with step-by-step posts — this keeps the Instagram feed feeling cohesive. However, the **layout and color system are fundamentally different**:

| Property | Step-by-step | News |
|---|---|---|
| Background | Cream `#F5F2ED` with grid | **Dark** — photo + gradient overlay |
| Text color | Dark `#0E0E0E` | **White `#FFFFFF`** |
| Visual | SVG illustrations, UI mockups | **Real photos of people/products** |
| Format | Multi-slide carousel | **Single image** (standalone post) |
| Accent | Coral + yellow highlights | **Coral `#E85D3C`** for badge/accents only |
| Mood | Clean, editorial, tutorial | **Bold, urgent, newsworthy** |

The shared thread is Inter typography + the brand handle + the Alta Studio watermark. This creates *sinergia visual* without making everything look the same.

---

## 1. Canvas & format

| Property | Value |
|---|---|
| Aspect ratio | **4:5 portrait** (Instagram feed optimal) |
| Resolution | **1080 × 1350 px** |
| Format | **Single image** — news posts are NOT carousels. One slide, one headline, one visual. |
| Safe margins | ~60 px on all sides; keep text within the safe zone |

---

## 2. Color palette

News posts use a **dark palette** — the opposite of the cream step-by-step system. The photo is the background; everything else layers on top.

| Role | Value | Use |
|---|---|---|
| Photo overlay gradient | `linear-gradient(to bottom, rgba(0,0,0,0.15) 0%, rgba(0,0,0,0.75) 100%)` | Always on top of the person photo — darker at bottom for text legibility |
| Primary text | `#FFFFFF` | Headlines, main text |
| Secondary text | `rgba(255,255,255,0.7)` | Badge text, captions, subtle labels |
| Accent coral | `#E85D3C` | "AI NEWS" badge background, optional keyword accent |
| Highlight yellow | `#FFE45C` | Sparingly — only for an extremely important keyword (rare on news) |
| Dark fallback | `#0A0A0A` | If no photo is available, use a solid dark background |

**Key rule:** the gradient overlay must be strong enough that white text is **always readable** against the photo. If in doubt, make the gradient heavier. Readability > aesthetics.

---

## 3. Typography

**Same family as step-by-step** for brand consistency across the feed.

- **Family:** `'Inter', system-ui, -apple-system, sans-serif`
- **Import:** `https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700;800;900&display=swap`
- **Code font (if needed):** `'JetBrains Mono', monospace`

### Hierarchy for news posts (1080×1350 canvas)

| Element | Size | Weight | Color | Notes |
|---|---|---|---|---|
| "AI NEWS" badge text | 18–20 px | 700 | `#FFFFFF` | Inside coral pill, uppercase, letter-spacing +0.12em |
| Alta Studio logo (top-right) | 36 px tall | — | `opacity: 0.5; filter: brightness(3)` | Top-right corner — replaces `@lucianomusellaa` on news posts |
| **Headline** | 62–70 px | 800 | `#FFFFFF` | Bottom third of the image, left-aligned, 2–4 lines max, line-height 1.12–1.15. Go BIG — the text should fill the width and feel impactful. |
| Source/attribution | 18–20 px | 500 | `rgba(255,255,255,0.5)` | Optional — "Fuente: Bloomberg" style, below headline |
| Alta Studio logo | 36–44 px wide | — | White or `rgba(255,255,255,0.4)` | Bottom-right corner, subtle watermark |

---

## 4. The visual composition layer (CRITICAL — Nano Banana 2 full composition)

> **Core change (April 2026):** news posts no longer compose photos + logos in HTML/CSS. Instead, **Nano Banana 2 generates the complete visual composition** as a single image — person, brand logo, atmosphere, lighting, gradient — all baked together. HTML is used ONLY for text overlays (badge, headline, source, watermark).

### Why this approach

The previous approach (person photo as CSS background + logo as CSS overlay with `mix-blend-mode`) produced images that looked "pasted together" — the logo never felt integrated into the lighting, the blend modes were limited, and it took 12–18 HTML variations to get something passable. Nano Banana can generate a cohesive composition where the logo naturally belongs in the scene.

### What Nano Banana generates (the "composition image")

A single 4:5 image that contains:
- **The person** — recognizable, editorial photography style, occupying the upper 2/3 of the canvas
- **The brand logo** — large, semi-transparent, naturally integrated into the scene's lighting (behind or beside the person, as part of the atmosphere)
- **Dark editorial atmosphere** — moody lighting, dark tones, gradient that gets darker toward the bottom (where text will go)
- **The bottom ~35% should be very dark** — this is where the HTML headline will sit, so it needs to be dark enough for white text readability

### What Nano Banana does NOT generate

- Text of any kind (no headlines, no badges, no attributions)
- The "AI NEWS" badge
- The Alta Studio logo (top-right)
- Any text overlay — all text is composited onto the image via **Python/PIL**, NOT HTML/Chrome (Chrome introduces border artifacts on Windows)

### Composition prompting guidelines

The prompt to Nano Banana should follow this structure:

```
Professional editorial photograph of [PERSON NAME], [ROLE/TITLE] of [COMPANY].
[PERSON DESCRIPTION: clothing, expression, pose].
The [COMPANY] logo appears large and semi-transparent in the background,
naturally integrated into the scene lighting.
Dark, moody editorial atmosphere. The bottom third of the image fades to
near-black darkness (for text overlay). 4:5 portrait format.
High-quality magazine cover / news editorial style.
No text, no typography, no words anywhere in the image.
```

**Key prompt rules:**
- **Always end with "No text, no typography, no words anywhere in the image"** — Nano Banana tends to add text if not explicitly told not to
- **Describe the logo integration** — "semi-transparent in the background", "subtly visible behind the person", "glowing softly in the upper-right"
- **Emphasize the dark bottom** — "bottom third fades to near-black" is critical for text readability
- **Use `--aspect-ratio 4:5`** to match the Instagram canvas
- **Use `--model gemini-3-pro-image-preview`** for maximum quality (news compositions are the flagship product)

### Example prompts (based on validated favorites)

**Amazon-style (person in business setting, logo in background):**
```
Professional editorial photograph of Andy Jassy, CEO of Amazon.
He wears a blue blazer over a light shirt, speaking at a conference with a serious expression.
The Amazon logo appears large and semi-transparent behind him, softly glowing in the dark background.
Dark, moody editorial atmosphere with deep shadows. The bottom third fades to near-black darkness.
4:5 portrait format. High-quality news editorial photography.
No text, no typography, no words anywhere in the image.
```

**Perplexity-style (tech founder, geometric logo integrated):**
```
Professional editorial photograph of Aravind Srinivas, CEO of Perplexity AI.
He wears glasses and a dark t-shirt, intense expression, fist slightly raised.
The Perplexity logo (geometric asterisk shape) appears large and semi-transparent in the upper-right background, naturally blended into the dark scene.
Dark, moody editorial atmosphere. The bottom third fades to near-black.
4:5 portrait format. Magazine cover quality.
No text, no typography, no words anywhere in the image.
```

### Workflow for generating the composition

> **IMPORTANT: Generate ONE composition only.** The user trusts the prompt crafting to produce a good result on the first try. Do NOT generate 2–3 variants — that wastes API calls and money. Only generate a second composition if the user explicitly rejects the first one.

1. **Check `Assets/Personas/`** — if a reference photo exists, use `--reference` mode for better likeness
2. **Craft the best possible prompt** using the guidelines above and the user's validated favorites as reference
3. **Generate ONE composition:**
   ```bash
   python generate-image.py \
     --prompt "[composition prompt]" \
     --reference Assets/Personas/person_name.png \
     --output PostTypes/news/Outputs/{topic-slug}/composition.png \
     --model gemini-3-pro-image-preview \
     --aspect-ratio 4:5
   ```
4. **Resize to exact canvas dimensions** (Nano Banana may output smaller):
   ```python
   from PIL import Image
   img = Image.open("composition.png")
   if img.size != (1080, 1350):
       img = img.resize((1080, 1350), Image.LANCZOS)
       img.save("composition.png")
   ```
5. **Present to user for review** — only regenerate if they reject it
6. Once approved, proceed to the **PIL text compositing step** (NOT HTML/Chrome)

### Quality checklist for compositions
- Person is recognizable and well-lit
- Brand logo is visible but not overwhelming (semi-transparent, part of the atmosphere)
- Bottom ~35% is dark enough for white text to be readable
- No AI-generated text or artifacts in the image
- Overall feel: professional magazine cover, not "AI-generated collage"
- The composition looks like ONE cohesive image, not separate elements pasted together

---

## 5. Layout structure (new: composition image + HTML text overlay)

> **The layout is now two layers:**
> 1. **Nano Banana composition** — the full visual (person + logo + atmosphere) as a single background image
> 2. **HTML text overlay** — badge, headline, source, watermark rendered with precise typography

### Vertical structure

```
┌─────────────────────────────────┐
│  [AI NEWS badge]  [Alta Studio] │  ← HTML: top bar, ~60px from top
│                                 │
│     ┌───────────────────────┐   │
│     │  NANO BANANA          │   │
│     │  COMPOSITION IMAGE    │   │  ← Generated image: person + brand logo
│     │  (person + logo +     │   │     + dark atmosphere, all baked together
│     │   dark atmosphere)    │   │
│     │                       │   │
│     │   (bottom fades to    │   │
│     │    near-black)        │   │
│     └───────────────────────┘   │
│                                 │
│  Headline text in bold white    │  ← PIL: bottom area (over dark zone)
│  spanning 2-4 lines max         │
│                                 │
│  [Source attribution]           │  ← PIL: below headline
└─────────────────────────────────┘
```

### Brand logo — handled by Nano Banana, NOT CSS/PIL

The brand logo is **part of the generated composition image**. It's described in the Nano Banana prompt and gets naturally integrated into the scene's lighting and atmosphere.

### Text compositing — Python/PIL, NOT HTML/Chrome

> **CRITICAL:** News posts do NOT use HTML or Chrome for rendering. Chrome on Windows introduces black border artifacts that are visible on Instagram. Instead, all text is composited directly onto the composition image using **Python/PIL**.

#### Elements composited with PIL:
- **"AI NEWS" badge:** coral pill (`#E85D3C`, border-radius 8) with white Inter Bold text, top-left (~55px from top, ~55px from left)
- **Alta Studio logo:** top-right corner, 140px tall, opacity 0.75. **News posts do NOT show `@lucianomusellaa`** — the Alta Studio logo replaces the handle for an editorial feel.
- **Headline:** Inter Black, 80px, white, bottom area. 0–1 keyword in coral. Left-aligned, ~60px from left edge.
- **Source attribution:** Inter, 17px, white at 40% opacity, below headline.
- **Light gradient overlay:** subtle darkening on bottom 40% for text readability (numpy alpha gradient, max alpha ~140).
- **NO bottom-right watermark** — the user removed it. Only the top-right Alta Studio logo.

#### Text positioning rules:
- **Bottom margin:** ~50px from bottom edge to the "Fuente:" line
- **Headline sits above the source** with ~10px gap
- The text block should feel integrated with the image, not floating in empty space
- **No padding so large that it creates a visible "black strip"** at the bottom — this is the #1 visual bug to avoid

#### Font requirement:
- Inter font files must exist in `Assets/Fonts/` — at minimum `Inter-Black.ttf` (used for headlines and badges)
- Download from Google Fonts if missing

---

## 6. Headline writing rules for news posts

News headlines are **NOT tutorial headlines**. They need to feel like a news ticker — urgent, factual, punchy.

| Rule | News post |
|---|---|
| Word count | **8–20 words** (longer than covers because there's no "swipe" — this is the whole message) |
| Line count | 2–4 lines |
| Font size | 52–64 px (adjust to fit — shorter headlines get bigger) |
| Alignment | Left-aligned (default) or centered |
| Tone | **Factual, third-person** — reporting a fact, not giving instructions |
| Language | **Colombian Spanish, tú form** when addressing the viewer; neutral for reporting |
| Highlighted words | **0–1 keyword** in coral. News headlines are factual — highlighting is optional and rare |

### Headline style guide

**Good news headlines:**
- "Anthropic planea fabricar sus propios chips de IA"
- "El CEO de Amazon confirma una inversión de $2,000M en inteligencia artificial"
- "Perplexity ahora puede rastrear y analizar tus finanzas personales"
- "Investigadores crearon una IA que predice fallas cardíacas con 5 años de anticipación"

**Bad news headlines:**
- "¡INCREÍBLE noticia de Anthropic!" (clickbait, exclamation marks)
- "Crea tus propios chips con Anthropic" (this is a tutorial headline, not news)
- "Anthropic." (too vague, no information)
- "Anthropic reportedly considers building its own AI chips" (English — write in Colombian Spanish)

### Translation notes
- When the source is in English, translate to natural Colombian Spanish — don't do literal word-by-word translation.
- Adapt currency and units: "$2,000 this year" → "$2,000M este año" or "US$2.000 millones"
- Keep brand names in their original form: "Perplexity", "Anthropic", "OpenAI" — never translate these.

---

## 7. Accent highlighting on news posts — TWO versions every time

News posts **always produce two headline versions** so the user can pick the visual intensity:

### Version A — coral only (clean)
- 0–1 keyword in coral `#E85D3C`, everything else white. Classic news editorial feel.
- Example: "La IA de <span style='color:#E85D3C'>Scotiabank</span> ya resuelve el 40% de las consultas de sus clientes"

### Version B — double highlight (bold, step-by-step cover style)
- One keyword in **coral text** `#E85D3C` (typically a brand name)
- Another keyword on a **yellow marker** background `#FFE45C` with dark text `#0E0E0E` (typically a number or strong noun)
- The yellow marker is a rounded rectangle (8px radius) with tight padding (~10px horizontal, ~6px vertical), sized to the actual glyph bounds so it feels natural and proportional
- This brings the step-by-step cover energy to news posts for a bolder, more eye-catching result

### Which keywords to highlight
- **Coral:** brand names (Scotiabank, Anthropic, OpenAI), strong nouns (chips, agentes)
- **Yellow marker:** numbers (40%, $2,000M, 5 años), short impactful words (gratis, ahora)

---

## 8. Anti-patterns (news-specific)

In addition to the brand-wide anti-patterns in the base system:

- ❌ Cream/light background (news posts are ALWAYS dark)
- ❌ Grid pattern overlay (that's the step-by-step identity)
- ❌ SVG illustrations replacing real photos (the photo IS the visual — don't substitute it)
- ❌ Carousel format (news = single image, not a carousel)
- ❌ "PASO X" labels (that's tutorial language)
- ❌ "Desliza →" footer (there's nothing to swipe)
- ❌ Slide indicator dots (single image, not a carousel)
- ❌ Clickbait exclamation marks ("¡INCREÍBLE!", "¡NO VAS A CREER!")
- ❌ English headlines (always Colombian Spanish)
- ❌ Composing person photos + logos in HTML/CSS (use Nano Banana for the full visual composition — logos in CSS look "pasted")
- ❌ Using HTML/Chrome to render news posts (Chrome on Windows creates black border artifacts — use PIL for text compositing)
- ❌ Generating multiple COMPOSITION variants (waste of API money — generate ONE, only redo if user rejects it). Note: two TEXT versions (clean + highlight) are mandatory, not optional.
- ❌ Adding a bottom-right watermark (removed per user preference — only the top-right Alta Studio logo)
- ❌ CSS `mix-blend-mode` or `opacity` hacks for logo integration (the logo should be baked into the Nano Banana composition)
- ❌ Logo bubbles or connector lines (that's the step-by-step cover identity)
- ❌ Alta Studio logo bigger than ~44px or at full opacity (it's a SUBTLE watermark)
- ❌ Headline in the top half of the image (it belongs in the bottom third, over the dark area)
- ❌ White text without dark background beneath it (if composition bottom isn't dark enough, add a safety gradient)

---

## 9. Workflow when the user asks for a news post

1. **Read this skill** + the base system rules from [`CLAUDE.md`](../../../CLAUDE.md).
2. **Mandatory visual re-anchoring:** review `Inspiracion/` AND `Favoritos_Claude_Generated/` (see CLAUDE.md section 1.5).
3. **Understand the news:** read the headline, URL, or context the user provided. Identify:
   - What happened (the fact)
   - Which **people** appear in the story (CEOs, founders, researchers)
   - Which **brands/companies** are involved
4. **Check existing assets** — list `Assets/Personas/` and `Logos/` to see if a reference photo of the person exists (useful for `--reference` mode in Nano Banana).
5. **Propose 2–3 headline variations** in Colombian Spanish. Wait for approval.
6. **Research the full story.** If the user only gave a title/topic, use WebSearch to find the complete news article. Extract: who, what, when, how, numbers, impact, differentiator. Never invent data.
7. **Draft the caption** following the structure in section 13. Generate it directly (no approval needed — see memory: captions don't need approval).
8. **Generate ONE visual composition with Nano Banana 2.** This is the key step:
   - Craft the best possible prompt: person + brand logo integrated + dark editorial atmosphere + dark bottom for text (see section 4)
   - Use `--reference` with an existing persona photo if available (preserves likeness)
   - Use `--model gemini-3-pro-image-preview` for maximum quality
   - Use `--aspect-ratio 4:5` for Instagram canvas
   - **Generate ONE composition only** — don't waste API calls on variants. The user trusts the prompt crafting.
   - Resize to 1080×1350 if needed (Nano Banana may output smaller)
   - **Present to user for review** — only regenerate if rejected
9. **Composite text with Python/PIL — generate TWO versions** (NOT HTML/Chrome — Chrome creates border artifacts on Windows):
   After the user approves the composition, **always generate two headline variants** so the user can choose the visual intensity:
   - **Version A (`news_v1_clean.png`) — coral only:** 0–1 keyword in coral `#E85D3C`, no yellow marker. Classic news style, cleaner.
   - **Version B (`news_v2_highlight.png`) — double highlight (step-by-step cover style):** one keyword in coral + another keyword on a **yellow marker** background `#FFE45C` (rounded rect, 8px radius, tight padding: ~10px horizontal, ~6px vertical). Text on the marker is dark `#0E0E0E`. This is the bolder, more eye-catching variant.
   
   Both versions share these elements:
   - Load composition as base image
   - Add light gradient overlay on bottom 40% (numpy, max alpha ~140)
   - Draw "AI NEWS" badge (coral pill + white text, top-left)
   - Paste Alta Studio logo (top-right, 140px, opacity 0.75)
   - Draw headline (Inter Black 76–80px, white, left-aligned at x=60)
   - Draw source attribution (Inter 17px, white 40% opacity, below headline)
   - Bottom margin: ~50px. **No bottom-right watermark.**
   
   **Yellow marker sizing rules (version B):**
   - Use `font.getbbox()` to measure the actual glyph bounds of the marker keyword
   - Horizontal padding: ~10px (tight — must NOT touch adjacent characters)
   - Vertical padding: ~6px
   - Align the rect to the actual glyph top/bottom (use `getbbox()[1]` for top offset), not the text origin
   - Border radius: 8px
   - The marker must feel natural and proportional, not oversized
   
   Present both versions side by side and let the user choose.
10. **MANDATORY visual verification.** Open and inspect BOTH PNGs. Check: text readable, no artifacts, image fills 1080×1350 edge-to-edge with zero borders, yellow marker (v2) fully contains the text without cutting it.
11. **Save the caption** as `caption.txt` in the same output folder.
12. **Present the complete deliverable:** rendered image + caption text, together. Offer iterations.
13. **Ask which images are favorites** for `Favoritos_Claude_Generated/` (see CLAUDE.md section 1.6).

### Naming convention for news output files

```
PostTypes/news/Outputs/{topic-slug}/
├── composition.png           ← Nano Banana full composition (person + logo + atmosphere)
├── news_v1_clean.png         ← Version A: coral-only headline (classic news style)
├── news_v2_highlight.png     ← Version B: double highlight with yellow marker (bolder style)
└── caption.txt               ← Caption for Instagram
```

- `{topic-slug}`: kebab-case, descriptive. E.g. `anthropic-chips-ia`, `amazon-inversion-ia`, `perplexity-finanzas`.
- **TWO text versions per post** — one clean (coral only) and one with yellow marker highlight. The user picks which to publish.

---

## 10. PIL text compositing — reference code

> **News posts use Python/PIL for text compositing, NOT HTML/Chrome.** This eliminates the black border artifacts Chrome produces on Windows and guarantees the image fills 1080×1350 edge-to-edge.

```python
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# === Load assets ===
composition = Image.open("composition.png").convert("RGBA")
alta_logo = Image.open("Logos/Alta_Studio_logo_white.png").convert("RGBA")
font_headline = ImageFont.truetype("Assets/Fonts/Inter-Black.ttf", 80)
font_badge = ImageFont.truetype("Assets/Fonts/Inter-Black.ttf", 18)
font_source = ImageFont.truetype("Assets/Fonts/Inter-Black.ttf", 17)

# === Resize composition to exact canvas if needed ===
if composition.size != (1080, 1350):
    composition = composition.resize((1080, 1350), Image.LANCZOS)

canvas = composition.copy()

# === Light gradient overlay (bottom 40%, max alpha 140) ===
gradient = Image.new("RGBA", (1080, 1350), (0, 0, 0, 0))
grad_arr = np.array(gradient)
for y in range(810, 1350):
    grad_arr[y, :, 3] = int(140 * ((y - 810) / 540))
canvas = Image.alpha_composite(canvas, Image.fromarray(grad_arr))
draw = ImageDraw.Draw(canvas)

# === "AI NEWS" badge (top-left, ~55px from edges) ===
badge_text, bx, by, px, py = "AI NEWS", 55, 50, 22, 10
bbox = font_badge.getbbox(badge_text)
draw.rounded_rectangle(
    [bx, by, bx + bbox[2]-bbox[0] + px*2, by + bbox[3]-bbox[1] + py*2],
    radius=8, fill=(232, 93, 60, 255))
draw.text((bx + px, by + py), badge_text, font=font_badge, fill=(255, 255, 255))

# === Alta Studio logo (top-right, 140px, opacity 0.75) ===
logo_h = 140
logo_w = int(logo_h * alta_logo.width / alta_logo.height)
logo_sm = alta_logo.resize((logo_w, logo_h), Image.LANCZOS)
logo_arr = np.array(logo_sm)
logo_arr[:, :, 3] = (logo_arr[:, :, 3] * 0.75).astype(np.uint8)
canvas.paste(Image.fromarray(logo_arr), (1080 - 55 - logo_w, 30), Image.fromarray(logo_arr))
draw = ImageDraw.Draw(canvas)

# === Headline (Inter Black 80px, left-aligned at x=60) ===
# Break into lines with optional coral keyword
lines = [
    [("HEADLINE LINE 1", (255, 255, 255))],
    [("KEYWORD", (232, 93, 60)), (" rest of line 2", (255, 255, 255))],
    [("line 3", (255, 255, 255))],
]
line_h, bottom_margin, source_h, gap = 86, 50, 22, 10
headline_y = 1350 - bottom_margin - source_h - gap - (len(lines) * line_h)
for i, parts in enumerate(lines):
    x = 60
    for text, color in parts:
        draw.text((x, headline_y + i * line_h), text, font=font_headline, fill=color)
        x += font_headline.getbbox(text)[2] - font_headline.getbbox(text)[0]

# === Source (below headline, ~50px from bottom edge) ===
draw.text((60, 1350 - bottom_margin - source_h),
          "Fuente: ...", font=font_source, fill=(255, 255, 255, 102))

# === Save (NO bottom-right watermark) ===
canvas.convert("RGB").save("news_final.png", quality=95)
```

### Key specs for PIL compositing

| Element | Font | Size | Position | Color/Opacity |
|---|---|---|---|---|
| "AI NEWS" badge | Inter Black | 18px | top-left (55, 50) | White on coral `#E85D3C` pill |
| Alta Studio logo | — | 140px tall | top-right (55px from edge) | 75% opacity |
| Headline | Inter Black | 80px | bottom area, x=60 | White, 0–1 keyword in coral |
| Source | Inter Black | 17px | below headline, x=60 | White 40% opacity |
| Bottom margin | — | ~50px | from bottom edge to source text | — |
| Gradient | numpy | bottom 40% | max alpha 140 | Black, transparent to semi-opaque |
| Bottom-right watermark | — | — | **NONE** | Removed per user preference |

---

## 11. Alta Studio logo rules (NEWS posts ONLY)

The Alta Studio logo appears **in the top-right corner** of every news post (composited via PIL). This is exclusive to news posts — step-by-step and informativos use `@lucianomusellaa` instead.

| Property | Value |
|---|---|
| File | `Logos/Alta_Studio_logo_white.png` |
| Position | Top-right corner, ~55px from right edge, ~30px from top |
| Size | 140px tall (auto width) |
| Opacity | 0.75 |

**Non-negotiable:** the watermark must NEVER be the focal point. If someone has to squint to see it, that's perfect. It's a brand signature, not a feature.

---

## 13. Caption del post — el complemento informativo (OBLIGATORIO)

Cada news post es una **imagen única** + un **caption** en texto. La imagen atrapa la atención; el caption entrega la información. Los dos son parte del entregable — nunca presentes solo la imagen sin el caption.

### Investigación de la noticia

Cuando el usuario da la noticia, pueden pasar dos cosas:

1. **El usuario da un titular o tema suelto** (ej: "la noticia de que Oxford creó una IA que predice fallas cardíacas") → **buscar en internet** la noticia completa usando WebSearch. Extraer los datos clave: quién, qué, cuándo, cómo, cifras, impacto, diferencial.
2. **El usuario da una URL o un texto largo** → extraer la información directamente de ahí.

En ambos casos, el caption se redacta **después de tener los datos completos**. Nunca inventar cifras, porcentajes o afirmaciones que no estén en la fuente.

### Estructura del caption

El caption sigue un formato de **párrafos cortos y separados** (cada uno de 1–2 oraciones). NO es un párrafo largo ni un bloque de texto corrido. La estructura es:

1. **Hook** (1 línea) — la afirmación más impactante de la noticia, en presente. Captura la atención como un titular expandido.
2. **Contexto** (1–2 líneas) — quién hizo qué, cuándo, dónde. El "lead" periodístico.
3. **Dato clave 1** (1–2 líneas) — el cómo funciona, la tecnología, el método.
4. **Dato clave 2** (1–2 líneas) — la escala, los números, la muestra.
5. **Dato clave 3** (1–2 líneas) — el resultado, la precisión, el impacto medido.
6. **Dato de impacto** (1–2 líneas) — la consecuencia práctica para personas/industria.
7. **Siguiente paso / futuro** (1–2 líneas) — qué sigue (regulación, despliegue, fechas).
8. **Diferencial** (1–2 líneas) — qué hace diferente a esta noticia vs. lo que ya existía. Cierra con perspectiva.

No todos los puntos son obligatorios — adaptar según la noticia. Algunas noticias tienen 5 párrafos, otras 8. La clave es que cada párrafo agrega información nueva y ninguno es relleno.

### Ejemplo de caption (español colombiano)

```
Una herramienta de IA desarrollada en Oxford puede predecir fallas cardíacas años antes de que ocurran.

Investigadores de la Universidad de Oxford crearon una IA capaz de predecir el riesgo de insuficiencia cardíaca de una persona con hasta cinco años de anticipación.

Funciona analizando tomografías de rutina y detectando señales sutiles de inflamación en la grasa que rodea el corazón, señales que los médicos no pueden ver a simple vista.

El sistema fue entrenado con datos de 72,000 pacientes en hospitales del NHS en Inglaterra.

Luego asigna a cada paciente un puntaje de riesgo personalizado para desarrollar insuficiencia cardíaca en los próximos cinco años.

En las pruebas, alcanzó una precisión del 86%.

Los pacientes identificados como alto riesgo tenían 20 veces más probabilidades de desarrollar la condición.

Los investigadores buscan integrar la herramienta en los flujos hospitalarios estándar, pendiente de aprobación regulatoria, para permitir diagnósticos más tempranos y atención preventiva.

A diferencia de métodos anteriores que dependían de imágenes especializadas o conjuntos de datos clínicos complejos, la IA de Oxford usa tomografías de rutina para detectar inflamación oculta alrededor del corazón, probada en 72,000 pacientes y ahora en camino a implementación real.
```

### Reglas de redacción del caption

| Regla | Detalle |
|---|---|
| Idioma | **Español colombiano, tú form** — mismo estándar que toda la marca |
| Tono | Informativo, directo, sin opinión personal. Como un periodista tech que explica claro |
| Párrafos | Cortos (1–2 oraciones cada uno), separados por línea en blanco |
| Números | Usar cifras, no palabras: "72,000 pacientes", "86% de precisión", "$2,000M" |
| Jerga técnica | Explicarla en la misma oración si el público general no la conoce |
| Fuentes | No inventar datos. Si no encuentras un dato, no lo incluyas |
| Emojis | NO usar emojis en el caption |
| Hashtags | NO incluir hashtags — el usuario los agrega después si quiere |
| Longitud | 6–10 párrafos cortos (típicamente 150–300 palabras) |
| CTA | NO incluir call-to-action ("sígueme", "guarda", "comenta") — solo información |

### Dónde se entrega el caption

El caption se presenta como **texto plano** en la respuesta, debajo de la imagen renderizada, listo para copiar y pegar en Instagram. También se guarda como archivo `.txt` en la carpeta de outputs del post:

```
PostTypes/news/Outputs/{topic-slug}/
├── news_v1_{descriptor}.html
├── news_v1_{descriptor}.png
├── caption.txt                  ← el caption listo para copiar
└── ...
```

### Caption en el workflow

El caption se genera como **paso 6** del workflow (después de aprobar los headlines, antes de generar el HTML de la imagen). El flujo es:

1. (...pasos 1–4 del workflow: skill, re-anchoring, entender noticia, asset check...)
2. Proponer headlines → usuario aprueba
3. **Investigar la noticia a fondo** (si solo dio un titular, buscar en internet)
4. **Redactar el caption** y presentarlo al usuario para aprobación
5. Generar la imagen HTML + renderizar
6. Presentar imagen + caption juntos como entregable completo

---

## 14. Quick reference checklist (run before exporting any news post)

### Composition (Nano Banana)
- [ ] Composition generated with `gemini-3-pro-image-preview` at 4:5 aspect ratio
- [ ] Person is recognizable and well-lit in the composition
- [ ] Brand logo is visible and naturally integrated (not pasted-looking)
- [ ] Bottom ~35% of composition is dark enough for white text
- [ ] No AI-generated text or typography artifacts in the composition
- [ ] Composition was presented to user and approved before proceeding

### HTML text overlay
- [ ] Canvas is 1080×1350
- [ ] "AI NEWS" badge in coral pill, top-left
- [ ] Alta Studio logo in top-right (NOT `@lucianomusellaa` on news posts)
- [ ] Headline in bottom third, 8–20 words, Colombian Spanish
- [ ] Headline uses Inter font, weight 800, white
- [ ] 0–1 keyword highlighted in coral (not mandatory)
- [ ] No double highlight, no yellow marker (unless exceptional)
- [ ] Source attribution if applicable
- [ ] Alta Studio watermark in bottom-right, subtle (opacity 0.3–0.5)
- [ ] Safety gradient only if needed for text readability

### Content
- [ ] **Colombian Spanish only** — no voseo (creá, usá, etc.)
- [ ] **Caption drafted** — 6–10 short paragraphs, factual, no emojis, no hashtags, no CTA
- [ ] Caption saved as `caption.txt` in the output folder
- [ ] All data in the caption is sourced (nothing invented)

### Delivery
- [ ] Saved to `PostTypes/news/Outputs/{topic-slug}/`
- [ ] Rendered via `./render.sh`
- [ ] Visual verification passed — text readable, no artifacts
