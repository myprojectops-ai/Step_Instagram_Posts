---
name: informativo-post-design
description: Visual system for informative Instagram posts â€” dense infographics, tip lists, cheatsheets, tier lists, hack compilations. Uses Codex image tool for full visual compositions (backgrounds, icons, layout structure, brand logos) with HTML text overlay for precise typography. The goal is "save-worthy" content that looks editorially designed, not AI-generated.
type: skill
---

# Informativo Post Design Skill

> **Project root:** `c:/Visual_posts/`. The autoloaded **[`CLAUDE.md`](../../../CLAUDE.md)** at the project root contains the trigger phrases and routes to per-type workflows. The informativo workflow lives in [`../README.md`](../README.md). Read those for the *process*; read this skill for the *visual system*.

This skill defines the complete visual language for **informative posts** â€” standalone infographics, tip lists, hack compilations, cheatsheets, tier lists, and "save-this" reference content about AI tools. These are the **densest, most visually rich posts** in the project.

---

## 0. Relationship to the other post types

Informativos share the **brand-wide typography** (Inter family) and brand elements (`@lucianomusellaa`) with step-by-step posts. But the visual approach and layout density are fundamentally different:

| Property | Step-by-step | News | **Informativo** |
|---|---|---|---|
| Background | Cream `#F5F2ED` + grid | Dark photo + gradient | **Codex image tool composition** (cream-based, richly designed) |
| Density | Low â€” one focal point per slide | Low â€” photo + headline | **HIGH â€” multiple content blocks, icons, badges** |
| Format | Multi-slide carousel (6â€“8 slides) | Single image | **Single image OR short carousel (1â€“4 slides)** |
| Visual generation | HTML + CSS + inline SVG | Codex image tool full composition | **Codex image tool full composition** |
| Text rendering | HTML (baked into the slide) | PIL overlay | **PIL overlay** (directly on composition image) |
| Visual elements | 1â€“2 per slide (logo bubbles, mockup) | Photo + gradient | **Many â€” icons, badges, cards, numbered items, tier bars** |
| Mood | Clean, instructional | Bold, urgent | **Dense, save-worthy, reference-quality** |

The shared thread: Inter typography + `@lucianomusellaa` handle + coral/yellow accents. Informativos are the "textbook pages" of the feed â€” packed with value.

---

## 1. Canvas & format

| Property | Value |
|---|---|
| Aspect ratio | **4:5 portrait** (Instagram feed optimal) |
| Resolution | **1080 x 1350 px** |
| Format | **Single image** (default) or **short carousel** (2â€“4 slides max for very long lists). Most informativos are single images. |
| Safe margins | **50â€“60 px** on all sides (tighter than step-by-step â€” we need the space) |

### When to use carousel vs single image

| Content | Format |
|---|---|
| 5â€“9 items (tips, tools, hacks) | **Single image** â€” fit them all |
| 10+ items or items with long descriptions | **Short carousel** (2â€“3 slides + optional closing CTA) |
| Cheatsheet / reference card | **Single image** â€” it should be screenshot-able |
| Mind map / concept diagram | **Single image** |
| Tier list / pyramid | **Single image** |

When using carousel format, include slide indicators and `Desliza â†’` exactly like step-by-step (see base skill section 4.5).

---

## 2. Color palette â€” extended for informativos

Informativos inherit the base palette but unlock **category colors** for distinguishing sections, items, or tiers. This is the only post type that can use more than 2 accent colors per slide.

### Core palette (same as base)

| Role | Hex | Use |
|---|---|---|
| Background | `#F5F2ED` | Canvas base (Codex image tool should replicate this) |
| Grid lines | `#E8E4DD` | Subtle background grid |
| Primary text | `#0E0E0E` | Titles, item names |
| Secondary text | `#8A8780` | Labels, captions, descriptions |
| Body text | `#3A3A38` | Item descriptions, longer text |
| **Accent coral** | `#E85D3C` | Primary accent â€” numbers, key badges, highlighted words |
| **Highlight yellow** | `#FFE45C` | Secondary accent â€” markers, callout backgrounds |

### Category color palette (informativos only)

When items need **visual differentiation** (e.g., "7 AI models" where each needs its own identity, or a tier list with levels), use these category colors:

| Name | Hex | Use case |
|---|---|---|
| Coral (primary) | `#E85D3C` | Default accent, first category, numbers |
| Warm orange | `#F49D37` | Second category, warnings, "pro tips" |
| Sage green | `#5B8C5A` | Third category, "works well", approved |
| Ocean blue | `#4A90D9` | Fourth category, tools, links, tech |
| Soft purple | `#8B6CC1` | Fifth category, advanced, premium |
| Dusty rose | `#C7727D` | Sixth category, creative, design |
| Slate teal | `#5A9E9E` | Seventh category, data, analytics |

**Rules for category colors:**
- Use **at most 5 different category colors** per single-image post. More than that = visual chaos.
- Category colors appear as **small elements** â€” badges, side borders, icon fills, number circles. Never as large background areas.
- The overall post must still read as ~75% neutral (cream/black/grey) with colored accents, NOT a rainbow.
- When items don't need differentiation (e.g., "5 tips" that are all equal), stick to coral + yellow only.

---

## 3. Typography â€” denser hierarchy

Informativos need more typography levels than step-by-step because they carry more information layers. All text is rendered via HTML overlay, NOT baked into the Codex image tool composition.

- **Family:** `'Inter', system-ui, -apple-system, sans-serif`
- **Import:** `https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap`
- **Code font:** `'JetBrains Mono', monospace` (for prompts, code snippets, technical content)

### Hierarchy for informativos (1080x1350 canvas)

| Element | Size | Weight | Color | Notes |
|---|---|---|---|---|
| `@lucianomusellaa` (top) | 22â€“24 px | 500 | `#8A8780` | Top center or top-left, slightly smaller than step-by-step to save space |
| **Main title** | 48â€“64 px | 800â€“900 | `#0E0E0E` | The hook. 2â€“3 lines max. Can go up to 72 px for pure typographic covers. |
| **Subtitle / hook line** | 22â€“26 px | 500 | `#8A8780` | Optional â€” appears below the title |
| **Section header** | 28â€“34 px | 700 | `#0E0E0E` | Used in multi-section layouts |
| **Item number / badge** | 24â€“32 px | 800 | `#FFFFFF` on colored circle | Numbered items get a colored circle (36â€“44 px) with the number inside |
| **Item title** | 24â€“30 px | 700 | `#0E0E0E` | The name of the tip/tool/hack |
| **Item description** | 18â€“22 px | 400â€“500 | `#3A3A38` or `#6B6860` | 1â€“2 lines explaining the item. Keep it tight. |
| **Callout / highlight box text** | 20â€“24 px | 600 | Varies | Inside colored boxes or cards |
| **Footer / source** | 16â€“18 px | 500 | `#8A8780` | "Fuente:", attribution, or micro-CTA |

### Title writing rules for informativos

The title is the **hook** â€” it has to promise enough value that the viewer saves the post.

| Rule | Value |
|---|---|
| Word count | **5â€“14 words** (longer than covers because it often includes a number) |
| Number in title | **Almost always** â€” "7 prompts", "Top 5 herramientas", "9 reglas" |
| Font size | 48â€“64 px (adjust based on content density below it) |
| Highlighted words | **1â€“2 keywords** in coral or on yellow marker. The number is almost always highlighted. |
| Tone | Colombian Spanish, `tu` form. Factual + useful. |

**Good informativo titles:**
- "**9** reglas de oro para configurar **Claude**"
- "Top **7** modelos de IA para trabajar mas inteligente"
- "Las mejores apps de **IA** para 2026"
- "**5** hacks de prompts que nadie te ensena"

---

## 4. The visual composition layer (CRITICAL â€” Codex image tool full composition)

> **Core approach (April 2026):** informativo posts use **Codex image tool to generate the complete visual composition** â€” background, layout structure, decorative elements, icons, brand logos, gradients, card shapes â€” all as ONE cohesive image. **HTML is used ONLY for text overlays** (titles, item names, descriptions, numbers, badges, handle, footer).

### Why this approach

The previous approach (HTML + CSS + inline SVG) produced layouts that looked "flat" and "AI-template-ish." The inspiration images (Inspo_01 through Inspo_13) show rich visual compositions with:
- Organic gradients and artistic textures impossible in CSS
- Real photographs of people (Inspo_03, 05, 07, 08)
- Complex decorative elements (abstract blobs in Inspo_01, artistic ear in Inspo_08)
- Professionally designed card layouts with depth and shadows
- Brand logos naturally integrated into the scene

Codex image tool can generate all of this as one cohesive image where elements feel like they *belong together*, not pasted on top of each other. Text overlay via HTML ensures every word is legible, correctly spelled, and precisely positioned.

### What Codex image tool generates (the "composition image")

A single 4:5 image that contains the **visual skeleton** of the post:
- **Background** â€” cream-based with subtle texture, grid pattern, or artistic gradient (matching the brand `#F5F2ED` palette)
- **Layout structure** â€” visual containers for content: card shapes, tier bars, grid cells, mind-map nodes, section dividers
- **Decorative elements** â€” icons, illustrations, abstract shapes, gradients, visual accents
- **Brand logos** â€” real brand logos naturally integrated (e.g., Claude logo, ChatGPT logo, tool icons)
- **Photos** â€” real person photos if relevant to the content (e.g., Inspo_05 style)
- **Color coding** â€” category colors on cards, tier bars, badges (the visual framework the text will sit on)

### What Codex image tool does NOT generate

- **NO text of any kind** â€” no titles, no item names, no descriptions, no numbers, no handle, no footer
- **NO typography** â€” all text comes from the HTML overlay
- The composition should have **clear empty zones** where text will be placed â€” these zones should be visually defined (e.g., a white card area, a colored bar, a labeled region) but contain no actual text

### Composition prompting guidelines

The prompt to Codex image tool must describe the **complete visual layout** in detail. The model needs to understand the spatial arrangement so the text overlay aligns correctly.

**General prompt structure:**

```
Professional Instagram infographic composition, 4:5 portrait format, 1080x1350 pixels.
[BACKGROUND DESCRIPTION: cream/warm palette, subtle grid, artistic texture].
[LAYOUT DESCRIPTION: specific arrangement of visual containers â€” cards, bars, circles, etc.].
[DECORATIVE ELEMENTS: icons, illustrations, brand logos with specific positions].
[COLOR CODING: which containers use which colors from the brand palette].
Leave ALL text areas empty â€” no text, no typography, no letters, no numbers anywhere in the image.
Clean, editorial, magazine-quality design. NOT generic AI template aesthetics.
```

**Key prompt rules:**
- **Always end with "No text, no typography, no letters, no numbers anywhere in the image"** â€” Codex image tool tends to add text if not explicitly told not to
- **Describe the layout spatially** â€” "top section has...", "center area contains a 3x3 grid of cards", "bottom strip has..."
- **Reference the color palette by name** â€” "cream background (#F5F2ED)", "coral accent circles (#E85D3C)", "soft purple card borders"
- **Describe empty zones explicitly** â€” "each card has empty white space in the center where text will be added later"
- **Use `--aspect-ratio 4:5`** to match the Instagram canvas
- **Default `--quality high`** for the editorial density compositions require; switch to `--quality medium` when iterating on the prompt wording to save cost

### Prompt templates per layout pattern

#### Layout A â€” Numbered list
```
Professional Instagram infographic composition, 4:5 portrait, 1080x1350px.
Warm cream background (#F5F2ED) with subtle grid pattern.
Top area: empty space for title text (no text).
Below the title: [N] horizontal card rows stacked vertically with small gaps.
Each card is a white rounded rectangle with soft shadow.
Left side of each card: a coral (#E85D3C) circle (for the number â€” leave the circle empty, no number).
Center of each card: empty white space for item title and description text.
Right side of each card: [optional: small icon/logo relevant to the item â€” describe specifically].
Bottom: thin footer area with empty space for footer text.
No text, no typography, no letters, no numbers anywhere in the image.
Clean, editorial infographic design. Magazine quality.
```

#### Layout B â€” Grid cards
```
Professional Instagram infographic composition, 4:5 portrait, 1080x1350px.
Warm cream background (#F5F2ED) with subtle grid texture.
Top area: empty space for title (no text).
Main area: a [2x3 / 3x3] grid of white rounded cards with soft shadows.
Each card has a colored top border (varying colors: coral, orange, green, blue, purple â€” one per card).
Inside each card: a small colored circle at top-left (empty, for number) and empty white space for text.
Cards are evenly spaced with 16-20px gaps between them.
Bottom: footer area with empty space.
No text, no typography, no letters, no numbers anywhere in the image.
Polished editorial design, professional infographic layout.
```

#### Layout C â€” Tier list / Pyramid
```
Professional Instagram infographic composition, 4:5 portrait, 1080x1350px.
Warm cream background (#F5F2ED) with subtle grid.
Top area: empty space for title (no text).
Center: a pyramid/tier structure with [N] horizontal bars stacked vertically.
Top bar is narrowest (~55% width), bottom bar is widest (~95% width).
Each bar has a different color: [describe colors top to bottom â€” coral, orange, green, blue, purple].
Bars have rounded corners and soft shadows, separated by small gaps.
Inside each bar: empty space for tier label and item names. Also include small [brand/app] icons naturally arranged inside each bar.
Bottom: footer area.
No text, no typography, no letters, no numbers anywhere in the image.
```

#### Layout D â€” Mind map / Radial
```
Professional Instagram infographic composition, 4:5 portrait, 1080x1350px.
Warm cream background (#F5F2ED) with subtle grid.
Center: a large coral (#E85D3C) circle (hub) â€” empty inside (title text will be added).
Around the center: [N] white rounded-rectangle satellite nodes arranged radially, connected to the center by thin dashed lines.
Each satellite node has a small colored number circle at top-left (empty) and empty space for text inside.
Nodes are evenly distributed around the central hub with balanced spacing.
Some nodes may have a subtle coral-tinted callout box at the bottom.
No text, no typography, no letters, no numbers anywhere in the image.
Elegant, organized mind-map layout. Magazine infographic quality.
```

#### Layout E â€” Sectioned cheatsheet
```
Professional Instagram infographic composition, 4:5 portrait, 1080x1350px.
Warm cream background (#F5F2ED) with subtle grid.
Top area: compact space for title (no text).
Main area: [2â€“4] large white section cards stacked vertically with generous spacing.
Each section card has a colored left border (coral, green, blue, purple â€” one per section).
Inside each card: a header row area (empty, for section title) and below it a 2-column layout of empty content areas.
Optional: one section includes a dark (#1A1A1A) code-block area with rounded corners.
Bottom: footer area.
No text, no typography, no letters, no numbers anywhere in the image.
Reference-card quality, clean and organized.
```

#### Layout F â€” Single feature / Hero card
```
Professional Instagram infographic composition, 4:5 portrait, 1080x1350px.
Warm cream background (#F5F2ED) with subtle grid.
Top area: generous space for a large title (no text).
Center: one large white card with pronounced rounded corners and deep shadow, taking up ~70% of the width.
Inside the card: [describe the visual â€” e.g., a code editor mockup, a UI screenshot recreation, a prompt template area]. The card interior has empty space for text content.
Below the card: empty space for supporting context text.
Bottom: footer area.
[Optional: decorative elements around the card â€” subtle sparkle icons, connecting lines, brand logo].
No text, no typography, no letters, no numbers anywhere in the image.
Bold, high-impact single-feature layout.
```

#### Layout G â€” Comparison / Before-After
```
Professional Instagram infographic composition, 4:5 portrait, 1080x1350px.
Warm cream background (#F5F2ED) with subtle grid.
Top area: space for title (no text).
Main area: two columns side by side, separated by a thin vertical divider or "VS" badge shape.
Left column: [3-5] rows with grey/red-tinted accent markers (representing "before/without").
Right column: [3-5] rows with green/coral-tinted accent markers (representing "after/with").
Each row has empty space for item text.
Optional: a circular badge between the columns with space for "VS" text.
Bottom: footer area.
No text, no typography, no letters, no numbers anywhere in the image.
Clean comparison layout, balanced and symmetrical.
```

### Workflow for generating the composition

> **IMPORTANT: Generate ONE composition only.** The user trusts the prompt crafting to produce a good result on the first try. Do NOT generate 2â€“3 variants â€” that creates unnecessary variants. Only generate a second composition if the user explicitly rejects the first one.

1. **Choose the layout pattern** (Aâ€“G) based on the content
2. **Craft the composition prompt** using the template above, customized for the specific topic:
   - Specify exact number of items/cards/tiers
   - Describe any brand logos needed (check `Logos/` first â€” if the real logo exists, use image references)
   - Describe decorative elements specific to the topic
   - Specify the category colors for each card/tier/section
3. **Check `Logos/` and `Assets/`** â€” if brand logos or person photos exist, use image references mode
4. **Generate ONE composition:** use Codex's integrated image tool and save the approved result as `PostTypes/informativos/Outputs/{topic-slug}/composition.png`
   The script crops + resizes internally, so `composition.png` is guaranteed to be exactly 1080Ã—1350. No separate resize step is needed.
5. **Present to user for review** â€” only regenerate if they reject it
6. Once approved, proceed to the **HTML text overlay step**

### Quality checklist for compositions
- Layout structure is clear and matches the chosen pattern
- Empty text zones are clearly defined (white space, card areas, bar interiors)
- Brand logos are visible and naturally integrated (not pasted-looking)
- Color coding matches the brand palette
- No AI-generated text or artifacts in the image
- Overall feel: professional magazine infographic, not "AI template"
- The composition looks like ONE cohesive design, not separate elements

---

## 5. PIL text compositing â€” the second layer

> **After the Codex image tool composition is approved, PIL renders all text directly on top of it.** This eliminates Chrome border artifacts that occur when using HTML+render.sh with background images.

### Why PIL (not HTML/Chrome) for informativos

Chrome on Windows introduces border artifacts when rendering HTML with a background-image. PIL composites text directly onto the image â€” no browser, no viewport issues, pixel-perfect output at exactly 1080x1350.

### PIL workflow

```python
from PIL import Image, ImageDraw, ImageFont

# 1. Load composition
comp = Image.open("composition.png").convert("RGBA")
if comp.size != (1080, 1350):
    comp = comp.resize((1080, 1350), Image.LANCZOS)
canvas = comp.copy()
draw = ImageDraw.Draw(canvas)

# 2. Load fonts from Assets/Fonts/
font_name = ImageFont.truetype("Assets/Fonts/Inter-ExtraBold.ttf", 30)
font_badge = ImageFont.truetype("Assets/Fonts/Inter-Bold.ttf", 14)
font_desc = ImageFont.truetype("Assets/Fonts/Inter-Medium.ttf", 18)

# 3. Draw text centered on blob positions (from connected component analysis)
# 4. Save
canvas.convert("RGB").save("output.png", quality=95)
```

### Text drawn directly â€” no white card backgrounds

Text sits **directly on the composition** without semi-transparent rectangles. The white oval interiors provide enough contrast. White card backgrounds overlap with colored blob borders and look "pasted on."

### Finding exact text positions â€” connected component analysis (MANDATORY)

**Never guess pixel coordinates manually.** Use scipy connected component analysis to find the exact white interiors:

```python
from PIL import Image
import numpy as np
from scipy import ndimage

comp = Image.open("composition.png").convert("RGB")
arr = np.array(comp)

# Pure white pixels (>252) = blob interiors, not cream bg (~245)
white = np.all(arr > 252, axis=2)
labeled, n = ndimage.label(white)

for i in range(1, n+1):
    mask = labeled == i
    size = np.sum(mask)
    if size > 3000:  # only large regions = actual blob interiors
        coords = np.argwhere(mask)
        cy, cx = int(coords[:,0].mean()), int(coords[:,1].mean())
        print(f"center=({cx},{cy}), pixels={size}")
```

This gives the **exact center** of each white oval. Text is then centered on these coordinates. Manual estimates can be off by 100+ pixels on irregular organic shapes.

### No white card backgrounds

Text is drawn **directly on the composition** without semi-transparent rectangles behind it. The white oval interiors already provide the contrast needed for readability. Adding white rectangles overlaps with the colored blob borders and looks "pasted on."

---

## 6. Layout patterns â€” conceptual reference

These 7 patterns guide BOTH the Codex image tool prompt (section 4) AND the HTML text overlay (section 5). Choose the one that best fits the content.

### Layout A â€” Numbered list (the default)
**Best for:** "Top N...", "X tips para...", "X hacks de...", any numbered list.
- 5â€“9 items stacked vertically as horizontal card rows
- Each card: colored number circle + title + description + optional icon
- Items separated by card gaps

### Layout B â€” Grid cards
**Best for:** Tips with explanations, rule sets, cheatsheets with sections.
- 2â€“3 column grid of cards (4â€“9 cards)
- Each card: icon/number + title + 2â€“3 bullet points
- Cards have white background with colored top-border for category

### Layout C â€” Tier list / Pyramid
**Best for:** Rankings, hierarchies, capability layers.
- 4â€“7 stacked horizontal bars, progressively wider (pyramid) or same width
- Each bar: different color, tier label + item icons/names
- Bars separated by small gaps

### Layout D â€” Mind map / Radial
**Best for:** Central concept with related ideas radiating outward.
- Central circle (hub) with 6â€“9 satellite nodes arranged radially
- Connecting lines from center to each node
- Each node: number + title + description + optional callout
- **Most technically challenging** â€” positioning needs careful calculation

### Layout E â€” Sectioned cheatsheet
**Best for:** Reference cards, multi-section guides, "everything you need to know."
- 2â€“4 major sections, each as a white card with colored left-border
- Each section: section header + content area (mini-list, table, bullets)
- Optional code block section

### Layout F â€” Single feature / Hero card
**Best for:** One killer prompt, one hack, high visual impact.
- Large central card with prominent shadow
- Inside: prompt text, code snippet, or UI recreation
- Supporting context text below
- Lots of whitespace â€” quality > quantity

### Layout G â€” Comparison / Before-After
**Best for:** "X vs Y", "antes vs despuÃ©s", "con IA vs sin IA."
- Two columns side by side with divider or "VS" badge
- Left column: "antes/sin" items (grey/red accent)
- Right column: "despuÃ©s/con" items (green/coral accent)

---

## 7. Highlight & accent rules for informativos

### Title highlighting
- Same as covers: **1â€“2 keywords highlighted** (coral text or yellow marker)
- The **number** in the title is almost always highlighted: `<span class='accent-coral'>9</span> reglas de oro`
- If there's a brand name, it can be the second highlight

### Item-level highlighting
- **Numbered badges** use the category color palette (coral circle with white number by default)
- **Key terms** inside item descriptions can be **bold** but NOT colored â€” too many colors in body text creates chaos
- **One callout box** per post can use a yellow `#FFE45C` background at 15% opacity as a "pro tip" highlight

### What NOT to highlight
- Don't color every item title differently (unless it's a tier list where color = tier)
- Don't use yellow marker on body text (only on titles)
- Don't put coral on more than 2 words in the title

---

## 8. Icon system and brand logos

### Icons in the composition

Since Codex image tool generates the visual composition, icons and decorative elements are **baked into the image**. When prompting Codex image tool:
- Describe icons by their concept, not SVG code: "a lightning bolt icon", "a shield icon", "a brain illustration"
- Specify the icon style: "stroke-based, minimalist, matching the editorial aesthetic"
- Specify colors: "coral icon", "grey icon", "blue icon"

### Brand logos

When the post references **real brands** (Claude, ChatGPT, Perplexity, etc.):

1. **Check `Logos/` first** â€” if the real logo exists, describe it in the prompt or use image references
2. **If not in `Logos/`** â†’ include the logo in the Codex image tool composition prompt: "the [Brand] logo naturally integrated into the card/section"
3. **Alternatively, generate the logo separately** with Codex image tool, save to `Logos/`, then use it as a reference in the main composition
4. **Always present generated logos to the user for review**

---

## 9. Anti-patterns (informativo-specific)

In addition to the brand-wide anti-patterns:

- âŒ **Generic AI template aesthetics** â€” the composition must look editorially designed, not like a Canva template
- âŒ **Text in the Codex image tool composition** â€” ALL text comes from HTML overlay. No exceptions.
- âŒ **"PASO X" labels** â€” that's tutorial language, not informativo
- âŒ **Logo bubble connectors** â€” that's the step-by-step cover identity
- âŒ **Alta Studio watermark** â€” watermark is news-only. NOT on informativos.
- âŒ **Misaligned text overlay** â€” text must align precisely with the composition's visual zones. Always verify.
- âŒ **Cramped text** â€” if you can't read every word at 50% zoom, the layout is too tight. Cut items.
- âŒ **Rainbow explosion** â€” using all 7 category colors at once. Max 5 per post.
- âŒ **Tiny unreadable text** â€” minimum text size is 16 px. If content doesn't fit at 16 px, reduce items.
- âŒ **Generic filler content** â€” every item must deliver real, specific value
- âŒ **Walls of text** â€” descriptions are 1â€“2 lines max per item
- âŒ **Emojis as icons** â€” icons are part of the Codex image tool composition, not emoji characters
- âŒ **Generating multiple composition variants** â€” ONE only, regenerate only if user rejects it
- âŒ **Using Codex image tool assets without user review** â€” always present the composition for approval
- âŒ **Carousel when single image works** â€” default to single image
- âŒ **Missing number in title** â€” informativos almost always have a number
- âŒ **"Desliza â†’" on single-image posts** â€” no swiping on single images
- âŒ **Clickbait exclamation marks** â€” no "INCREIBLE!" or "NO VAS A CREER!"
- âŒ **Dark background** â€” informativos are cream-based (unlike news). The Codex image tool composition should maintain the warm cream aesthetic.
- âŒ **Pure HTML+CSS+SVG compositions** â€” the old approach. Always use Codex image tool for the visual composition now.

---

## 10. Caption structure for informativos

Like news posts, informativos come with a **caption** that complements the image. The tone is conversational and value-driven.

### Caption structure

1. **Hook** (1 line) â€” the promise. What they'll get from this post.
2. **Context** (1â€“2 lines) â€” why this matters now.
3. **Key takeaways** (3â€“5 short paragraphs) â€” expand on the most interesting items. Each paragraph = 1â€“2 sentences.
4. **Personal angle** (1â€“2 lines) â€” what YOU (the creator) use or recommend.
5. **Soft CTA** (1 line) â€” "Guarda este post para cuando lo necesites." or "Cual es tu favorita?"

### Caption rules

| Rule | Detail |
|---|---|
| Language | Colombian Spanish, tu form |
| Tone | Conversational, expert but approachable. Not academic, not clickbaity |
| Paragraphs | Short (1â€“2 sentences), separated by blank lines |
| Length | 100â€“250 words (shorter than news â€” the image carries more information) |
| Emojis | NO emojis |
| Hashtags | NO â€” user adds them later |
| Numbers | Use digits: "7 modelos", "2026", "$20/mes" |
| CTA style | Soft. "Guarda", "Comenta", "Comparte" â€” never aggressive |

### Caption delivery

Save as `caption.txt` in the output folder alongside the image files.

---

## 11. Workflow when the user asks for an informativo

> **Two workflows exist depending on format: single-image vs. multi-slide carousel.**

### 11.A â€” Single-image informativos (default)

1. **Read this skill** + brand-wide rules from [`CLAUDE.md`](../../../CLAUDE.md).
2. **Mandatory visual re-anchoring:** review `Inspiracion/` AND `Favoritos_Claude_Generated/` (see CLAUDE.md section 1.5).
3. **Understand the topic:** What information is being presented? How many items? What's the natural structure?
4. **Choose the layout pattern** (Aâ€“G from section 6) based on the content type.
5. **Check `Logos/` and `Assets/`** for any brand logos or photos needed.
6. **Propose the content breakdown** to the user:
   - Title (with highlighted keywords marked)
   - Layout pattern choice (with reasoning)
   - List of items/sections with their titles and 1-line descriptions
   - Wait for approval before generating.
7. **Draft the caption** and present alongside the content breakdown (no approval needed for captions).
8. **Generate ONE visual composition with Codex image tool.** This is the key step:
   - Craft the best possible prompt using the layout template from section 4, customized for the topic
   - Use existing logos/photos as visual references when appropriate
   - Use a 4:5 target for the Instagram canvas
      - **Generate ONE composition only** unless the user rejects it
   - Save or resize the final composition to exactly 1080x1350
   - **Present to user for review** â€” only regenerate if rejected
9. **PIL text overlay** on the approved composition (see section 5).
10. **MANDATORY visual verification** (Visual QA skill) â€” inspect every PNG before presenting.
11. **Present the complete deliverable:** rendered image + caption.
12. **Ask which images are favorites** for `Favoritos_Claude_Generated/`.

### 11.B â€” Multi-slide informativo carousels (HYBRID approach)

When the informativo has **multiple slides** (cover + content slides), use this hybrid workflow:

> **Cover = Codex image tool (editorial photo composition). Content slides = HTML+CSS (step-by-step structure).**

**Why this hybrid:** Codex image tool produces stunning editorial cover photos but is unreliable for content slides â€” text positioning on generated compositions requires guessing pixel coordinates, leading to misaligned text and wasted iterations. HTML+CSS gives pixel-perfect control over mockups, code editors, terminals, and typography.

1. Steps 1â€“7 are the same as 11.A (load skills, re-anchor, propose breakdown, draft caption).
2. **Cover slide â€” Codex image tool composition:**
   - Generate ONE editorial photo composition (person + brand elements + warm tones)
   - PIL text overlay for the title, handle, subtitle, slide indicator, and "Desliza â†’"
   - **Title must be BIG (64px+ Inter ExtraBold)** and clearly visible â€” positioned where it has good contrast against the photo
   - Yellow highlight and coral accents must be properly centered on the text they wrap
   - Present to user for review
3. **Content slides â€” HTML+CSS (step-by-step structure):**
   - Use the cream background + grid system from step-by-step posts
   - Include: `@lucianomusellaa` handle, coral number badge (not "PASO X"), bold headline with single coral highlight, subtitle, UI mockup (code editor, terminal, diagram â€” recreated in HTML/CSS), chevrons, slide indicators
   - Last slide: include CTA ("Guarda este post") and omit "Desliza â†’"
   - Render via `./render.sh`
4. **MANDATORY visual verification** â€” inspect every PNG.
5. **Present the complete deliverable:** cover + content slides + caption.
6. **Ask which images are favorites** for `Favoritos_Claude_Generated/`.

### Naming convention for informativo output files

```
PostTypes/informativos/Outputs/{topic-slug}/
â”œâ”€â”€ composition.png              â† Codex image tool full visual composition (NO text)
â”œâ”€â”€ info_v1_{descriptor}.html    â† HTML text overlay (references composition.png as background)
â”œâ”€â”€ info_v1_{descriptor}.png     â† Final rendered image (composition + text)
â”œâ”€â”€ caption.txt                  â† Caption for Instagram
â””â”€â”€ ...
```

- `{topic-slug}`: kebab-case. E.g. `top-7-modelos-ia`, `reglas-claude`, `hacks-prompts`.
- `{descriptor}`: layout or variation label. E.g. `numbered-list`, `grid-cards`, `tier-pyramid`.

---

## 12. Quick reference checklist (run before exporting any informativo)

### Composition (Codex image tool)
- [ ] Composition generated with Codex image tool at 4:5 aspect ratio
- [ ] Layout structure matches the chosen pattern (Aâ€“G)
- [ ] Empty text zones are clearly defined
- [ ] Brand logos are visible and naturally integrated (not pasted-looking)
- [ ] No AI-generated text or typography artifacts in the composition
- [ ] Color palette matches brand (cream-based, coral/yellow accents)
- [ ] Composition was presented to user and approved before proceeding

### HTML text overlay
- [ ] Canvas is 1080x1350
- [ ] Composition is the `background-image` filling edge to edge
- [ ] `@lucianomusellaa` at top (NOT @ramiro.cubria)
- [ ] Title has a number and 1â€“2 highlighted keywords
- [ ] Text elements align precisely with composition visual zones
- [ ] All items are readable at 50% zoom (minimum 16 px text)
- [ ] Category colors used sparingly (max 5 per post)
- [ ] No Alta Studio watermark (that's news-only)

### Content
- [ ] **Colombian Spanish only** â€” no voseo (crea, usa, etc.)
- [ ] Content is specific and useful (no generic filler)
- [ ] Caption drafted and saved as `caption.txt`
- [ ] Single image unless content genuinely requires carousel

### Delivery
- [ ] Saved to `PostTypes/informativos/Outputs/{topic-slug}/`
- [ ] Rendered via `./render.sh` (uses `--window-size=1098,1550` + PIL crop to handle Chrome's viewport bug â€” content below yâ‰ˆ1272 was invisible with the old window size)
- [ ] Visual QA passed â€” every PNG inspected, text alignment verified, bottom elements (dots, footer, handle) visible
- [ ] Asked user which images are favorites for `Favoritos_Claude_Generated/`

---

## 13. Adapting complexity to content â€” "readability budget"

| Content type | Density level | Layout recommendation |
|---|---|---|
| "Top 5 tools" (simple list) | Medium | Layout A with breathing room |
| "9 rules" (each needs explanation) | High | Layout B (3x3 grid) or Layout D (mind map) |
| "Complete cheatsheet" | Very high | Layout E, possibly 2-slide carousel |
| "1 killer prompt" | Low | Layout F (hero card, lots of whitespace) |
| "X vs Y comparison" | Medium | Layout G |
| "Tier ranking" | Medium-high | Layout C |

**The golden rule:** if you have to shrink text below 16 px to fit everything, you have too much content. Either cut items, simplify descriptions, or split into a carousel. Legibility is non-negotiable.


