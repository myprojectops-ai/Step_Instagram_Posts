# Brand Spec — @lucianomusellaa

**This file is the single source of truth for the visual system.** All skills (`PostTypes/*/Skills/*.md`, root `Skills/*.md`, `CLAUDE.md`, `AGENTS.md`) defer to this document for color, typography, and slide-pattern rules. If a skill contradicts this file, this file wins — update the skill.

Last updated: 2026-05-22 (brand migration v2)

---

## TL;DR — what to load before drafting any post

1. **Color scheme**: ask the user at the start of every post — `AMARILLO` (orange highlights), `ROJO` (red highlights), or `AZUL` (blue highlights).
2. **Mode**: ask the user at the start of every post — `LIGHT` (cream/off-white backgrounds) or `DARK` (black/navy backgrounds).
3. **Typography**: Roboto for everything readable; Playfair Display **Italic only** for 1–2 emphasis words per headline.
4. **Reference templates**: live in `Brand/Templates/Tutorial/{COLOR}/{STYLE}/{MODE}/` and `Brand/Templates/Noticias/{COLOR}/{MODE}/`. Open at least one before drafting HTML — that's your visual anchor for the post.

---

## 1. Color palette

### Light mode

| Role | Tokens | Notes |
|---|---|---|
| **Background (primary)** | `#efedec` `#e6ecee` `#ffffff` | `#efedec` is the standard "cream" used in most Tutorial light templates. |
| **Background (alt / cards)** | `#b4c8cd` `#e4dfde` | Soft blue-gray / warm gray for inner cards, callouts. |
| **Text (primary)** | `#000000` `#0c1314` `#11191b` | `#0c1314` is the canonical body text. |
| **Text (accent — navy)** | `#002b53` `#00386e` | For dark accent text on light bg. |
| **Text (subtle / alt)** | `#b4c8cd` `#e4dfde` | Use for footnotes, sources, very low-emphasis text. |

### Dark mode

| Role | Tokens | Notes |
|---|---|---|
| **Background (primary)** | `#000000` `#0c1314` `#11191b` | `#11191b` is the canonical body background — slightly warm black. |
| **Background (alt / accent)** | `#002b53` `#00386e` `#0056a6` | Navy variants used for gradients (dark→navy at slide bottom) and accent zones. |
| **Text (primary)** | `#ffffff` `#e6ecee` | `#ffffff` for headlines; `#e6ecee` for body. |
| **Text (subtle / alt)** | `#c9d7da` `#efedec` | Low-emphasis text in dark mode. |

### Highlights (both modes — color scheme dependent)

The "highlight" color is determined by the post's color scheme (AMARILLO / ROJO / AZUL). Use the bright token for primary emphasis, the dark token for solid-fill pills/buttons, the light token for hover/secondary highlights.

| Scheme | Primary highlight | Solid/pill fill | Light/secondary |
|---|---|---|---|
| **AMARILLO** | `#ffb050` (canonical orange) | `#ff9d00` (saturated) | `#ffc47f` (peach) |
| **ROJO** | `#e60000` | `#c30000` | `#ff0000` |
| **AZUL** | `#0056a6` | `#00386e` | `#c9d7da` (for soft callouts) |

**Bullet dot semantics (verdict / list slides):** semaphore — green for positive (`#22c55e` or similar — not in palette but acceptable for status), orange `#ffb050` for neutral/caution, red `#e60000` for negative.

---

## 2. Typography

### Fonts

- **Roboto** — primary. Used for body, headings, eyebrows, button labels, numbers. Weights to use:
  - `400` Regular — body
  - `500` Medium — body emphasis, small captions
  - `700` Bold — headlines, step titles
  - `900` Black — huge numbers (stat cards), big headlines in news covers
- **Playfair Display Italic** — emphasis only. Use for **1–2 words per headline** to add editorial character. Never use upright Playfair. Match the color to the post's highlight token.
- **Monospace** — terminal mockups. Use the system mono (Consolas, Menlo, JetBrains Mono if available) — no custom mono font required.

### Loading fonts in HTML (canonical `@font-face` block)

The HTML output lives at `PostTypes/<type>/Outputs/<post-slug>/<slide>.html`. From there, `../../../../Brand/Fonts/` reaches the fonts. Use this exact block at the top of every slide's `<style>`:

```css
@font-face {
  font-family: 'Roboto';
  src: url('../../../../Brand/Fonts/Roboto/static/Roboto-Regular.ttf') format('truetype');
  font-weight: 400; font-style: normal; font-display: block;
}
@font-face {
  font-family: 'Roboto';
  src: url('../../../../Brand/Fonts/Roboto/static/Roboto-Medium.ttf') format('truetype');
  font-weight: 500; font-style: normal; font-display: block;
}
@font-face {
  font-family: 'Roboto';
  src: url('../../../../Brand/Fonts/Roboto/static/Roboto-Bold.ttf') format('truetype');
  font-weight: 700; font-style: normal; font-display: block;
}
@font-face {
  font-family: 'Roboto';
  src: url('../../../../Brand/Fonts/Roboto/static/Roboto-Black.ttf') format('truetype');
  font-weight: 900; font-style: normal; font-display: block;
}
@font-face {
  font-family: 'Playfair Display';
  src: url('../../../../Brand/Fonts/PlayfairDisplay/static/PlayfairDisplay-Italic.ttf') format('truetype');
  font-weight: 400; font-style: italic; font-display: block;
}
@font-face {
  font-family: 'Playfair Display';
  src: url('../../../../Brand/Fonts/PlayfairDisplay/static/PlayfairDisplay-BoldItalic.ttf') format('truetype');
  font-weight: 700; font-style: italic; font-display: block;
}
```

- `font-display: block` is **mandatory** — keeps Chrome headless from rendering fallback fonts before the TTFs load (which produces the "wrong font on first paint" bug).
- Adjust the `../../../../` prefix if the HTML lives at a non-standard depth (e.g., a one-off test at the repo root needs `./Brand/Fonts/...`).
- Do **not** use Google Fonts CDN (`fonts.googleapis.com`) — render.sh runs headless on potentially-flaky networks and the local TTFs guarantee deterministic output.

### Type scale (suggested)

| Element | Size | Weight | Color |
|---|---|---|---|
| Eyebrow (e.g. "TUTORIAL · PASO 01") | 18–20px | 500 Medium, ALL CAPS, letter-spacing 2px | highlight primary |
| Headline (slide title) | 64–84px | 700 Bold | text primary |
| Headline emphasis (1–2 words) | same as headline | Playfair Italic 400 | highlight primary |
| Subheadline | 28–36px | 500 Medium | text primary |
| Body text | 22–28px | 400 Regular, line-height 1.4 | text primary |
| Caption / source | 14–16px | 500 Medium, ALL CAPS, letter-spacing 1.5px | text subtle |
| Huge stat number | 240–320px | 900 Black | text primary, with `%` or unit in Playfair Italic highlight |
| Pill button label | 32–48px | 500–700 | white-on-highlight or highlight-on-bg |

---

## 3. Slide patterns (canonical layouts)

These patterns come from the templates in `Brand/Templates/`. **Always open the matching template** before drafting HTML for a new slide — variations exist within each pattern and copying numbers/spacing visually is faster than re-deriving.

### Tutorial cover

```
┌─ 1080 × 1350 ────────────────────────────────────────┐
│                                                       │
│                   @lucianomusellaa                    │ ← orange small caps, top center
│                                                       │
│                                                       │
│              Crea tu propio                           │ ← Roboto Bold 80px, line 1
│              agente de IA con                         │ ← Roboto Bold 80px, line 2
│              ╔════════════════╗                       │
│              ║   Claude Code  ║                       │ ← Playfair Italic 80px, highlight color, line 3
│              ╚════════════════╝                       │
│                                                       │
│             ┌─────────────────────────┐               │
│             │ █████  en 4 pasos       │               │ ← pill solid highlight color, white text, Roboto 500
│             └─────────────────────────┘               │
│                                                       │
│         [terminal mockup, illustration, or            │ ← visual hook (terminal, orgchart, screenshot)
│          other concept-relevant visual]               │
│                                                       │
│             ╭──────────────╮                          │
│             │   Desliza    │                          │ ← pill outline, text primary
│             ╰──────────────╯                          │
└───────────────────────────────────────────────────────┘
```

### Tutorial step (interior)

```
┌─ 1080 × 1350 ────────────────────────────────────────┐
│                                                       │
│                                                       │
│                                                       │
│              TUTORIAL · PASO 01                       │ ← eyebrow, orange small caps
│                                                       │
│              Instala Claude Code                      │ ← Roboto Bold, headline
│              en tu  ╱terminal╲                        │ ← "terminal" in Playfair Italic highlight
│                                                       │
│                                                       │
│         ┌─────────────────────────────────┐           │
│         │ • • •      ~/mi-agente — bash   │           │
│         │                                 │           │
│         │ # instálalo globalmente con npm │           │
│         │    npm install -g …             │           │ ← terminal mockup
│         │                                 │           │
│         │ # entra a tu proyecto           │           │
│         │    cd mi-agente                 │           │
│         │    claude                       │           │
│         └─────────────────────────────────┘           │
│                                                       │
│                                                       │
└───────────────────────────────────────────────────────┘
```

Alternative content blocks below the headline: orgchart of "code-window" cards (with macOS dots top-left + green status dot top-right), numbered list with colored dots, comparison diagrams.

### Tutorial closer

Last slide. Same layout as a step but content is recap + call-to-action ("guarda este post", "sígueme para más", etc.) instead of a numbered step.

### News cover (4-slide carousel, slide 1)

```
┌─ 1080 × 1350 ────────────────────────────────────────┐
│                                                       │ ← full-bleed photo (Higgsfield)
│  ╲                                            ╱       │   takes top ~55% of canvas
│   ╲                                          ╱        │
│    ╲                                        ╱         │
│     ╲                                      ╱          │   gradient overlay: photo →
│      ╲                                    ╱           │   transparent → dark gradient
│       ╲                                  ╱            │   at the bottom transition
│        ╲                                ╱             │
│         ╲     IMAGEN — hardware…       ╱              │ ← image label (small caps, gray)
│          ╲                            ╱               │
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │
│ ANTHROPIC LANZÓ                                        │ ← Roboto Black ALL CAPS, white
│ ╱OPUS╲ 4.7: MÁS CÓDIGO,                                │ ← "OPUS" in Playfair Italic highlight color
│ MENOS ╱MEMORIA╲                                        │ ← "MEMORIA" in Playfair Italic highlight color
│ — ¿VALE EL ╱PRECIO╲?                                   │ ← "PRECIO" in Playfair Italic highlight color
│                                                        │
│ EL MODELO QUE PROMETÍA MÁS Y LLEGÓ CON SORPRESAS      │ ← subtitle, gray small caps
│                                                        │
└────────────────────────────────────────────────────────┘
```

The "X" diagonal cross visible in template PNGs is a **placeholder marker only** — never render it in the final output. The Higgsfield photo replaces that zone entirely.

### News body slide (text + photo split)

```
┌─ 1080 × 1350 ────────────────────────────────────────┐
│                                                       │
│  LA CONTROVERSIA                                      │ ← eyebrow orange small caps
│                                                       │
│  La memoria cayó de ╱78.3%╲ a solo ╱32.2%╲            │ ← body Roboto 500, percentages in highlight
│  en el test MRCR v2.                                  │
│                                                       │
│  Anthropic retiró el test: dice que no                │
│  mide la memoria como los humanos la usan.            │
│                                                       │
│  Y usa hasta ╱35% más tokens╲ en modo thinking        │
│  puede costar ╱35% más╲ por tarea.                    │
│                                                       │
│ ─────────────────────────────────────────────────     │ ← divider, then black photo zone
│                                                       │
│                                                       │ ← photo zone (Higgsfield)
│           IMAGEN — vidrio roto / circuito             │
│                                                       │
│                                                       │
└───────────────────────────────────────────────────────┘
```

### News stat card

```
┌─ 1080 × 1350 ────────────────────────────────────────┐
│  ┌─────────────────────────────────────────────┐      │
│  │                                              │     │
│  │  CODING BENCHMARK                           │      │ ← eyebrow
│  │                                              │     │
│  │     64.3%                                   │      │ ← huge Roboto Black, % in Playfair Italic highlight
│  │                                              │     │
│  │  SWE-BENCH VERIFIED PRO                     │      │ ← caption
│  │  El test más difícil de contaminar…         │      │ ← body
│  │                                              │     │
│  │  ┌──────┐  ┌──────┐  ┌──────┐               │     │
│  │  │57.7% │  │~63%  │  │64.3% │               │     │ ← comparison cards (gray boxes)
│  │  └──────┘  └──────┘  └──────┘               │     │
│  │                                              │     │
│  │  Fuente: SWE-bench …                        │      │ ← source line
│  └─────────────────────────────────────────────┘      │
└───────────────────────────────────────────────────────┘
```

### News verdict (closer)

```
┌─ 1080 × 1350 ────────────────────────────────────────┐
│  ┌─────────────────────────────────────────────┐      │
│  │  EL VEREDICTO                               │     │ ← eyebrow
│  │                                              │     │
│  │  4.7 se siente como un                      │     │
│  │  ╱4.6.1╲ con ╱training data╲                │     │ ← italic emphasis on key terms
│  │  nuevo.                                      │     │
│  │  ───────────                                │     │
│  │  ● Mejor en código                          │     │ ← green dot
│  │    (64.3% SWE-bench Pro) y comprensión …    │     │
│  │  ● Memoria deteriorada                      │     │ ← red dot
│  │    (78.3% 32.2% en MRCR v2)                 │     │
│  │  ● Puede costar hasta 30–150% más           │     │ ← orange dot
│  │    por tarea en producción                  │     │
│  └─────────────────────────────────────────────┘      │
└───────────────────────────────────────────────────────┘
```

### Informativo (single-step Higgsfield generation, text baked in -- 100% no HTML overlay)

**Updated 2026-05-23:** Informativos are now **always generated as a single Higgsfield call** with all text content (title, item names, descriptions, handle) included in the prompt. Use `nano_banana_pro` at `resolution: "2k"`. Tested on Layout B (grid cards) -- the model renders typography reliably: correct Spanish accents, requested Playfair Italic emphasis words, brand palette tokens, `@lucianomusellaa` handle.

**Rule:** every informativo = 1 Higgsfield call. No HTML overlay, no two-step composition + text pipeline.

**Mandatory visual QA:** since the model is rendering text, ALWAYS read the rendered PNG and verify spelling + layout before presenting. If a word is misspelled or a card is missing content, **regenerate with a refined prompt** -- do not patch via HTML.

**If a specific layout fails after 2-3 regenerations:** flag the issue to the user, then evaluate fallback to HTML overlay as a one-off (not as a layout-class rule). The current default is "always single-step" until evidence shows a layout class consistently breaks.

See `PostTypes/informativos/Skills/informativo-post-design.md` for the per-layout prompt templates with full text content embedded.

---

## 4. Higgsfield prompt anatomy

### Model selection -- which Higgsfield model for which slot

Tested 2026-05-23 with the same prompt:

| Model | Cost | 4:5 native | Respects "no text" | Mood |
|---|---|---|---|---|
| **`nano_banana_pro`** | 2 credits | ✅ Yes (1080×1350 at `resolution: "2k"`) | ✅ Yes (clean) | Literal, product-photo feel |
| `soul_2` | 1 credit | ❌ Adjusts to 3:4 | ❌ Text bleeds into image | Atmospheric, cinematic, editorial |

**Default: `nano_banana_pro`** for any slot where text-overlay is going to sit on the image (news covers, informativo compositions). The 4:5 native output + no-text guarantee outweighs the 2× cost.

**Use `soul_2`** for:
- Body slides where aspect ratio is forgiving (16:9 photos, accent shots)
- Slots where editorial mood matters more than literal subject interpretation
- When you can crop or post-process to handle text bleed and 3:4 aspect

For 16:9 body photos, Soul produces stronger editorial atmosphere -- worth the trade-off.

### Prompt structure (favors descriptive long-form, similar to Midjourney v6+, not terse DALL·E-style)

### Anatomy

```
[SUBJECT — specific noun + key adjectives]
[STYLE — editorial / cinematic / minimalist / photoreal etc.]
[COMPOSITION — framing, depth, angle]
[LIGHTING — natural, studio, dramatic, golden hour, etc.]
[PALETTE — limit to brand-friendly tones; avoid colors that clash with the mode]
[NEGATIVE — "no text", "no logos", "no watermarks"]
[ASPECT RATIO — explicit, e.g. --ar 4:5, --ar 16:9, --ar 1:1]
[SEED — same seed across slides of one carousel for stylistic consistency]
```

### Aspect ratios used in this project

| Slot | Ratio | Pixel target | When |
|---|---|---|---|
| News cover photo (full-bleed) | 4:5 | 1080 × 1350 | every news cover |
| News body photo (split) | 16:9 | 1080 × 608 | body slides with photo zone |
| News stat card icon (optional) | 1:1 | 1080 × 1080 | rare, decorative |
| Tutorial illustration | 16:9 | 1080 × 608 | inline visuals inside tutorial steps |
| Informativo full composition | 4:5 | 1080 × 1350 | every informativo |
| Logo (generated) | 1:1 | 1080 × 1080 | only when a brand logo is missing from `Logos/` |

### Boilerplate prompt fragments to reuse

- **News dark-mode photo:** "editorial dark mood, Financial Times aesthetic, high-contrast dramatic lighting, muted palette of deep black and navy with subtle warm highlights, photoreal, no text or logos"
- **News light-mode photo:** "soft editorial daylight, neutral warm tones, magazine-quality composition, palette of cream and soft gray with a single warm accent, photoreal, no text or logos"
- **Tutorial inline illustration:** "minimalist flat illustration, clean geometric shapes, brand palette of cream and orange accents, no text"
- **Informativo composition (tier list example):** "vertical layout with 5 horizontal bands stacked top-to-bottom, each band in a distinct color from the brand palette, clean editorial design, no text or numbers, photoreal lighting"

### Anti-patterns

- ❌ Asking Higgsfield to render text inside the image (typography is HTML's job, and Soul reliably mis-renders text)
- ❌ Asking for a logo of a real brand (use the assets in `Logos/` or generate only when missing — see CLAUDE.md §3.5.1)
- ❌ Prompts under 15 words — Soul produces generic AI-looking results

---

## 5. Templates as canonical reference

The `Brand/Templates/` folder is the visual ground truth. Before drafting any slide:

1. Open the matching template subfolder:
   - Tutorial: `Brand/Templates/Tutorial/{AMARILLO|ROJO}/{GRADIENTES|PLANO}/{DARK|LIGHT|LIGHT_DARK|DARK_LIGHT}/`
   - Noticias: `Brand/Templates/Noticias/{AMARILLO|AZUL|ROJO}/{DARK[ MODE]|LIGHT[ MODE]}/`
2. Read at least 2 PNGs to anchor visually — spacing, font sizing, color use, layout proportions.
3. **Vary at least one structural element** vs. the most recent post in the same type (different cover sub-layout, different visual element, different headline emphasis pattern). Feed coherence requires deliberate variety — never produce two visually-rhyming consecutive posts.

---

## 6. What is NOT in this spec (and why)

- **Logos** — live in `Logos/`. Brand third-party logos and the Alta Studio logo (light + white variants for dark mode) are not duplicated here.
- **Real-person photos** — live in `Assets/Personas/`. Always prefer real photos to Higgsfield-generated person photos when available.
- **render.sh internals** — see the script comments. It auto-handles the viewport bug and Git Bash → Windows path conversion.
- **Spanish dialect rules** — Colombian Spanish, `tú` form. Full conversion table lives in `PostTypes/step-by-step/Skills/instagram-post-design.md` (referenced from CLAUDE.md §3.2). Not duplicated here.
- **Per-type workflows** (when to ask the user what, how to research news, etc.) — live in each `PostTypes/<type>/README.md`. This file only defines *visual* truth, not procedural truth.
