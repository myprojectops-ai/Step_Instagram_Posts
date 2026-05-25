---
name: news-post-design
description: Visual system for AI news Instagram posts -- 4-slide carousel (cover / body text+photo / stat card / verdict). Higgsfield photo per slide that needs one; HTML overlay for everything else. Editorial dark or light mode per user choice; AMARILLO/ROJO/AZUL highlight scheme. Replaces the deprecated 5-slide / Codex / Inter system.
type: skill
---

# News Post Design (brand v2)

> **Project root:** `c:/Trabajo_AI/Visual_posts/`. The autoloaded [CLAUDE.md](../../../CLAUDE.md) is the master router. The news workflow lives in [../README.md](../README.md). The **brand visual system lives in [Brand/brand-spec.md](../../../Brand/brand-spec.md)** -- this skill builds on top of it.

This skill defines the visual language for **AI news posts**: a **4-slide Instagram carousel** with editorial photography (Higgsfield-generated), Roboto + Playfair Italic typography, and the scheme/mode the user chose at the start of the post. The previous 5-slide / Codex / Inter system is deprecated.

**Workflow (updated 2026-05-23):** Each news slide is a **single Higgsfield generation** with all text + visuals + layout baked into the prompt. **No logo, no handle, no Alta Studio mark anywhere.** The top-left corner is intentionally left empty -- editorial magazine look. After generation, the only post-processing is a PIL resize from the model's native 1856×2304 output down to 1080×1350. No HTML overlay, no CSS, no render.sh, no PIL paste. Validated end-to-end on the Opus 4.7 test carousel (2026-05-23).

**Always open at least 2 reference templates from `Brand/Templates/Noticias/{COLOR}/{MODE}/` before designing slides.**

---

## 1. Slide library + recipe-driven structure (added 2026-05-25)

> **Why this changed:** the old "always cover/body/stat/verdict" produced visually-rhyming posts. User feedback 2026-05-25: *"no siempre tienen que ser esos 3 slides después del cover los mismos. Puedes poner tweets relevantes, jugar con el orden, a veces 5 slides en vez de 4, cambiar visualmente los slides de información."* New system: 7 slide types in a library, 4 recipes that pick from it, and 2-3 visual variants per info slide. The cover is fixed (slide 1, always); everything after rotates. See `[[feedback-news-slide-recipes-variety]]`.

### 1.1 The slide library (7 types)

| Type | Purpose | Default visual core |
|---|---|---|
| **Cover** | Hook (ALWAYS slide 1) | Full-bleed photo + subject company logo + headline (Playfair Italic emphasis) + subtitle |
| **Body text** | What happened — key facts with stats inline | Text + stats inline, paired with concept photo (see variants in §1.4) |
| **Stat card** | Punchline — killer number(s) on a card | Huge Roboto Black number + Playfair Italic unit (see variants in §1.4) |
| **Verdict** | Synthesis / closer | Semaphore bullets OR pull-quote OR Q&A (see variants in §1.4) |
| **Tweet card** | Real reaction / official announcement quote | Twitter UI mock with avatar + handle + tweet text. Mandatory: follow §8 tweet ethics (never fabricate quotes from real people) |
| **Quote pull** | Editorial typographic quote (no Twitter UI) | Big italic Playfair quote, attribution line below, source eyebrow above. For pulled lines from CEOs / journalists / fuente |
| **Comparison split** | Before/after, X vs Y, two-column contrast | Two stacked or side-by-side cards with same structure (label + value/photo) — one in highlight color, one in neutral |

### 1.2 The 4 recipes (pick ONE per news post, rotate vs the last 2 posts)

| Recipe | Slides | When |
|---|---|---|
| **A — Standard** | Cover → Body → Stat → Verdict | Factual news with a strong number. The default if nothing else fits. |
| **B — Reaction** | Cover → Body → **Tweet/Quote** → Stat → Verdict (5) | When there's a public voice that matters (CEO statement, official tweet, expert reaction) |
| **C — Comparison** | Cover → Body → **Comparison** → Verdict | Strategy pivots, before/after, X vs competition (e.g. Allbirds pivot, model vs model) |
| **D — Photo essay** | Cover → Body → **Quote Pull** → Stat → Verdict (5) | More narrative/human news. The quote pull adds editorial weight between data points. |

**Rotation rule:** check the last 2 dated folders in `PostTypes/news/Outputs/`. Don't repeat the same recipe two posts in a row, and try not to repeat 3 in a row. If you're forced to (because nothing else fits), document the reason in the outline message.

**Length limits:** never fewer than 3 slides (feels thin), never more than 6 (loses punch). 4 is the sweet spot; 5 is fine when a tweet/quote earns its place.

### 1.3 Outline workflow change

When proposing the outline (per [README.md](../README.md) step 6), I now propose:
1. **Recipe + reason** ("Receta B porque hay un tweet real de Zeb Evans que da voz a la noticia")
2. **Per-slide breakdown** (slide-by-slide content angle, same as before)
3. **Visual variant per info slide** ("body variante (b) split porque la foto es vertical")
4. **Wait for user approval before generating.**

Variant choices and recipe pick are part of the same outline message — don't ask separately.

### 1.4 Visual variants per info slide type

So that body/stat/verdict don't look identical between posts, each has 2-3 documented layout variants. Pick a different variant than the most recent post used. Variants live in their respective slide sections below:

- **Body slide:** (a) text-top + photo-bottom · (b) photo-left + text-right · (c) full-bleed photo + text overlaid on gradient — see §4
- **Stat card:** (a) one huge number · (b) dashboard 2–3 numbers in a row · (c) stat + sparkline/icon — see §5
- **Verdict:** (a) 3 semaphore bullets · (b) pull-quote synthesis · (c) Q&A "Y entonces?" — see §6

---

## 2. Brand fundamentals (delegated to brand-spec.md)

All palette, typography, and slide-pattern rules live in [Brand/brand-spec.md](../../../Brand/brand-spec.md). News-specific notes:

- **Mode (LIGHT or DARK):** asked at session start. DARK mode is the default editorial look for news (matches the Bridgemind-style references and the `#11191b` warm-dark backgrounds in templates). LIGHT mode (cream) is supported -- the cover is photo + cream gradient instead of photo + dark gradient.
- **Color scheme (AMARILLO/ROJO/AZUL):** asked at session start. Drives highlight color in headlines + accents.
- **Fonts:** Roboto for body/headlines, Playfair Display Italic for 1-3 emphasis words per headline.
- **No `@lucianomusellaa` on news.** News uses the Alta Studio logo in one top corner instead. See CLAUDE.md §3.1.
- **No page dots.** IG handles carousel pagination natively.

---

---

> **Sections 3-6 below describe the LAYOUT and COPY of each slide.** They reference HTML scaffolds from the previous "Higgsfield photo + HTML overlay" approach -- **those scaffolds are LEGACY and should NOT be used.** The current production workflow is in §9: single Higgsfield generation per slide, no HTML, no PIL overlay, no logo. The layout descriptions are still useful as input material for the Higgsfield prompt -- translate the visual structure into prose for the prompt.

---

## 3. Slide 1 -- Cover

### Layout (full-bleed Higgsfield photo + CSS gradient overlay)

```
┌─ 1080 × 1350 ────────────────────────────────────────┐
│                                                       │ ← full-bleed photo (Higgsfield)
│                                                       │   takes ~58% of canvas
│                                                       │
│                                                       │   TOP-LEFT MUST BE EMPTY (no
│                  Higgsfield PHOTO (4:5)               │   Alta Studio, no @handle)
│                                                       │
│                  subject in upper 58%                 │   gradient overlay: photo top →
│                                                       │   transparent middle → dark/cream
│                                                       │   at bottom transition
│ ════════════════════════════════════════════════════  │ ← gradient/dark zone begins
│              ▲                                         │ ← subject company logo (centered,
│         [ClickUp logo]                                 │   ~280px wide, real brand colors)
│              ─────────────                             │ ← thin divider line (~60% width)
│ CLICKUP DESPIDIÓ                                       │ ← Roboto Black ALL CAPS, white
│ AL 22% — Y LOS                                         │
│ REEMPLAZÓ POR                                          │
│ ╱3.000 AGENTES╲ DE IA                                  │ ← Playfair Italic + scheme highlight
│                                                        │
│ EL FUTURO DEL TRABAJO LLEGÓ ANTES DE LO ESPERADO      │ ← subtitle, gray small caps
│                                                        │
└────────────────────────────────────────────────────────┘
```

**The "X" diagonal cross visible in template PNGs is a placeholder marker only** -- never render it in the final output. The Higgsfield photo replaces that zone entirely.

### Cover rules

- **Photo:** 4:5 Higgsfield generation. Subject in upper ~58% (will be visible). Bottom ~42% will be darkened by gradient for the logo + headline + subtitle stack.
- **Gradient overlay (DARK mode):** `linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0.88) 8%, rgba(0,0,0,0.72) 22%, rgba(0,0,0,0.35) 42%, transparent 62%)`
- **Gradient overlay (LIGHT mode):** invert with cream tones, `linear-gradient(to top, rgba(239,237,236,0.95) 0%, rgba(239,237,236,0.85) 10%, rgba(239,237,236,0.4) 30%, transparent 55%)`
- **Subject company logo (MANDATORY, added 2026-05-25):** every news cover MUST include the subject company's logo (the company the news is about — e.g. ClickUp, OpenAI, Anthropic) rendered inside the Higgsfield prompt. Placement: centered horizontally in the dark gradient zone, top of the typography stack, just above a thin divider line. Size ~280px wide × 60–80px tall. Use the company's actual brand colors (wordmark + icon if it has one). The model won't be pixel-perfect — that's fine; brand recognition + visual hook is the goal. The image caption ("IMAGEN — descriptor") is REPLACED by this logo on covers. See `[[feedback-news-cover-company-logo]]`.
- **Divider line:** 1px warm-gray (`#3a4044`), ~60% width, centered, sits between the logo and the headline with small vertical breathing room.
- **Headline:** Roboto Black 64–84px, ALL CAPS, 3–4 lines. 1–3 keywords rendered in Playfair Display Italic in the scheme highlight color. Left-aligned with 60px left padding.
- **Subtitle:** 17–19px Roboto Medium, ALL CAPS, letter-spacing 0.08em, color `rgba(255,255,255,0.55)` (DARK) or `rgba(12,19,20,0.55)` (LIGHT). Centered near the bottom edge.
- **No Alta Studio logo, no `@lucianomusellaa` handle.** The top-left corner is intentionally empty (editorial magazine look). The Higgsfield prompt must include the mandatory line "The top-left corner MUST BE COMPLETELY EMPTY. No logo, no symbol, no mark, no triangle." The ONLY logo on the cover is the centered subject-company logo in the dark zone.
- **Body / stat / verdict slides (2, 3, 4) do NOT carry the company logo.** Logo is cover-only.
- **No SWIPE pill on the cover** — the templates don't use one; IG's swipe affordance is enough.

### Higgsfield prompt structure (cover photo)

```
Editorial cinematic photograph, vertical portrait composition, 4:5 aspect ratio.
[SCENE/SUBJECT description — position subject in the UPPER portion of the frame, leave lower 40% as open/dark space for text overlay].
Dramatic lighting, subtle film grain, slightly desaturated editorial tones.
Magazine-quality vertical framing.
No text, no typography, no logos, no words, no watermarks.
--ar 4:5 --seed [STABLE-SEED-FOR-THIS-CAROUSEL]
```

**Prompt rules:**
- Always end with "No text, no typography, no logos" -- Soul will add text otherwise
- Position the subject in the upper portion (above y=540) so the gradient zone covers expendable detail
- Match the emotional temperature of the news (warm/inviting for positive news, cold/dramatic for controversy)
- Include "film grain" or "editorial photography" to avoid the plastic AI look
- For real public figures: describe by role/features, not by name (e.g. "a tech CEO in his 50s with grey hair in a Senate hearing"). Soul handles named figures better than gpt-image-1 did, but content policy still applies.

Generate ONE cover photo. Present to user. Only regenerate if rejected.

### Cover HTML scaffold (DARK + AMARILLO -- adapt tokens per mode/scheme)

Save as `slide1_cover.html` in the post's output folder. The Higgsfield-generated `cover_photo.png` must be in the same folder.

```html
<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8">
<style>
  /* @font-face block -- canonical, see Brand/brand-spec.md §2 */
  @font-face { font-family: 'Roboto'; src: url('../../../../Brand/Fonts/Roboto/static/Roboto-Bold.ttf')  format('truetype'); font-weight: 700; font-style: normal; font-display: block; }
  @font-face { font-family: 'Roboto'; src: url('../../../../Brand/Fonts/Roboto/static/Roboto-Black.ttf') format('truetype'); font-weight: 900; font-style: normal; font-display: block; }
  @font-face { font-family: 'Roboto'; src: url('../../../../Brand/Fonts/Roboto/static/Roboto-Medium.ttf') format('truetype'); font-weight: 500; font-style: normal; font-display: block; }
  @font-face { font-family: 'Playfair Display'; src: url('../../../../Brand/Fonts/PlayfairDisplay/static/PlayfairDisplay-Italic.ttf') format('truetype'); font-weight: 400; font-style: italic; font-display: block; }

  * { margin:0; padding:0; box-sizing:border-box; }
  body { width:1080px; height:1350px; font-family:'Roboto', sans-serif; overflow:hidden; position:relative; background:#11191b; }
  .photo { position:absolute; inset:0; background-image:url('cover_photo.png'); background-size:cover; background-position:center center; }
  .gradient {
    position:absolute; inset:0; z-index:2;
    background: linear-gradient(to top, rgba(17,25,27,0.96) 0%, rgba(17,25,27,0.88) 10%, rgba(17,25,27,0.65) 28%, rgba(17,25,27,0.25) 50%, transparent 65%);
  }
  .alta { position:absolute; top:44px; left:50px; height:100px; opacity:.98; z-index:10; filter: drop-shadow(0 2px 14px rgba(0,0,0,.55)); }
  .image-caption {
    position:absolute; top:740px; left:60px; right:60px; z-index:10;
    color: rgba(255,255,255,0.6); font-size:16px; font-weight:500;
    text-transform:uppercase; letter-spacing:0.08em; text-align:center;
  }
  .headline {
    position:absolute; top:820px; left:60px; right:60px; z-index:10;
    font-size:64px; font-weight:900; line-height:1.05; color:#ffffff;
    letter-spacing:-0.012em; text-transform:uppercase;
  }
  .emphasis { font-family:'Playfair Display'; font-style:italic; font-weight:400; color:#ffb050; text-transform:none; }
  .subtitle {
    position:absolute; top:1270px; left:60px; right:60px; z-index:10;
    color: rgba(255,255,255,0.55); font-size:18px; font-weight:500;
    text-transform:uppercase; letter-spacing:0.08em; text-align:center;
  }
</style></head>
<body>
  <div class="photo"></div>
  <div class="gradient"></div>
  <img class="alta" src="../../../../Logos/Alta_Studio_logo_white.png">
  <div class="image-caption">IMAGEN — hardware / servidor</div>
  <div class="headline">
    ANTHROPIC LANZÓ<br>
    <span class="emphasis">OPUS</span> 4.7: MÁS CÓDIGO,<br>
    MENOS <span class="emphasis">MEMORIA</span><br>
    — ¿VALE EL <span class="emphasis">PRECIO</span>?
  </div>
  <div class="subtitle">EL MODELO QUE PROMETÍA MÁS Y LLEGÓ CON SORPRESAS</div>
</body></html>
```

### Adapting to other modes/schemes

- **LIGHT mode:** body bg `#efedec`, gradient flips to cream tones, headline color `#0c1314`, Alta Studio logo uses `Alta_Studio_logo.png` (dark variant). Image caption + subtitle use `rgba(12,19,20,0.55)`.
- **ROJO scheme:** `.emphasis { color: #e60000; }`
- **AZUL scheme:** `.emphasis { color: #0056a6; }`

---

## 4. Slide 2 -- Body text + photo

### Layout

```
┌─ 1080 × 1350 ────────────────────────────────────────┐
│                                                       │
│  LA CONTROVERSIA                                      │ ← eyebrow scheme highlight color
│                                                       │
│  La memoria cayó de ╱78.3%╲ a solo ╱32.2%╲           │ ← Roboto Medium, stats inline highlight
│  en el test MRCR v2.                                  │
│                                                       │
│  Anthropic retiró el test: dice que no                │
│  mide la memoria como los humanos la usan.            │
│                                                       │
│  Y usa hasta ╱35% más tokens╲ en modo thinking        │
│  puede costar ╱35% más╲ por tarea.                    │
│                                                       │
│ ─────────────────────────────────────────────────     │ ← visual divider
│                                                       │
│                                                       │
│           IMAGEN — vidrio roto / circuito             │ ← Higgsfield photo zone (16:9)
│                                                       │
└───────────────────────────────────────────────────────┘
```

- **Eyebrow:** scheme highlight color, ALL CAPS, letter-spacing 2px, Roboto Medium 16-18px
- **Body text:** Roboto Medium 28-32px, line-height 1.45. Stats/percentages wrapped in `<span class="emphasis">` (Playfair Italic + scheme highlight color)
- **Photo zone (16:9):** Higgsfield `--ar 16:9` → 1080×608. Subject is concept-reinforcing (not portrait). Sits at the bottom of the canvas.
- **Image caption:** small caps over the dark/black zone above the photo, centered

### Body visual variants (pick one — vary vs the last post)

- **(a) Text-top + photo-bottom** (default, shown in the diagram above). Use when the photo is horizontal and the text needs ~55% of canvas.
- **(b) Photo-left + text-right** (or right + left). Splits the canvas vertically ~50/50. Use when the photo is vertical (portrait of a CEO, building) or when you want the text to feel more focused/quoted.
- **(c) Full-bleed photo + text overlaid on gradient** (cover-style for the body). Use when the photo is hero-grade (dramatic editorial shot) and the text is short — eyebrow + 2–3 short paragraphs max. Subtle dark gradient bottom-up so text stays legible.

Translate the chosen variant into the Higgsfield prompt as a layout description ("UPPER 60% photo, LOWER 40% text" / "LEFT 50% photo, RIGHT 50% text" / "Full-bleed photo, text overlaid with gradient at bottom").

### Body slide HTML scaffold (DARK + AMARILLO)

```html
<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8">
<style>
  /* Reuse @font-face block from cover scaffold */
  * { margin:0; padding:0; box-sizing:border-box; }
  body { width:1080px; height:1350px; font-family:'Roboto', sans-serif; background:#efedec; color:#0c1314; }
  .top-zone { padding: 100px 70px 50px; }
  .eyebrow { color:#ffb050; font-size:18px; font-weight:500; text-transform:uppercase; letter-spacing:2px; margin-bottom:30px; }
  .body-text { font-size:30px; font-weight:500; line-height:1.5; }
  .body-text p { margin-bottom:24px; }
  .emphasis { font-family:'Playfair Display'; font-style:italic; font-weight:400; color:#ffb050; }
  .bottom-zone {
    position:absolute; bottom:0; left:0; right:0; height:540px;
    background:#11191b; display:flex; align-items:flex-start; justify-content:center; padding-top:30px;
  }
  .image-caption {
    color: rgba(255,255,255,0.55); font-size:15px; font-weight:500;
    text-transform:uppercase; letter-spacing:0.08em;
  }
  .photo {
    position:absolute; bottom:0; left:0; right:0; height:480px;
    background-image:url('slide2_photo.png'); background-size:cover; background-position:center;
  }
</style></head>
<body>
  <div class="top-zone">
    <div class="eyebrow">LA CONTROVERSIA</div>
    <div class="body-text">
      <p>La memoria cayó de <span class="emphasis">78.3%</span> a solo <span class="emphasis">32.2%</span> en el test MRCR v2.</p>
      <p>Anthropic retiró el test: dice que no mide la memoria como los humanos la usan.</p>
      <p>Y usa hasta <span class="emphasis">35% más tokens</span> en modo thinking — puede costar <span class="emphasis">35% más</span> por tarea.</p>
    </div>
  </div>
  <div class="bottom-zone"><div class="image-caption">IMAGEN — vidrio roto / circuito</div></div>
  <div class="photo"></div>
</body></html>
```

The Higgsfield photo (16:9, generic concept-reinforcing imagery) is generated separately and saved as `slide2_photo.png`. Photo prompts: "concept-reinforcing horizontal editorial photograph at 16:9, [scene description], cinematic, film grain, no text, no logos".

---

## 5. Slide 3 -- Stat card

### Layout

```
┌─ 1080 × 1350 ────────────────────────────────────────┐
│  ┌─────────────────────────────────────────────┐      │
│  │                                              │     │
│  │  CODING BENCHMARK                           │      │ ← eyebrow scheme highlight color
│  │                                              │     │
│  │     64.3%                                   │      │ ← huge Roboto Black, % in Playfair Italic
│  │                                              │     │
│  │  SWE-BENCH VERIFIED PRO                     │      │ ← small caps caption
│  │  El test más difícil de contaminar. Opus 4.7│      │ ← body, with brand names in italic
│  │  supera a GPT-4.5 Codex (57.7%)             │      │
│  │                                              │     │
│  │  ┌──────┐  ┌──────┐  ┌──────┐               │     │ ← comparison cards
│  │  │57.7% │  │~63%  │  │64.3% │               │     │
│  │  └──────┘  └──────┘  └──────┘               │     │
│  │                                              │     │
│  │  Fuente: SWE-bench Verified Pro             │      │ ← source line, small grey
│  └─────────────────────────────────────────────┘      │
└───────────────────────────────────────────────────────┘
```

- **Background:** mode background (cream in LIGHT, dark in DARK)
- **Card:** white in LIGHT mode (`#ffffff`) with subtle shadow, OR `#e6ecee` very-light-gray card in DARK mode. Border-radius 28px, padding 60px 56px.
- **Number:** Roboto Black 240-280px, letter-spacing -8px
- **% sign:** Playfair Italic in scheme highlight color
- **Comparison cards:** 3 small white/gray boxes in a row, each with a comparison value. Roboto Bold inside. The leading value (the slide's "winner") is also in Playfair Italic highlight color.
- **Source line:** 16px Roboto Medium, text-subtle color

### Stat card visual variants (pick one — vary vs the last post)

- **(a) One huge number** (default, shown above). Use when there's ONE killer stat that carries the slide. Body paragraph + optional 3 comparison cards underneath.
- **(b) Dashboard 2–3 numbers in a row** — split the card top zone into 2 or 3 equal columns, each with its own caption + huge Roboto Black number + unit in Playfair Italic. Use when the news has multiple parallel stats that gain meaning side-by-side (e.g. revenue / users / valuation). Body paragraph stays underneath.
- **(c) Stat + sparkline / icon** — one huge number on the left/top, a stylized simple chart (sparkline, bar, donut) or symbolic icon on the right/bottom in the highlight color. Use when the trend or shape of the number matters (growth curve, market share slice). The "chart" is described into the Higgsfield prompt as geometric shapes — keep it abstract, not data-accurate.

### Stat card HTML scaffold (LIGHT + AMARILLO)

```html
<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8">
<style>
  /* @font-face block omitted -- reuse from cover */
  * { margin:0; padding:0; box-sizing:border-box; }
  body { width:1080px; height:1350px; font-family:'Roboto', sans-serif; background:#efedec; color:#0c1314; padding:60px 60px; }
  .card { background:#ffffff; border-radius:28px; padding:60px 56px; box-shadow:0 8px 32px rgba(0,0,0,0.04); height:100%; display:flex; flex-direction:column; }
  .eyebrow { color:#ffb050; font-size:18px; font-weight:500; text-transform:uppercase; letter-spacing:2px; margin-bottom:40px; }
  .stat { font-size:260px; font-weight:900; line-height:0.95; letter-spacing:-8px; margin-bottom:30px; }
  .pct { font-family:'Playfair Display'; font-style:italic; font-weight:400; color:#ffb050; letter-spacing:0; }
  .caption { color:#ffb050; font-size:18px; font-weight:500; text-transform:uppercase; letter-spacing:2px; margin-bottom:12px; }
  .body { font-size:24px; font-weight:500; line-height:1.45; margin-bottom:50px; }
  .body .em-tool { font-family:'Playfair Display'; font-style:italic; font-weight:400; color:#ffb050; }
  .comparison { display:grid; grid-template-columns:repeat(3, 1fr); gap:16px; margin-top:auto; }
  .comp-card { background:#f5f3f1; border-radius:14px; padding:22px 18px; text-align:center; }
  .comp-label { font-size:12px; font-weight:500; color:#6b6860; text-transform:uppercase; letter-spacing:1.2px; margin-bottom:8px; }
  .comp-value { font-size:44px; font-weight:900; line-height:1; }
  .comp-card.winner .comp-value { font-family:'Playfair Display'; font-style:italic; font-weight:400; color:#ffb050; }
  .source { font-size:14px; font-weight:500; color:#6b6860; margin-top:24px; }
</style></head>
<body>
  <div class="card">
    <div class="eyebrow">CODING BENCHMARK</div>
    <div class="stat">64.3<span class="pct">%</span></div>
    <div class="caption">SWE-BENCH VERIFIED PRO</div>
    <div class="body">
      El test más difícil de contaminar. Opus 4.7 supera a <span class="em-tool">GPT-4.5 Codex</span> (57.7%).
    </div>
    <div class="comparison">
      <div class="comp-card"><div class="comp-label">GPT-4.5 Codex</div><div class="comp-value">57.7%</div></div>
      <div class="comp-card"><div class="comp-label">Gemini 3.1 Pro</div><div class="comp-value">~63%</div></div>
      <div class="comp-card winner"><div class="comp-label">Opus 4.7</div><div class="comp-value">64.3%</div></div>
    </div>
    <div class="source">Fuente: SWE-bench Verified Pro · Anthropic, abr. 2026</div>
  </div>
</body></html>
```

---

## 6. Slide 4 -- Verdict (closer)

### Layout

```
┌─ 1080 × 1350 ────────────────────────────────────────┐
│  ┌─────────────────────────────────────────────┐      │
│  │  EL VEREDICTO                               │     │ ← eyebrow scheme highlight color
│  │                                              │     │
│  │  4.7 se siente como un                      │     │
│  │  ╱4.6.1╲ con ╱training data╲                │     │ ← italic emphasis on key terms
│  │  nuevo.                                      │     │
│  │  ───────────                                │     │ ← thin divider
│  │  ● Mejor en código                          │     │ ← GREEN dot (positive)
│  │    (64.3% SWE-bench Pro) y comprensión …    │     │
│  │  ● Memoria deteriorada                      │     │ ← RED dot (negative)
│  │    (78.3% 32.2% en MRCR v2)                 │     │
│  │  ● Puede costar hasta 30–150% más           │     │ ← ORANGE dot (caution)
│  │    por tarea en producción                  │     │
│  └─────────────────────────────────────────────┘      │
└───────────────────────────────────────────────────────┘
```

- **Eyebrow:** "EL VEREDICTO" / "EN RESUMEN" / "CONCLUSIÓN" -- scheme highlight color
- **Headline:** Roboto Bold 44-54px, 2-3 lines. 1-2 key terms in Playfair Italic scheme highlight color.
- **Bullet dots:** semaphore semantics regardless of scheme:
  - 🟢 GREEN `#22c55e` -- positive finding
  - 🟠 ORANGE `#ffb050` -- neutral / caution / cost
  - 🔴 RED `#e60000` -- negative finding
- **Bullets:** Roboto Bold 26-30px for the headline of each bullet, italic gray 18-22px for the parenthetical detail below

### Verdict visual variants (pick one — vary vs the last post)

- **(a) 3 semaphore bullets** (default, shown above). Synthesis as positive/neutral/negative findings with dot colors. Use when there's a clear pro/con read.
- **(b) Pull-quote synthesis** — drop the bullets, render the verdict as ONE big italic Playfair Display quote (50–60px) centered or left-aligned in the card, with a small attribution / source line below ("— @lucianomusellaa" or "Lectura editorial"). Use when one synthesized sentence says everything.
- **(c) Q&A format** — two paragraphs: "**¿Y entonces?**" header in highlight color + answer paragraph in white/text-primary; optionally a second "**¿Qué viene ahora?**" + answer below. Use when the news has a clear question-the-reader-is-asking and you want to land the answer cleanly.

### Verdict HTML scaffold (LIGHT + AMARILLO)

```html
<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8">
<style>
  /* @font-face block omitted -- reuse from cover */
  * { margin:0; padding:0; box-sizing:border-box; }
  body { width:1080px; height:1350px; font-family:'Roboto', sans-serif; background:#efedec; color:#0c1314; padding:60px 60px; }
  .card { background:#ffffff; border-radius:28px; padding:80px 70px; height:100%; display:flex; flex-direction:column; box-shadow:0 8px 32px rgba(0,0,0,0.04); }
  .eyebrow { color:#ffb050; font-size:18px; font-weight:500; text-transform:uppercase; letter-spacing:2px; margin-bottom:32px; }
  .headline { font-size:50px; font-weight:700; line-height:1.18; margin-bottom:40px; }
  .emphasis { font-family:'Playfair Display'; font-style:italic; font-weight:400; color:#ffb050; }
  .divider { width:80%; height:1px; background:#e4dfde; margin-bottom:34px; }
  .bullet { display:flex; align-items:flex-start; gap:18px; margin-bottom:30px; }
  .dot { width:14px; height:14px; border-radius:50%; flex-shrink:0; margin-top:10px; }
  .dot.pos { background:#22c55e; }
  .dot.cau { background:#ffb050; }
  .dot.neg { background:#e60000; }
  .bullet-body { flex:1; }
  .bullet-title { font-size:28px; font-weight:700; line-height:1.25; margin-bottom:6px; }
  .bullet-detail { font-size:20px; font-weight:400; color:#6b6860; font-style:italic; line-height:1.4; }
</style></head>
<body>
  <div class="card">
    <div class="eyebrow">EL VEREDICTO</div>
    <div class="headline">4.7 se siente como un <span class="emphasis">4.6.1</span> con <span class="emphasis">training data</span> nuevo.</div>
    <div class="divider"></div>
    <div class="bullet">
      <div class="dot pos"></div>
      <div class="bullet-body">
        <div class="bullet-title">Mejor en código</div>
        <div class="bullet-detail">(64.3% SWE-bench Pro) y comprensión visual</div>
      </div>
    </div>
    <div class="bullet">
      <div class="dot neg"></div>
      <div class="bullet-body">
        <div class="bullet-title">Memoria deteriorada</div>
        <div class="bullet-detail">(78.3% → 32.2% en MRCR v2)</div>
      </div>
    </div>
    <div class="bullet">
      <div class="dot cau"></div>
      <div class="bullet-body">
        <div class="bullet-title">Puede costar hasta 30-150% más</div>
        <div class="bullet-detail">por tarea en producción</div>
      </div>
    </div>
  </div>
</body></html>
```

---

## 6.5 Slide type -- Tweet card (Recipe B)

**When:** the news has a public statement worth showing in its original voice — an official company tweet, a CEO quote, a journalist's hot take. Insert between Body and Stat (or replace Stat in shorter recipes).

**Mandatory:** follow §8 tweet ethics. Never fabricate a quote attributed to a real person. Official tweets must be reproduced verbatim from a real source; commentary tweets from invented personas are OK if clearly fictional.

### Layout

```
┌─ 1080 × 1350 ────────────────────────────────────────┐
│                                                       │
│  LA REACCIÓN                                          │ ← eyebrow scheme highlight color
│                                                       │
│                                                       │
│  ┌─────────────────────────────────────────────┐     │
│  │ ◯  Zeb Evans ✓                              │     │ ← avatar circle + name + verified
│  │    @zebevans                                │     │ ← handle, muted gray
│  │                                             │     │
│  │ "Most savings from this change will        │     │ ← tweet text, Roboto 28-32px
│  │  flow directly back into the people        │     │   1-3 short paragraphs
│  │  who stay. Million-dollar salary bands."   │     │
│  │                                             │     │
│  │  ───────────────                            │     │ ← divider
│  │ 3:42 PM · 22 may 2026 · CEO ClickUp         │     │ ← timestamp + source, small grey
│  └─────────────────────────────────────────────┘     │
│                                                       │
│  ─────                                                │ ← thin divider
│  LA LECTURA                                           │ ← optional bottom row eyebrow
│  El ahorro no va a la utilidad — va a los que       │ ← editorial 1-line take
│  ╱se quedan╲.                                         │ ← italic emphasis
└───────────────────────────────────────────────────────┘
```

**Card styling:** white card (LIGHT mode) or `#e6ecee` very-light card (DARK mode), border-radius 22px, padding 50px 50px. Tweet body in dark text. Twitter UI affordances are decorative — keep them subtle and editorial-feeling (small avatar circle, verified checkmark if real, handle + timestamp).

**Higgsfield prompt anatomy:**
- Describe the card geometry (rounded white card on dark/cream bg, padding, drop shadow)
- Avatar: "small circular avatar at top-left of card, [describe person or a generic editorial portrait at 50px diameter]"
- Name + verified mark + handle (real if public account, invented if commentary persona)
- Tweet body text rendered in Roboto Medium black/dark, exactly as the prompt provides — no rephrasing
- Timestamp + source line, muted gray
- Optional bottom "LA LECTURA" row with editorial take below the card

**Source verification:** if quoting a real public tweet, WebSearch the actual URL/handle and reproduce verbatim. If unverifiable, use Quote Pull (§6.6) instead — no Twitter UI = no false-attribution risk.

---

## 6.6 Slide type -- Quote pull (Recipe D, or anywhere)

**When:** a single line from the news, the CEO, or the journalist deserves editorial weight without the Twitter UI baggage. Pure typographic moment.

### Layout

```
┌─ 1080 × 1350 ────────────────────────────────────────┐
│                                                       │
│  LA FRASE                                             │ ← eyebrow scheme highlight color
│                                                       │
│                                                       │
│        "The people that                               │
│         ╱automate their jobs╲                         │ ← Playfair Display Italic
│         with AI will always                           │   60-80px, italic, dark/light text
│         have a job."                                  │   highlight in scheme color
│                                                       │
│         ─────                                         │ ← small horizontal divider
│         Zeb Evans                                     │ ← attribution name, Roboto Bold 22px
│         CEO de ClickUp                                │ ← role, Roboto Regular 18px gray
│                                                       │
└───────────────────────────────────────────────────────┘
```

**Styling:**
- Background: mode background (dark `#11191b` or cream `#efedec`), NO card. Pure canvas.
- Quote: Playfair Display Italic 60-80px, line-height 1.18, centered or left-aligned with 80-100px padding. 2-4 lines max. Open with `"` (curly typographic quote).
- 1-3 keywords inside the quote in scheme highlight color (still Playfair Italic).
- Attribution block below the quote, separated by a thin divider line.
- Optional: a small symbolic icon (quotation mark, abstract geometric shape) in the highlight color as visual anchor — not mandatory.

**Higgsfield prompt anatomy:**
- Describe the canvas as "mostly empty editorial canvas, [mode] background"
- The quote text rendered in Playfair Display Italic SERIF font with the keyword tokens in scheme highlight color
- Attribution name + role below
- No card, no Twitter UI, no avatar — just typography
- TOP-LEFT MUST BE EMPTY mandatory line

**Ethics:** the quote must come from a real verifiable source (article, official statement). Cite the source in the attribution. Same rules as tweet cards (see §8).

---

## 6.7 Slide type -- Comparison split (Recipe C)

**When:** the news has a strong before/after, X vs Y, or strategy pivot. Two parallel realities benefit from side-by-side framing.

### Layout

```
┌─ 1080 × 1350 ────────────────────────────────────────┐
│                                                       │
│  EL CAMBIO                                            │ ← eyebrow scheme highlight color
│                                                       │
│  ┌────────────────┐  ┌────────────────┐              │
│  │  ANTES         │  │  AHORA         │              │ ← left/right labels, small caps
│  │                │  │                │              │
│  │   78%          │  │   ╱32%╲        │              │ ← big numbers; right side in highlight italic
│  │   memoria      │  │   memoria      │              │ ← descriptor
│  │                │  │                │              │
│  │   IMAGEN /     │  │   IMAGEN /     │              │ ← small concept photo per side
│  │   icono        │  │   icono        │              │   (optional)
│  └────────────────┘  └────────────────┘              │
│                                                       │
│  ─────                                                │
│  La memoria cayó ╱46 puntos╲ entre v1 y v2.          │ ← synthesis line below, italic emphasis
└───────────────────────────────────────────────────────┘
```

**Styling:**
- Two equal cards side-by-side (split 50/50 with ~20px gap). Each card has the mode-card background (white in LIGHT, very-light gray in DARK).
- Same internal structure on both sides: small caps label at top + big number/image in the middle + descriptor + optional small concept photo or icon.
- Visual asymmetry: the "after" / "new" / "winner" card gets the highlight color treatment (Playfair Italic number, accent border, or filled background); the "before" card stays neutral (gray).
- Below the cards: synthesis line in Roboto Medium with 1-2 Playfair Italic emphasis tokens.

**Alternative: vertical comparison (stacked top/bottom).** Same idea but cards stack vertically (one half / one half). Use when the "before" and "after" each have a horizontal photo that needs width.

**Higgsfield prompt anatomy:**
- Describe the canvas as two cards side-by-side (or stacked) with explicit padding/gap
- Each card's exact text and number, with the right side getting Playfair Italic + scheme highlight
- Optional concept icons described as simple geometric shapes (not photo)
- Synthesis line below with explicit italic tokens
- TOP-LEFT MUST BE EMPTY mandatory line

---

## 7. Headline writing rules

### Language
- **Colombian Spanish, `tú` form.** No voseo.
- Brand names stay in English: "Anthropic", "Perplexity", "Claude", "OpenAI"
- Numbers: prefer digits ("40%", "US$2.000M", "5 años")

### Cover headline
| Rule | Detail |
|---|---|
| Word count | 6-12 words (tight, news-style) |
| Case | ALL CAPS |
| Font weight | Roboto Black 900 |
| Lines | 3-4 |
| Emphasis | 1-3 words in Playfair Italic scheme highlight color |
| Tone | Factual, newsworthy. **Not clickbait.** No exclamation marks, no "¡INCREÍBLE!" |

### Emphasis word selection
Pick the **most concrete nouns**: tool/product names (Opus, Claude Code, GPT-4.5), strong concept nouns (MEMORIA, PRECIO, BRÚJULA ÉTICA), or impactful adjectives (HISTÓRICO, MASIVO).

### Subtitle (below headline on cover)
- 1 line, ALL CAPS, Roboto Medium 17-19px, scheme-text-subtle color
- Expands the "why this matters"
- Example: "EL MODELO QUE PROMETÍA MÁS Y LLEGÓ CON SORPRESAS"

---

## 8. Tweet ethics (still mandatory if a tweet slide is added)

For news posts that need a tweet slide (insert between body and stat slides, e.g., the official announcement quote):

| Case | What to do |
|---|---|
| **Official company announcement** | WebSearch the actual tweet. Reproduce real text + handle. Cite, never invent. |
| **Public CEO statement** | Paraphrase only from documented public record. Real handle. If unverifiable, do NOT attribute to a real person. |
| **Reaction / commentary** | Invented plausible handle (e.g., `@sofia_reyes_ai`) with Higgsfield-generated avatar. Clearly fictional persona. **Never attribute an invented quote to a real person.** |
| **Editorial quote card** | If no real tweet and no need for fictional commentary, use a typographic quote card instead -- not styled as a Twitter UI. |

Fabricated quotes attributed to real people are misinformation. These rules protect the brand.

---

## 9. Generation pipeline (single-step Higgsfield, no overlays)

> **Logo policy:** the **subject company's logo** (the company the news is about) is included ON THE COVER ONLY, described inside the Higgsfield prompt and rendered baked-in (no HTML overlay). Body / stat / verdict slides have no logo. No Alta Studio mark anywhere, no `@lucianomusellaa` handle.

### Per-slide workflow

Each of the 4 news slides is generated in one Higgsfield call. The only post-processing is a PIL resize from native ~1856×2304 to the canvas target 1080×1350.

```
1. Higgsfield generation (text + visuals + layout, top-left intentionally empty)
   ↓ saves to {slide}_raw.png at native ~1856×2304
2. PIL resize to 1080×1350 LANCZOS, save as {slide}.png, delete _raw
   ↓ this is the deliverable
```

### Step 1 -- Higgsfield generation

Use `mcp__higgsfield__generate_image`:
- **Model:** `nano_banana_pro` (do NOT use `soul_2` for news -- Soul bleeds text and adjusts 4:5 to 3:4)
- **Aspect ratio:** `"4:5"`
- **Resolution:** `"2k"` (gives ~1856×2304 native output)
- **Count:** 1

The prompt must include EVERY text element with explicit styling:
- Headline / title text with exact wording (and "exactly N lines" if multi-line)
- Eyebrow / labels with their color, casing, and letter-spacing
- Body text with stats marked as "rendered in Playfair Display Italic serif #e60000"
- Number stats with exact spelling instructions (e.g. "Verified spelled V-E-R-I-F-I-E-D, eight letters")
- Bullet dots with explicit colors and order ("GREEN circle (#22c55e), then RED (#e60000), then ORANGE (#ffb050), in that order top to bottom")
- Sub-card labels and values
- Subtitle text below the headline
- **COVER ONLY — subject company logo:** describe the company wordmark (spelling, weight, geometric icon if any) + actual brand colors (e.g. ClickUp = pink-magenta `#FF1F8E` → violet `#7B68EE` → cyan `#49CCF9` gradient). Place centered horizontally in the dark gradient zone above a thin divider line and above the headline. Size ~280px wide × 60–80px tall. End the logo description with: "The ONLY logo on the entire canvas is the centered [Company] wordmark in the dark gradient zone."
- **MANDATORY line in EVERY prompt:** "The top-left corner of the canvas MUST BE COMPLETELY EMPTY. No logo, no symbol, no mark, no triangle. Leave that area clean."

Without that mandatory line, the model fills the top-left with an invented "Alta Studio-style" triangular placeholder. With it, the corner stays clean. On the cover, this rule coexists with the centered subject-company logo — the model treats top-left and the dark-zone center as independent regions.

### Step 2 -- Resize to canvas dimensions

```python
from PIL import Image
img = Image.open('slide_raw.png').convert('RGB')
img.resize((1080, 1350), Image.LANCZOS).save('slide.png', quality=95)
# then delete the _raw file
```

### Per-slide prompts (canonical for the Opus 4.7 test)

The full prompts for each of the 4 slides are committed in the test folder `PostTypes/news/Outputs/v2-test-opus-4-7/` as reference. For a new news post, adapt those prompts to the new topic while preserving:
- The "TOP-LEFT MUST BE EMPTY" instruction
- The Playfair Italic emphasis style for keywords/stats
- The mode-appropriate background (`#11191b` DARK, `#efedec` LIGHT)
- The scheme-appropriate highlight color (`#e60000` ROJO, `#ffb050` AMARILLO, `#0056a6` AZUL)
- The semaphore dot colors on verdict slides (green/red/orange)

### Mandatory visual QA before presenting

Since the model renders all text, **read every slide PNG with the Read tool and verify**:
- All Spanish accents preserved
- No word duplications (e.g. "MENOS MENOS MEMORIA" was a real bug)
- No missing letters (e.g. "Verifed" instead of "Verified")
- No styling-instruction leakage into the rendered text (e.g. "Roboto Medium Italic, ALL CAPS: LA APUESTA" was a real bug — fix by separating styling from text labels in the prompt; see slide 2/3 regen notes in the brand v2 ClickUp post)
- All stats numerically correct
- Italic emphasis on the right words
- Semaphore dot colors in the right order
- Top-left corner clean (no invented logo)
- **Cover only:** subject company logo present, centered in dark zone, identifiable, in correct brand colors

If anything is wrong, **regenerate that slide with a more explicit prompt** (e.g. "the word X appears exactly one time" or "X spelled L-E-T-T-E-R-S"). Do not patch via HTML or PIL.

### Prompt anti-patterns
- Don't mention the Alta Studio mark, the `@lucianomusellaa` handle, or any unrelated logo in the prompt (the model will draw one). The subject company logo on the cover is the ONLY exception.
- Don't name real public figures directly (describe by role/features)
- Don't use prompts under 15 words
- Don't trust the model with critical numbers without explicit spelling instructions

---

## 10. Caption (Instagram post caption)

The carousel carries the content. The caption is **brief and utilitarian**:

- 1-3 lines max
- No hashtags (user adds them manually)
- No emojis
- No CTA ("sígueme", "guarda")
- Goal: minimal context for the feed + searchability

Save as `caption.txt` in the post output folder.

### Examples

```
Anthropic lanzó Opus 4.7. Mejora en código pero deteriora memoria — y puede costar hasta 35% más por tarea.
```

```
Sam Altman ha sido atacado en su casa dos veces en una semana.
El costo del liderazgo público en IA.
```

---

## 11. Visual QA + global rules

Every slide must pass [Skills/visual-qa.md](../../../Skills/visual-qa.md). Specific to news:

- [ ] Photo position correct (subject in upper portion of cover)
- [ ] Gradient overlay reads (text legible over photo)
- [ ] Alta Studio logo present, correct variant for mode (white on DARK, normal on LIGHT)
- [ ] No `@lucianomusellaa` handle on any slide
- [ ] No page dots / SWIPE pill (Instagram handles pagination)
- [ ] Headline and subtitle are SEPARATE absolute-positioned elements (not nested)
- [ ] Fonts loaded (Roboto + Playfair Italic, not fallback)
- [ ] Highlight color matches chosen scheme on every emphasis word
- [ ] Colombian Spanish (`tú` form, no voseo)
