---
name: instagram-post-design
description: BASE visual system for step-by-step Instagram posts (tutorials, how-tos, paso-a-paso). Defines the shared design language, headline patterns, Colombian Spanish rules, and HTML scaffolds. The two sibling skills (instagram-cover-design, instagram-step-slide-design) extend this base. Read this first whenever building a step-by-step post.
type: skill
---

# Instagram Step-by-Step Post Design -- Base System

> **Project root:** `c:/Trabajo_AI/Visual_posts/`. The autoloaded [CLAUDE.md](../../../CLAUDE.md) is the master router. The step-by-step workflow lives in [../README.md](../README.md). The **brand visual system lives in [Brand/brand-spec.md](../../../Brand/brand-spec.md)** -- this skill builds on top of it.

This is the **foundation skill** for the step-by-step (tutorial) post type. Two specialized skills extend it:

- **[instagram-cover-design.md](instagram-cover-design.md)** -- the cover / first slide of the carousel
- **[instagram-step-slide-design.md](instagram-step-slide-design.md)** -- the step slides + closing slide

When the user asks for a tutorial post, I:
1. Read **brand-spec.md** (canonical palette, fonts, slide patterns)
2. Read **this** skill (step-by-step workflow + Colombian Spanish + scaffolds)
3. Read the layout-specific sibling skill (cover or step)
4. Re-anchor visually -- start with `Brand/Templates/Tutorial/{COLOR}/{STYLE}/{MODE}/`, then `Inspiracion/`, then `Favoritos_Claude_Generated/`

---

## 1. Brand fundamentals (delegated to brand-spec.md)

All visual rules -- palette, fonts, `@font-face` block, color mappings per scheme/mode -- live in [Brand/brand-spec.md](../../../Brand/brand-spec.md). **Read it once at session start.** This skill does NOT duplicate that content.

### Quick reference for tutorials specifically

- **Canvas:** 1080 × 1350 px (4:5 portrait)
- **Color scheme + mode:** asked at the start of every post (AMARILLO / ROJO / AZUL × LIGHT / DARK)
- **Background:** brand-spec `bg-primary` for the chosen mode (e.g. `#efedec` for LIGHT, `#11191b` for DARK)
- **Body text:** brand-spec `text-primary` for the mode
- **Highlights:** the chosen scheme's `highlight-primary` token (e.g. `#ffb050` for AMARILLO)
- **Fonts:** Roboto (body) + Playfair Display Italic (emphasis only)
- **Handle:** `@lucianomusellaa` in orange small caps at top of every slide (this is the step-by-step rule -- news does NOT use the handle)

---

## 2. Headline rules (specific to step-by-step)

Headlines on tutorial slides follow strict rules so the carousel feels coherent:

### 2.1 Cover headline

- **Length:** 5-10 words, 2-3 lines max
- **Emphasis:** **1 word** in Playfair Display Italic in the scheme's highlight color. This is the new "double highlight" -- a single italic-serif word that adds editorial character vs. surrounding Roboto Bold.
- **Optional accent:** a solid-color pill (e.g. "en 4 pasos") with white text in the scheme's `solid` token. Single pill per cover, not multiple.

Examples (AMARILLO scheme):
- "Crea tu propio agente de IA con *Claude Code*" + pill "en 4 pasos"
- "Configura *MCPs* en Claude Code paso a paso"
- "Arma tu primer *agente* de Claude en 5 minutos"

### 2.2 Step slide headline

- **Length:** 4-8 words, 1-2 lines max
- **Eyebrow above headline:** `TUTORIAL · PASO 0X` in orange small caps, letter-spacing 2px, font-size 18-20px
- **Emphasis:** **1 word** in Playfair Display Italic in scheme highlight color (same pattern as cover, but shorter headline)
- Examples:
  - "Instala Claude Code en tu *terminal*"
  - "Configura el *MCP* en tu proyecto"
  - "Delega tareas pesadas a *subagentes*"

### 2.3 Closing slide

The last slide drives engagement (follow, save, DM). Pattern:
- Friendly mascot/icon (sparkle, agent icon, cursor) ~140-160 px tall
- Big primary text in lowercase: "sígueme para más.", "guarda este post.", "no te vayas todavía."
- Thin divider line
- Small grey label: "comenta" / "envía" / "responde"
- **CTA pill** (white-on-dark or solid-color background) with a ONE-WORD trigger in ALL CAPS: `"AGENTE"`, `"PROMPTS"`, `"SISTEMA"`
- Caption below CTA: "y te envío la guía completa", "para recibir el setup"

---

## 3. Colombian Spanish -- CRITICAL

The visual reference creator @ramiro.cubria writes in Argentinian Spanish ("Creá", "Usá", "Deslizá", "vos"). **We do NOT copy that grammar.** The user's audience is Colombian -- Argentinian forms sound foreign.

### Use the `tú` form, never `vos`:

| Argentinian (forbidden) | Colombian (use this) |
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

**Neutral Latin American Colombian** is the target -- avoid both Spain Spanish (`vosotros`, `coger`, `ordenador`) and hyper-local Colombian slang (`parcero`, `bacano`) unless the user explicitly asks for slang.

**Verification step (mandatory):** before exporting any slide, scan every Spanish word for these forbidden markers and rewrite if any appear:
- `á` at the end of an imperative verb (creá, usá, deslizá, etc.)
- `vos`, `tenés`, `querés`, `podés`, `sos`

---

## 4. Composition rules

- **Vertical rhythm:** username (top) → eyebrow/headline (upper-mid) → visual hook (center) → "Desliza" pill (bottom). Always this order.
- **Centering:** everything center-aligned horizontally. No left-aligned text on these.
- **No page dots.** Instagram adds carousel pagination natively. Do NOT add dot indicators to slides -- per `feedback_no_page_dots.md`.
- **Whitespace:** ~15-30% of the canvas should be empty background. Resist filling space.
- **One focal point per slide.** Eye lands on headline first, then visual.
- **Slide spacing rules apply** -- see [Skills/slide-spacing.md](../../../Skills/slide-spacing.md). Content fills ~70-85% of usable canvas; never leave >150px empty in the middle or >120px at the bottom.

---

## 5. Anti-patterns (step-by-step)

- ❌ More than 1 italic emphasis word in a single headline (use only 1)
- ❌ Mixing accent colors from different schemes (a yellow post should not have red highlights)
- ❌ Page dots / carousel indicators -- IG adds them natively
- ❌ Gradients, glows, 3D effects (unless using a GRADIENTES template variant)
- ❌ Emojis inside the headline (small inline icons OK as visual elements)
- ❌ Centered text wider than 80% of canvas width
- ❌ More than 12 words in a headline
- ❌ Sans-serif "techy" fonts like Orbitron / Audiowide -- only Roboto for body, Playfair Italic for emphasis
- ❌ Generic AI-art aesthetic (neon, cyberpunk, holographic)
- ❌ Colombian Spanish violations (creá, usá, deslizá, vos, tenés)

---

## 6. Workflow when building a step-by-step post

When the user triggers a tutorial post (after I've already collected type + color + mode per CLAUDE.md §1):

1. **Re-anchor visually** -- open `Brand/Templates/Tutorial/{COLOR}/{STYLE}/{MODE}/` and read at least 2 PNGs. Then `Inspiracion/` and `Favoritos_Claude_Generated/`.
2. **Ask only missing context:** topic, number of slides (default cover + 4 pasos + closing = 6), source material URL/doc if any, specific keywords to italicize, real screenshots in `Assets/`?
3. **Propose the slide breakdown** in plain text (slide 1: cover with headline + italic word; slide 2: paso 1 with eyebrow + headline + visual; etc.). Wait for approval.
4. **Generate any missing logos via Higgsfield MCP** -- only if a needed brand logo is missing from `Logos/`. Save to `Logos/` after user review.
5. **Create output folder:** `PostTypes/step-by-step/Outputs/{topic-slug}/`
6. **Write each slide's HTML** using the scaffold from §7 below + the layout-specific sibling skill's recipes.
7. **Render** with `./render.sh PostTypes/step-by-step/Outputs/{topic-slug}` -- batch renders all HTMLs in the folder.
8. **Mandatory Visual QA** ([Skills/visual-qa.md](../../../Skills/visual-qa.md)) -- read every PNG, check fonts loaded, palette correct, Colombian Spanish, no page dots, layout proportions.
9. **Present the carousel** as a sequence (cover → paso 1 → ... → closing).
10. **Ask for favorites** (CLAUDE.md §1.6) -- copy chosen slides to `Favoritos_Claude_Generated/`.

---

## 7. Reusable HTML scaffold (canonical starting point)

Use this as the starting point for every tutorial slide. Adjust the inner content per slide type. The `@font-face` block is the SAME across all slides -- it's what makes Roboto + Playfair Italic render.

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
  /* @font-face block -- canonical, see Brand/brand-spec.md §2 */
  @font-face { font-family: 'Roboto'; src: url('../../../../Brand/Fonts/Roboto/static/Roboto-Regular.ttf') format('truetype'); font-weight: 400; font-style: normal; font-display: block; }
  @font-face { font-family: 'Roboto'; src: url('../../../../Brand/Fonts/Roboto/static/Roboto-Medium.ttf')  format('truetype'); font-weight: 500; font-style: normal; font-display: block; }
  @font-face { font-family: 'Roboto'; src: url('../../../../Brand/Fonts/Roboto/static/Roboto-Bold.ttf')    format('truetype'); font-weight: 700; font-style: normal; font-display: block; }
  @font-face { font-family: 'Roboto'; src: url('../../../../Brand/Fonts/Roboto/static/Roboto-Black.ttf')   format('truetype'); font-weight: 900; font-style: normal; font-display: block; }
  @font-face { font-family: 'Playfair Display'; src: url('../../../../Brand/Fonts/PlayfairDisplay/static/PlayfairDisplay-Italic.ttf') format('truetype'); font-weight: 400; font-style: italic; font-display: block; }

  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body { width: 1080px; height: 1350px; overflow: hidden; }
  body {
    /* CHANGE per mode: LIGHT bg #efedec | DARK bg #11191b (or gradient to navy) */
    background: #efedec;
    font-family: 'Roboto', system-ui, sans-serif;
    /* CHANGE per mode: LIGHT text #0c1314 | DARK text #ffffff */
    color: #0c1314;
    display: flex; flex-direction: column;
    align-items: center; justify-content: space-between;
    padding: 70px 80px 90px;
  }
  /* @lucianomusellaa handle -- always orange-ish small caps top-center */
  .handle {
    /* CHANGE per scheme: AMARILLO #ffb050 | ROJO #e60000 | AZUL #0056a6 */
    color: #ffb050;
    font-size: 22px; font-weight: 500;
    letter-spacing: 0.5px;
  }
  /* Headline -- Roboto Bold, scale per content length per slide-spacing.md */
  .headline {
    font-size: 72px; font-weight: 700; line-height: 1.08;
    text-align: center; max-width: 900px; letter-spacing: -0.02em;
  }
  /* Emphasis word -- Playfair Italic in scheme highlight color */
  .emphasis {
    font-family: 'Playfair Display'; font-style: italic; font-weight: 400;
    color: #ffb050; /* match scheme */
  }
  /* Solid pill (e.g. "en 4 pasos") */
  .pill-solid {
    background: #ff9d00; /* scheme solid token */
    color: #ffffff;
    padding: 18px 46px;
    font-size: 44px; font-weight: 500;
    border-radius: 4px;
  }
  /* Desliza pill (outline) */
  .swipe-pill {
    border: 2px solid #0c1314; /* text-primary */
    color: #0c1314;
    padding: 14px 56px;
    font-size: 28px; font-weight: 500;
    border-radius: 999px;
    background: transparent;
  }
  /* Center block holds the slide's main stack */
  .center-block {
    display: flex; flex-direction: column; align-items: center;
    gap: 50px; flex: 1; justify-content: center; width: 100%;
  }
</style>
</head>
<body>
  <div class="handle">@lucianomusellaa</div>
  <div class="center-block">
    <h1 class="headline">Crea tu propio agente de IA con <span class="emphasis">Claude Code</span></h1>
    <div class="pill-solid">en 4 pasos</div>
    <!-- slot for visual hook: terminal mockup, illustration, orgchart -->
  </div>
  <div class="swipe-pill">Desliza</div>
</body>
</html>
```

**Where to find the exact tokens per scheme/mode:** see [Brand/brand-spec.md §1](../../../Brand/brand-spec.md). Swap the marked values when building a slide for a different scheme/mode.

---

## 8. Quick reference checklist (run before exporting any slide)

- [ ] Canvas is 1080×1350
- [ ] `@font-face` block uses the canonical Brand/Fonts paths -- no Google Fonts CDN
- [ ] Background matches chosen mode; text color contrasts with bg
- [ ] Headline has 1 word in Playfair Italic in scheme highlight color
- [ ] No page dots / carousel indicators
- [ ] `@lucianomusellaa` in scheme highlight color at top
- [ ] **Colombian Spanish only** -- no `creá`, `usá`, `deslizá`, `vos`, `tenés`, `querés`
- [ ] Saved to `Outputs/{topic-slug}/` with descriptive name
- [ ] Slide-spacing rules satisfied (content fills 70-85% of canvas)
