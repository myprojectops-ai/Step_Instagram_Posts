---
name: instagram-post-design
description: BASE visual system for all Instagram posts in this project. Defines the shared design language (canvas, colors, fonts, anti-patterns, render pipeline) used by both instagram-cover-design and instagram-step-slide-design. Read this first whenever working on any post — the layout-specific skills extend this foundation.
type: skill
---

# Instagram Post Design — Base System

> **Project root:** `c:/Visual_posts/`. The autoloaded **[`CLAUDE.md`](../../../CLAUDE.md)** at the project root contains the trigger phrases and routes to per-type workflows. The step-by-step workflow lives in [`../README.md`](../README.md). Read those for the *process*; read this skill for the *visual system*.

This is the **foundation skill**. It defines the shared visual language used across every slide in the project. Two specialized skills extend this base:

- **[instagram-cover-design.md](instagram-cover-design.md)** — for the cover / thumbnail / first slide of a carousel
- **[instagram-step-slide-design.md](instagram-step-slide-design.md)** — for the step-by-step slides that come after the cover

When the user asks me to make a post, I should:
1. Read **this** skill first (visual system, palette, fonts, render pipeline)
2. Then read the **layout-specific** skill that matches what they want (cover or step)
3. Then re-open `Inspiracion/` to re-anchor visually

## Brand handle

The Instagram handle that appears at the top of **every** slide is **`@lucianomusellaa`** (note the double "a"). This is the project owner. The reference creator `@ramiro.cubria` shown in the `Inspiracion/` images is only the *visual style* inspiration — never put their handle on a generated post.

Reference examples live in [Inspiracion/](../Inspiracion/) — always re-read them at the start of a new post job to ground myself visually. The username in those reference images is wrong for our purposes; ignore it and use `@lucianomusellaa`.

---

## 1. Canvas & format

| Property | Value |
|---|---|
| Aspect ratio | **4:5 portrait** (Instagram feed optimal) |
| Resolution | **1080 × 1350 px** |
| Safe margins | ~80 px on all sides; nothing critical inside the outer 60 px |
| Background | Warm off-white **#F5F2ED** (cream / bone), NOT pure white |
| Background texture | **Subtle square grid** overlay, lines ~#E8E4DD, 1 px, 40 px spacing, very low contrast — barely visible. Adds editorial / blueprint feel |

---

## 2. Color palette

Use sparingly. The whole post should feel ~85% neutral, ~15% accent.

| Role | Hex | Use |
|---|---|---|
| Background | `#F5F2ED` | Canvas |
| Grid lines | `#E8E4DD` | Background grid |
| Primary text | `#0E0E0E` | Headlines, body |
| Secondary text | `#8A8780` | Username, captions, "PASO X" labels |
| **Accent coral** | `#E85D3C` | Highlighted keywords, brand circles, arrows |
| **Highlight yellow** | `#FFE45C` | Background highlight behind 1-2 words (like a marker) |
| Soft shadow | `rgba(14,14,14,0.08)` | Behind UI mockups / cards |

**Rule:** never use more than **two** accent colors per slide. Default to coral. Yellow is for one specific highlighted word/phrase only.

---

## 3. Typography

- **Family:** A modern geometric/grotesque sans-serif. Preferred order: `Inter`, `Söhne`, `Aeonik`, `Manrope`, fallback `system-ui, -apple-system, sans-serif`.
- **Headline weight:** 700 (Bold) or 800 (ExtraBold)
- **Body weight:** 500 (Medium)
- **Username/labels:** 500–600, tracked +2%

### Hierarchy (for 1080×1350 canvas)

| Element | Size | Weight | Color | Notes |
|---|---|---|---|---|
| `@username` (top) | 26 px | 500 | `#8A8780` | Centered, ~70 px from top |
| `PASO X` label | 24 px | 600 | `#8A8780` | UPPERCASE, letter-spacing +8%, only on step slides |
| **Headline** | 56–68 px | 800 | `#0E0E0E` | 2–3 lines max, centered, line-height 1.15 |
| Body / subtitle | 28 px | 500 | `#3A3A38` | Optional, only when needed |
| `Deslizá →` (bottom) | 26 px | 700 | `#0E0E0E` | Centered, ~80 px from bottom |

### Headline rules (CRITICAL — this is what makes it catchy)

1. Keep it **short**: 5–10 words total.
2. **Highlight 1–2 key words** in a different style:
   - Option A — color: paint the word in **coral `#E85D3C`** (most common).
   - Option B — yellow marker: place the word on a **yellow `#FFE45C`** rounded-rectangle background (radius 6 px, padding 8 px horizontal, slight tilt 0°).
   - Option C — both for *huge* emphasis (rare, only on covers).
3. Highlighted words should be **nouns or product names** (e.g. "Claude", "Gemini", "ManyChat", "TRÁFICO", "$100k/mes").
4. **Colombian Spanish only** — see section 3.5 below. NEVER Argentinian voseo, even though the visual reference creator (@ramiro.cubria) writes that way.

---

### 3.5. Spanish grammar — Colombian, NOT Argentinian (CRITICAL)

The visual reference creator @ramiro.cubria writes in Argentinian Spanish ("Creá", "Usá", "Deslizá", "vos"). **We do NOT copy that grammar.** The user's audience is Colombian — Argentinian forms sound foreign and break the connection. We copy his *visual style only*.

**Use the `tú` form, never `vos`:**

| ❌ Argentinian (forbidden) | ✅ Colombian (use this) |
|---|---|
| Creá tu agente | Crea tu agente |
| Definí las reglas | Define las reglas |
| Instalá Claude Code | Instala Claude Code |
| Convertí tus tareas | Convierte tus tareas |
| Delegá tareas pesadas | Delega tareas pesadas |
| Armá una campaña | Arma una campaña |
| Usá Gemini | Usa Gemini |
| Configurá el prompt | Configura el prompt |
| Conectá tu API | Conecta tu API |
| Agendá llamadas | Agenda llamadas |
| Guardá este post | Guarda este post |
| Deslizá → | Desliza → |
| ¿Tenés cuenta? | ¿Tienes cuenta? |
| ¿Querés más? | ¿Quieres más? |
| ¿Podés hacerlo? | ¿Puedes hacerlo? |
| Vos sos el dueño | Tú eres el dueño |

**Reflexive imperatives keep the accent on the verb stem:**
- `instálalo` (instala + lo), `arráncalo`, `guárdalo`, `créalo`

**Neutral Latin American Colombian** is the target — avoid both Spain Spanish (`vosotros`, `coger`, `ordenador`) and hyper-local Colombian slang (`parcero`, `bacano`) unless the user explicitly asks for slang.

**Verification step (mandatory):** before exporting any slide, scan every Spanish word for these forbidden markers and rewrite if any appear:
- `á` at the end of an imperative verb (creá, usá, deslizá, etc.)
- `vos`, `tenés`, `querés`, `podés`, `sos`

---

## 4. Layout patterns

Layout-specific design (logos, mockups, PASO labels, chevrons, etc.) lives in the two specialized skills:

- **Cover layouts** → see [instagram-cover-design.md](instagram-cover-design.md)
- **Step slide layouts** → see [instagram-step-slide-design.md](instagram-step-slide-design.md)

Always read the matching specialized skill before designing a slide. This base skill only owns the *system* (canvas, palette, fonts, render pipeline, anti-patterns).

---

## 4.5. Slide indicator (mandatory on all carousel slides)

Every slide in a carousel must show a **slide indicator** at the bottom — a row of small circles, one per slide, where the current slide's dot is highlighted in coral and bigger. This gives the viewer a clear sense of progress.

**Position:** stacked directly above the `Desliza →` footer text. On the closing slide (which has no `Desliza →`), the indicator goes at the bottom of the center block.

**Style spec:**

| Property | Value |
|---|---|
| Inactive dot | 9 × 9 px circle, fill `#D5D0C8` (slightly darker than the grid lines, visible but quiet) |
| Active dot | 13 × 13 px circle, fill coral `#E85D3C` (bigger than inactive, draws the eye) |
| Gap between dots | 12 px |
| Vertical gap from indicator to `Desliza →` | 18 px |
| Number of dots | One per slide in the carousel (6 slides → 6 dots, etc.) |
| Active dot position | Always matches the slide's index in the carousel (slide 1 → first dot active, slide 4 → fourth dot active, etc.) |

**HTML pattern:**

```html
<style>
  .footer { display: flex; flex-direction: column; align-items: center; gap: 18px; }
  .indicator { display: flex; gap: 12px; align-items: center; }
  .dot { width: 9px; height: 9px; border-radius: 50%; background: #D5D0C8; }
  .dot.active { width: 13px; height: 13px; background: #E85D3C; }
</style>

<!-- replace the bare .swipe with this footer block: -->
<div class="footer">
  <div class="indicator">
    <div class="dot"></div>
    <div class="dot active"></div>  <!-- the active one matches this slide's index -->
    <div class="dot"></div>
    <div class="dot"></div>
    <div class="dot"></div>
    <div class="dot"></div>
  </div>
  <div class="swipe">Desliza →</div>
</div>
```

**Rules:**
- Always include the indicator on every slide in a carousel — not just the cover
- The total number of dots must equal the total number of slides in the carousel (no extras, no missing)
- Only **one** dot is active per slide
- For the **closing slide** (no `Desliza →`), the indicator sits at the bottom of the center-block instead, with `margin-top: 18px` from the previous element
- For single standalone posts (not a carousel), skip the indicator

---

## 5. Composition rules

- **Vertical rhythm:** username (top) → label/headline (upper third) → visual (center) → "Deslizá" (bottom). Always this order.
- **Centering:** everything is **center-aligned horizontally**. No left-aligned text on these.
- **Whitespace is sacred:** at least 25% of the canvas should be empty cream background. Resist the urge to fill space.
- **One focal point per slide.** The eye should land on the headline first, then the visual.
- **No more than 2 visual elements** besides text per slide.

---

## 6. What to AVOID (anti-patterns)

- ❌ Pure white `#FFFFFF` background — too sterile, breaks the warmth
- ❌ Gradients, glows, or 3D effects
- ❌ More than 2 accent colors
- ❌ Drop shadows on text
- ❌ Stock-photo backgrounds
- ❌ Emojis inside the headline (small icons OK as visual elements)
- ❌ Centered text wider than 80% of canvas width
- ❌ More than 12 words in a headline
- ❌ Sans-serif "techy" fonts like Orbitron / Audiowide
- ❌ Generic AI-art aesthetic (neon, cyberpunk, holographic)

---

## 7. My workflow when the user asks for a post

When the user asks me to make a post / carousel, I will:

1. **Re-open `Inspiracion/`** and view at least 2 reference images to re-anchor visually.
2. **Ask the user (only if missing):**
   - What's the topic / message?
   - Is it a single cover or a full carousel? How many slides?
   - Any specific keyword(s) to highlight?
   - Should I include a screenshot/mockup, and if so do they have an asset or should I mock one up?
3. **Propose the slide breakdown** in text first (slide 1: cover, slide 2: paso 1, etc.) with the headline and highlighted word for each. Wait for approval before generating images.
4. **Generate the slide(s) via HTML + headless render to PNG.**
   - Write a self-contained `.html` file using the template in section 8 (inline ALL CSS — no external stylesheets, no relative imports)
   - Render to 1080×1350 PNG using **`./render.sh {folder}`** from the project root. The script wraps headless Chrome with all the right flags and handles Git Bash → Windows path conversion. Do NOT call Chrome manually.
   - Example: `./render.sh PostTypes/step-by-step/Outputs/agentes-claude-code` renders every `.html` in that folder to a PNG of the same name.
   - Single-file mode also works: `./render.sh PostTypes/step-by-step/Outputs/agentes-claude-code/cover_v1.html`

   For slides that need illustrations or imagery that HTML/CSS can't build, recreate them with elaborate inline SVG inside the HTML template. This is the only image-generation method used in this project — no external APIs.
5. **Save outputs** to [Outputs/](../Outputs/) with naming `post_{topic-slug}_{slide-number}.png`.
6. **Show the result** and offer iterations (color tweak, headline rewrite, layout swap).

---

## 8. Reusable HTML/CSS template

Use this as the starting point for every slide. Adjust per slide type.

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700;800&display=swap');
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    width: 1080px; height: 1350px;
    background: #F5F2ED;
    background-image:
      linear-gradient(#E8E4DD 1px, transparent 1px),
      linear-gradient(90deg, #E8E4DD 1px, transparent 1px);
    background-size: 40px 40px;
    font-family: 'Inter', system-ui, sans-serif;
    color: #0E0E0E;
    display: flex; flex-direction: column;
    align-items: center; justify-content: space-between;
    padding: 70px 80px;
  }
  .username { font-size: 26px; font-weight: 500; color: #8A8780; }
  .step-label {
    font-size: 24px; font-weight: 600; color: #8A8780;
    text-transform: uppercase; letter-spacing: 0.08em;
    margin-bottom: 20px;
  }
  .headline {
    font-size: 62px; font-weight: 800; line-height: 1.15;
    text-align: center; max-width: 880px;
  }
  .accent-coral { color: #E85D3C; }
  .accent-yellow {
    background: #FFE45C; padding: 4px 12px; border-radius: 6px;
  }
  .center-block { display: flex; flex-direction: column; align-items: center; gap: 40px; flex: 1; justify-content: center; }
  .swipe { font-size: 26px; font-weight: 700; }
  .mockup {
    border-radius: 18px;
    box-shadow: 0 12px 40px rgba(14,14,14,0.08);
    max-width: 720px;
  }
  .logo-row { display: flex; align-items: center; gap: 32px; }
  .logo-bubble {
    width: 130px; height: 130px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 8px 24px rgba(14,14,14,0.08);
  }
  .logo-bubble.white { background: #FFFFFF; }
  .logo-bubble.coral { background: #E85D3C; }
  .connector { width: 80px; height: 2px; background: #0E0E0E; position: relative; }
  .connector::after {
    content: ''; width: 28px; height: 28px; border-radius: 50%;
    background: #FFFFFF; border: 2px solid #0E0E0E;
    position: absolute; left: 50%; top: 50%;
    transform: translate(-50%, -50%);
  }
</style>
</head>
<body>
  <div class="username">@lucianomusellaa</div>
  <div class="center-block">
    <!-- optional: <div class="step-label">Paso 1</div> -->
    <h1 class="headline">¿Cómo agendar llamadas<br>de venta con <span class="accent-coral">Claude</span> y ManyChat?</h1>
    <!-- slot for visual element: logo-row, mockup img, etc. -->
  </div>
  <div class="swipe">Deslizá →</div>
</body>
</html>
```

---

## 9. Quick reference checklist (run before exporting any slide)

- [ ] Canvas is 1080×1350, cream `#F5F2ED` with subtle grid
- [ ] Username at top in small grey
- [ ] Headline is ≤10 words with 1–2 highlighted keywords
- [ ] Highlight color is coral OR yellow (not both unless cover)
- [ ] One focal visual, centered, with soft shadow
- [ ] "Deslizá →" at bottom
- [ ] At least 25% empty whitespace
- [ ] No gradients, no emojis in headline, no pure white
- [ ] **Colombian Spanish only** — no `creá`, `usá`, `deslizá`, `vos`, `tenés`, `querés` (see section 3.5)
- [ ] **Slide indicator** present at bottom (6 dots for 6-slide carousel, etc.) with the correct dot active (see section 4.5)
- [ ] Saved to `Outputs/` with descriptive name
