---
name: informativo-post-design
description: Visual system for informative Instagram posts (hacks/tips/lists/cheatsheets/tier lists/mind maps). 7 layout patterns (A-G), each rendered as Higgsfield full-canvas composition + HTML/PIL text overlay. Uses brand v2 palette (Roboto + Playfair Italic, scheme-aware) -- see Brand/brand-spec.md.
type: skill
---

# Informativo Post Design (brand v2)

> **Project root:** `c:/Trabajo_AI/Visual_posts/`. The autoloaded [CLAUDE.md](../../../CLAUDE.md) is the master router. The informativo workflow lives in [../README.md](../README.md). The **brand visual system lives in [Brand/brand-spec.md](../../../Brand/brand-spec.md)** -- this skill builds on top of it.

Informativos are the **densest, most save-worthy posts** in the project. They're standalone infographics, hacks lists, cheatsheets, tier lists, mind maps. The hook is: "this is so dense and useful that I'm going to save it for later."

**Workflow (updated 2026-05-23):** Every informativo = **one single Higgsfield generation** with ALL text content baked in -- title, item names, descriptions, handle, all rendered by the model. **No HTML overlay. No two-step pipeline.** This eliminates the manual text-positioning issues that plagued the previous "composition + HTML overlay" approach.

If a specific generation comes out poorly (misspelled word, layout broken), regenerate with a refined prompt. Do NOT patch via HTML. Only as a last resort, after 2-3 failed regenerations, fall back to the two-step approach as a one-off (and flag it to the user).

---

## 1. Brand fundamentals (delegated to brand-spec.md)

All palette, typography, and the `@font-face` block live in [Brand/brand-spec.md](../../../Brand/brand-spec.md). Informativo-specific notes:

- **Canvas:** 1080 × 1350 px (4:5 portrait)
- **Mode (LIGHT or DARK):** asked at session start
- **Color scheme (AMARILLO/ROJO/AZUL):** asked at session start. Drives highlight color in headlines, badges, accent elements.
- **Fonts:** Roboto for everything readable; Playfair Display Italic for 1-2 emphasis words per title.
- **Category colors (informativo-only unlock):** when items need visual differentiation (tier lists, multi-tool lists, mind maps), informativos can use up to **5 distinct accent colors per slide** from the brand palette + acceptable secondary tones. See §3.

---

## 2. The 7 layout patterns (A through G)

Pick the pattern that fits the content:

| Layout | Pattern | Best for |
|---|---|---|
| **A** | Numbered list (vertical cards) | "9 reglas de oro para X", "7 prompts esenciales" |
| **B** | Grid cards (3×3 / 2×3 / 2×2) | "Top 6 herramientas de IA", "Las apps para 2026" |
| **C** | Tier list (S/A/B/C/D bars stacked) | "Tier list de modelos de IA", "Ranking de herramientas" |
| **D** | Mind map (central node + branches) | "El cerebro de un agente", "Anatomía de un buen prompt" |
| **E** | Cheatsheet (dense grid, many small items) | "Cheatsheet de comandos de Claude Code", "Atajos de teclado" |
| **F** | Hero card (one big concept + supporting text) | "La regla #1 de los prompts", "El error más común" |
| **G** | Comparison (2-column or before/after) | "ChatGPT vs Claude", "Sin agentes vs Con agentes" |

The exact prompt templates per layout live in §4 below.

---

## 3. Color palette (extended for informativos)

Informativos inherit the brand-spec palette PLUS unlock **category colors** for differentiation:

### Core (from brand-spec)
- Mode background + text per LIGHT/DARK
- Scheme highlight (primary accent for the chosen scheme)

### Category colors (informativo-only -- max 5 per slide)
When items need visual differentiation (e.g., tier list bands, multi-item lists), informativos may use additional accents drawn from the brand palette:

| Name | Hex | Use |
|---|---|---|
| Orange (scheme AMARILLO primary) | `#ffb050` | Default first accent |
| Red (scheme ROJO primary) | `#e60000` | Strong/urgent items |
| Blue (scheme AZUL primary) | `#0056a6` | Tech/data items |
| Navy | `#00386e` | Secondary tech |
| Soft warm gray | `#e4dfde` | Neutral background |
| Soft cool gray | `#c9d7da` | Alt-neutral background |
| Soft peach | `#ffc47f` | Soft accent / category 4 |
| Deep red | `#c30000` | Strong negative category |

**Rules:**
- Max **5 different colors per slide**. More than that = visual chaos.
- Category colors appear as **small elements** (badges, side borders, icon fills, number circles). Never as large background areas.
- Overall slide must still read as ~75% neutral with colored accents.
- When items don't need differentiation, stick to the scheme highlight + neutral text.

---

## 4. Generation prompts -- per layout

> **Default for ALL layouts (A through G):** single Higgsfield call with all text included in the prompt. Use `nano_banana_pro` at `resolution: "2k"`. The prompt explicitly lists every text element: title (with italic emphasis words flagged), subtitle, each card's number + name + description, handle at the bottom. The model renders all typography correctly for short structured content.
>
> **Two-step approach (composition only + HTML overlay) is a last-resort fallback** — only used if a specific generation fails repeatedly after prompt refinement. Not pre-decided by layout type. See §5 for that path documentation.

### Single-step prompt structure (default for grid layouts)

```
Professional Instagram infographic poster, 4:5 portrait format. Clean editorial magazine design on a [mode bg color] background with subtle grid texture.

TOP TITLE (centered, [text color], Roboto Bold sans-serif):
"[Title line 1]
[Title line 2]"
The word(s) '[emphasis word]' and '[emphasis word]' rendered in Playfair Display Italic serif in [scheme highlight color hex].

SUBTITLE: uppercase gray "[SUBTITLE TEXT]"

MIDDLE: [layout description -- e.g. "2 column by 3 row grid of 6 equal rounded white cards with soft drop shadows, small [scheme color] corner accent stripe at the top-left of each card"]

Each card contains the following text, perfectly centered, no overflow:

Card 1 (top-left):
- small [scheme color] label: "01"
- big bold name: "[Item name]" (the word "[brand]" in italic [scheme color] serif)
- description: "[Item description in Spanish, 1-2 short lines]"

[... repeat for each card ...]

BOTTOM: centered small text "@lucianomusellaa" in [scheme color].

Use Roboto sans-serif as the primary font and Playfair Display Italic serif for the highlighted brand names. Spanish text only. Magazine-quality typographic layout. No misspellings, no garbled text, no logos or watermarks. Aspect ratio 4:5.
```

### Layout A -- Numbered list

```
Professional Instagram infographic composition, 4:5 portrait, 1080×1350.
Cream background (#efedec) with subtle warm grid texture.
Top area: empty space for title text (no text).
Below the title: [N] horizontal card rows stacked vertically with small gaps (16-20px).
Each card is a clean rectangle with rounded corners, subtle drop shadow.
Left side of each card: a colored circle (alternating orange #ffb050, blue #0056a6, red #e60000) for the item number -- leave the circle EMPTY.
Right side of each card: empty white space (where item title and description will be added).
Clean editorial design, magazine-quality, NO text, no letters, no numbers anywhere in the image.
--ar 4:5
```

### Layout B -- Grid cards

```
Professional Instagram infographic composition, 4:5 portrait, 1080×1350.
Warm cream background (#efedec) with subtle grid.
Top area: empty space for title text.
Center: 3×3 grid of equal-sized rounded square cards (or 2×3 if only 6 items), small gap between.
Each card is white with a small color accent at the top-left corner (rotating brand palette: orange, red, blue, navy).
Inside each card: empty white space where icon and text will be added.
Bottom strip: thin neutral footer area, no text.
Editorial magazine design, NO text, no letters, no numbers anywhere.
--ar 4:5
```

### Layout C -- Tier list

```
Professional tier list infographic composition, 4:5 portrait, 1080×1350.
Cream background (#efedec).
Top: title bar area, empty (no text).
Below: 5 horizontal bands stacked vertically (S, A, B, C, D tiers).
Each band ~200px tall, full-width, rounded ends.
Band colors top to bottom: red #e60000 (S), orange #ffb050 (A), peach #ffc47f (B), soft cool gray #c9d7da (C), neutral gray #e4dfde (D).
Left side of each band: solid colored zone where the tier letter will be added (leave empty).
Right side of each band: empty space for item logos / names (no text).
Clean editorial design, NO text, no letters, no numbers anywhere.
--ar 4:5
```

### Layout D -- Mind map

```
Mind map composition, 4:5 portrait, 1080×1350.
Cream background (#efedec) with subtle grid.
Center: one large circular node, ~280px diameter, scheme highlight color outline (orange #ffb050 thick stroke 4px).
Around it: 6 smaller circular nodes (~140px each) connected by thin dashed lines (also scheme highlight color).
The 6 nodes positioned in a hexagonal pattern around the center.
All circles have empty white interior (no text inside).
Editorial design, organic feel, NO text anywhere.
--ar 4:5
```

### Layout E -- Cheatsheet

```
Dense cheatsheet composition, 4:5 portrait, 1080×1350.
Cream background (#efedec).
Top: title bar area, empty.
Below: a 4-column × 6-row grid of small rounded boxes.
Each box ~250×150px, white with thin border, very subtle drop shadow.
Inside each box: a small colored stripe at the top (rotating colors), then empty space.
Bottom: thin footer area, empty.
Clean code-cheat-sheet aesthetic, magazine reference card quality, NO text anywhere.
--ar 4:5
```

### Layout F -- Hero card

```
Hero card composition, 4:5 portrait, 1080×1350.
Cream background (#efedec) with subtle grid.
Top: small label area, empty (no text).
Center: one large rounded white card, ~900×700px, soft drop shadow.
The card has a colored accent stripe at the top edge (scheme highlight color).
Inside the card: large empty zone where headline text will be added, plus small decorative elements at the corners (subtle scheme-color sparkles or geometric shapes).
Bottom: thin source/footer area, empty.
Editorial bold design, NO text anywhere.
--ar 4:5
```

### Layout G -- Comparison (2-column / before-after)

```
2-column comparison composition, 4:5 portrait, 1080×1350.
Top: title area + small subtitle area, both empty.
Center: two equal-width vertical zones separated by a thin vertical divider.
Left zone: light cream background, neutral color band at top (gray #c9d7da).
Right zone: scheme highlight tinted background (subtle orange #fff5e6), warm color band at top (orange #ffb050).
Each zone has empty space for item lists (no text).
Bottom: synthesis card area, empty.
Editorial side-by-side design, NO text, no letters, no numbers anywhere.
--ar 4:5
```

### Universal prompt rules (single-step approach)

1. **Model:** `nano_banana_pro` (better text rendering than Soul 2.0). Set `resolution: "2k"` to get true 1080×1350.
2. **Background:** use the chosen mode's primary background token from brand-spec (e.g. `#efedec` LIGHT, `#11191b` DARK).
3. **Color references:** mention hex codes inline (`cream #efedec`, `scheme blue #0056a6`, `Playfair Italic blue #0056a6`).
4. **Italic emphasis:** explicitly say "rendered in Playfair Display Italic serif in [color]" -- the model honors this.
5. **Spanish accents:** write them out correctly in the prompt (Diseña, código, DÍAS, fuentes verificables). Model preserves them.
6. **Negative directive:** end with "no misspellings, no garbled text, no logos or watermarks".
7. **Aspect ratio:** always `4:5`.
8. **Verify visually:** since the model is rendering text, ALWAYS read the output PNG and verify spelling + alignment before presenting. If a word is misspelled, regenerate (don't try to patch via HTML).

### Two-step approach (LAST-RESORT fallback only)

If, after 2-3 refined regenerations, a specific informativo still comes out broken (misspelled brand name that won't fix, layout structure that won't render, text overflow that won't go away), fall back to two-step ON THAT ONE POST. Flag it to the user as a fallback, not a routine path.

1. Generate composition only (no text) — end the prompt with "no text, no letters, no numbers anywhere"
2. Use `informativo-visual-iteration` skill with scipy blob detection to find exact text zones
3. Overlay text via PIL or HTML using the canonical `@font-face` block from `Brand/brand-spec.md`

Track which layouts/topics required fallback. If a pattern emerges (e.g. mind maps always need fallback), update this skill to document that exception. Until then, the default is single-step for everything.

---

## 5. HTML overlay (text on the composition)

After Higgsfield delivers the composition, HTML overlays the text. The composition is referenced as `background-image: url('composition.png')` and absolutely-positioned text elements align to the composition's empty zones.

### Finding exact text positions

For organic compositions (mind maps, blob layouts), DO NOT guess pixel positions. Use the `informativo-visual-iteration` skill ([Skills/informativo-visual-iteration.md](../../../Skills/informativo-visual-iteration.md)) which uses scipy connected-component analysis on the composition's white interiors to detect exact blob centers.

For grid layouts (Layout B, C, E), positions are predictable from the prompt -- just compute card positions deterministically.

### Overlay scaffold

```html
<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8">
<style>
  /* @font-face block -- canonical, see Brand/brand-spec.md §2 */
  @font-face { font-family: 'Roboto'; src: url('../../../../Brand/Fonts/Roboto/static/Roboto-Regular.ttf') format('truetype'); font-weight: 400; font-style: normal; font-display: block; }
  @font-face { font-family: 'Roboto'; src: url('../../../../Brand/Fonts/Roboto/static/Roboto-Medium.ttf')  format('truetype'); font-weight: 500; font-style: normal; font-display: block; }
  @font-face { font-family: 'Roboto'; src: url('../../../../Brand/Fonts/Roboto/static/Roboto-Bold.ttf')    format('truetype'); font-weight: 700; font-style: normal; font-display: block; }
  @font-face { font-family: 'Roboto'; src: url('../../../../Brand/Fonts/Roboto/static/Roboto-Black.ttf')   format('truetype'); font-weight: 900; font-style: normal; font-display: block; }
  @font-face { font-family: 'Playfair Display'; src: url('../../../../Brand/Fonts/PlayfairDisplay/static/PlayfairDisplay-Italic.ttf') format('truetype'); font-weight: 400; font-style: italic; font-display: block; }

  * { margin:0; padding:0; box-sizing:border-box; }
  body {
    width:1080px; height:1350px;
    background-image: url('composition.png');
    background-size: cover; background-position: center;
    font-family: 'Roboto', sans-serif; color:#0c1314;
    position: relative;
  }
  .handle { position:absolute; bottom:34px; left:0; right:0; text-align:center; color:#ffb050; font-size:20px; font-weight:500; }
  .title { position:absolute; top:80px; left:60px; right:60px; font-size:54px; font-weight:700; line-height:1.1; text-align:center; }
  .title-emphasis { font-family:'Playfair Display'; font-style:italic; font-weight:400; color:#ffb050; }
  .item { position:absolute; /* set top/left per card */ font-weight:600; font-size:22px; }
  /* ... more positioned elements for each layout */
</style></head>
<body>
  <div class="title">
    <span class="title-emphasis">9</span> reglas de oro para configurar <span class="title-emphasis">Claude</span>
  </div>
  <!-- positioned items per the layout's grid -->
  <div class="handle">@lucianomusellaa</div>
</body></html>
```

### When to use PIL overlay instead of HTML

For organic-shape compositions (mind maps, blob layouts), use PIL compositing per [Skills/informativo-visual-iteration.md](../../../Skills/informativo-visual-iteration.md). PIL gives pixel-precise positioning aligned to scipy-detected centers. Chrome with `background-image` works fine for grid layouts but struggles with irregular shapes.

---

## 6. Title rules

The title is the hook -- promise enough value that the viewer saves the post.

| Property | Value |
|---|---|
| Word count | 5-14 words (longer than tutorial covers because it often includes a number) |
| Number in title | **Almost always** -- "9 reglas", "Top 7 modelos", "5 hacks" |
| Font size | 48-64px Roboto Bold (adjust based on content density) |
| Emphasis | 1-2 words in Playfair Italic + scheme highlight color. The **number** is almost always italicized. |
| Tone | Colombian Spanish, `tú` form. Factual + useful. |

### Good informativo titles
- "*9* reglas de oro para configurar *Claude*"
- "Top *7* modelos de IA para trabajar más inteligente"
- "Las mejores apps de *IA* para 2026"
- "*5* hacks de prompts que nadie te enseña"

---

## 7. Workflow when building an informativo

1. **Confirm type + color + mode** (per CLAUDE.md §1)
2. **Read brand-spec + this skill + visual-iteration skill**
3. **Re-anchor visually:** `Inspiracion/` and `Favoritos_Claude_Generated/`. Informativos templates don't exist in `Brand/Templates/` (none in user's upload), so rely on inspiration folder.
4. **Choose layout pattern (A-G)** based on the content. Confirm with user.
5. **Craft the composition prompt** following §4. Include negative directive + aspect ratio + seed.
6. **Generate composition via Higgsfield MCP** -- one image. Save as `composition.png` in `PostTypes/informativos/Outputs/{topic-slug}/`.
7. **Present composition to user.** Only regenerate if rejected.
8. **For organic compositions:** run scipy blob detection (Skills/informativo-visual-iteration.md §0) to find exact text positions.
9. **Write the HTML or PIL overlay** with text positioned at detected/computed coordinates.
10. **Render** via `render.sh` (for HTML overlays) OR via the PIL script (for organic compositions). Save to `output.png` or `slide_overlay.png`.
11. **Run the self-iteration loop** (Skills/informativo-visual-iteration.md §2) -- max 5 attempts to align text with composition before presenting.
12. **Mandatory Visual QA** ([Skills/visual-qa.md](../../../Skills/visual-qa.md))
13. **Present to user** + ask for favorites

---

## 8. Anti-patterns

- ❌ Asking Higgsfield to render any text inside the composition (typography is HTML/PIL's job)
- ❌ Using more than 5 distinct accent colors on a single slide
- ❌ Guessing pixel positions on organic compositions -- always use scipy detection (visual-iteration skill)
- ❌ Mixing Inter or Google Fonts CDN -- always use local Brand/Fonts via @font-face
- ❌ Page dots (Instagram handles pagination)
- ❌ Argentinian voseo in copy

---

## 9. Checklist (before exporting)

- [ ] Composition generated by Higgsfield (not Codex/gpt-image-1)
- [ ] No text rendered inside the composition image (all text comes from HTML/PIL)
- [ ] HTML/PIL fonts: Roboto + Playfair Italic loaded correctly (no fallback)
- [ ] Title has 1-2 italic emphasis words (usually the number + one keyword)
- [ ] Highlight color matches chosen scheme on every emphasis element
- [ ] Background composition uses mode-appropriate palette
- [ ] Max 5 accent colors total on the slide
- [ ] `@lucianomusellaa` handle present at bottom (informativos use it; news doesn't)
- [ ] No page dots
- [ ] Colombian Spanish only
- [ ] Saved to `PostTypes/informativos/Outputs/{topic-slug}/`
