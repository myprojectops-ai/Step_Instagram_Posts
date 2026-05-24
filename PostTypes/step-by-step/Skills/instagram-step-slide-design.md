---
name: instagram-step-slide-design
description: Design step-by-step slides for a tutorial Instagram carousel -- the slides AFTER the cover that walk the viewer through PASO 01, PASO 02, etc., plus the closing slide. Use whenever the user asks for a step slide, paso, tutorial slide, or closing/cierre. Extends instagram-post-design (base) and Brand/brand-spec.md (canonical visual system).
type: skill
---

# Step Slide & Closing Slide Design

This skill defines how to design the **step slides** (PASO 01, PASO 02, ...) that come after the cover, and the **closing slide** at the end. It extends [instagram-post-design.md](instagram-post-design.md) and [Brand/brand-spec.md](../../../Brand/brand-spec.md).

**Always open at least 2 reference step PNGs from `Brand/Templates/Tutorial/{COLOR}/{STYLE}/{MODE}/` before building step slides.**

---

## 1. The step slide's job

The cover stopped the scroll. Step slides **deliver the value**:
- Tell the viewer exactly which step they're on (eyebrow: `TUTORIAL · PASO 0X`)
- Give them the action in plain Colombian Spanish (the headline, with 1 italic emphasis word)
- Show them what it looks like (terminal mockup, orgchart, screenshot, or other visual)
- Optionally explain *why* in a short body paragraph (rarely needed)

A step slide without a visual hook is almost always a wasted slide. Default to including one.

---

## 2. The eyebrow (mandatory)

Every step slide opens with an "eyebrow" above the headline:

```
TUTORIAL · PASO 01
```

| Property | Value |
|---|---|
| Text | `TUTORIAL · PASO 0X` where X is the step number (01, 02, 03, ...) -- always 2-digit zero-padded |
| Font | Roboto Medium 500 |
| Size | 18-20 px |
| Color | scheme highlight color (`#ffb050` AMARILLO / `#e60000` ROJO / `#0056a6` AZUL) |
| Style | ALL CAPS, letter-spacing 2px |
| Position | Centered, ~16-24 px above the headline |

The eyebrow is **mandatory** on every step slide. It's how the viewer tracks progress through the carousel.

---

## 3. Step headline rule

| Property | Value |
|---|---|
| Word count | 4-8 words (shorter than covers -- the cover already set context) |
| Lines | 1-2 (almost never 3) |
| Font | Roboto Bold 700 |
| Size | 64-72 px |
| Emphasis | **1 word** in Playfair Display Italic in scheme highlight color (same pattern as cover, just shorter overall headline) |
| Tone | Colombian Spanish action-imperative: "Instala", "Configura", "Conecta", "Delega", "Agenda" |

**Good headlines (Colombian Spanish):**
- "Instala Claude Code en tu *terminal*"
- "Configura tu primer *MCP*"
- "Delega tareas pesadas a *subagentes*"
- "Conecta tu API key de *Claude*"
- "Define las reglas en *CLAUDE.md*"

**Bad headlines:**
- "Vamos a crear un flujo en ManyChat ahora" (too long, too soft)
- "ManyChat es la herramienta que vamos a usar" (no verb, no action)
- "Creá un flujo en ManyChat" (Argentinian voseo -- wrong for this audience)
- "Configura el *MCP* y los *agentes*" (two italic words -- single emphasis only)

---

## 4. Step slide layout

### Vertical structure (top → bottom)

| Order | Element | Notes |
|---|---|---|
| 1 | (no `@lucianomusellaa` on step slides) | Save vertical space for content. Handle lives only on the cover. |
| 2 | **`TUTORIAL · PASO 0X`** eyebrow | Centered, scheme highlight color, small caps, 18-20 px |
| 3 | **Headline** | 1-2 lines, Roboto Bold 64-72 px, 1 word in Playfair Italic |
| 4 | Optional body subtitle | 1-2 lines, 24-28 px Roboto Regular, text-secondary color. Use sparingly -- if the visual carries the explanation, skip the subtitle |
| 5 | **Visual hook** | The centerpiece. Terminal mockup, orgchart cards, screenshot, or illustration. Max-width ~960 px |
| 6 | (no Desliza pill on interior steps -- the cover has it; intermediate steps don't need to remind users to swipe) | Optional: small "Desliza" pill at bottom on the last step before the closing slide |

### Visual hook patterns (from templates)

The visual below the headline carries most of the explanation. Choose per step content:

**Terminal mockup** -- for code/CLI tutorials. macOS-style window with 3 dots top-left, title in mono, content area showing commands with prompts in scheme highlight color.

**Orgchart of "code-window cards"** -- for "agent + subagents" or "X delegates to Y" patterns. Cards rendered as mini code-windows with macOS dots top-left + small green status dot top-right + label + body text. Connected by dashed lines in scheme highlight color. Template reference: `Brand/Templates/Tutorial/AMARILLO/PLANO/LIGHT_DARK/*-18.png`.

**Screenshot/UI list** -- for tutorials that walk through real interfaces. Use a real screenshot or recreate the relevant fragment in HTML+CSS. Highlight the relevant item with the scheme highlight color.

**Diagram/illustration** -- for abstract concepts (memory flow, network architecture). Minimalist inline SVG using brand palette only.

---

## 5. Anti-patterns (step slides)

- ❌ Missing `TUTORIAL · PASO 0X` eyebrow
- ❌ Two or more italic emphasis words (single emphasis only)
- ❌ No visual hook (step slides without a visual feel empty -- find a visual angle)
- ❌ Tilted mockups (covers can tilt slightly; step slides must be straight)
- ❌ Subtitle longer than 2 lines (rewrite the headline if you need more)
- ❌ Headline > 8 words
- ❌ Solid color pill on step slides (pills are for cover headlines / closing CTA only)
- ❌ Page dots (Instagram adds them natively)
- ❌ Numbering as "Paso uno" or "Step 1" -- always `PASO 01` with zero-pad
- ❌ Skipping a step number (PASO 01, PASO 02, PASO 03 -- never PASO 01, PASO 03)

---

## 6. Step slide HTML scaffold (LIGHT + AMARILLO -- adapt tokens per mode/scheme)

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
  /* @font-face block -- see instagram-post-design.md §7 */
  @font-face { font-family: 'Roboto'; src: url('../../../../Brand/Fonts/Roboto/static/Roboto-Regular.ttf') format('truetype'); font-weight: 400; font-style: normal; font-display: block; }
  @font-face { font-family: 'Roboto'; src: url('../../../../Brand/Fonts/Roboto/static/Roboto-Medium.ttf')  format('truetype'); font-weight: 500; font-style: normal; font-display: block; }
  @font-face { font-family: 'Roboto'; src: url('../../../../Brand/Fonts/Roboto/static/Roboto-Bold.ttf')    format('truetype'); font-weight: 700; font-style: normal; font-display: block; }
  @font-face { font-family: 'Roboto'; src: url('../../../../Brand/Fonts/Roboto/static/Roboto-Black.ttf')   format('truetype'); font-weight: 900; font-style: normal; font-display: block; }
  @font-face { font-family: 'Playfair Display'; src: url('../../../../Brand/Fonts/PlayfairDisplay/static/PlayfairDisplay-Italic.ttf') format('truetype'); font-weight: 400; font-style: italic; font-display: block; }

  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body { width: 1080px; height: 1350px; overflow: hidden; }
  body {
    background: #efedec;
    font-family: 'Roboto', system-ui, sans-serif;
    color: #0c1314;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    padding: 90px 80px;
  }
  .center-block { display: flex; flex-direction: column; align-items: center; gap: 50px; width: 100%; max-width: 960px; }
  .text-stack { display: flex; flex-direction: column; align-items: center; gap: 18px; }
  .eyebrow {
    color: #ffb050; font-size: 18px; font-weight: 500;
    text-transform: uppercase; letter-spacing: 2px;
  }
  .headline {
    font-size: 68px; font-weight: 700; line-height: 1.1;
    text-align: center; letter-spacing: -0.02em; max-width: 900px;
  }
  .emphasis { font-family: 'Playfair Display'; font-style: italic; font-weight: 400; color: #ffb050; }
  .hook { width: 100%; }
  /* Terminal mockup (reuse the same one from cover scaffold) */
  .terminal { background: #0c1314; border-radius: 12px; overflow: hidden; }
  .terminal-bar { background: #1a2225; padding: 14px 18px; display: flex; align-items: center; gap: 8px; }
  .terminal-dot { width: 12px; height: 12px; border-radius: 50%; }
  .terminal-dot.r { background: #ff6058; } .terminal-dot.y { background: #ffbe2e; } .terminal-dot.g { background: #28c93f; }
  .terminal-title { color: #8a9499; font-size: 14px; flex: 1; text-align: center; font-family: ui-monospace, Menlo, monospace; }
  .terminal-body { padding: 32px 36px; font-family: ui-monospace, Menlo, monospace; color: #efedec; font-size: 20px; line-height: 1.8; }
  .terminal-comment { color: #8a9499; }
  .terminal-cmd { color: #efedec; }
  .terminal-prompt { color: #ffb050; }
</style>
</head>
<body>
  <div class="center-block">
    <div class="text-stack">
      <div class="eyebrow">TUTORIAL · PASO 01</div>
      <h1 class="headline">Instala Claude Code<br>en tu <span class="emphasis">terminal</span></h1>
    </div>
    <div class="hook">
      <div class="terminal">
        <div class="terminal-bar">
          <div class="terminal-dot r"></div>
          <div class="terminal-dot y"></div>
          <div class="terminal-dot g"></div>
          <div class="terminal-title">~/mi-agente — bash</div>
        </div>
        <div class="terminal-body">
          <div class="terminal-comment"># instálalo globalmente con npm</div>
          <div class="terminal-cmd">&nbsp;&nbsp;&nbsp;&nbsp;npm install -g @anthropic-ai/claude-code</div>
          <br>
          <div class="terminal-comment"># entra a tu proyecto y arráncalo</div>
          <div class="terminal-cmd">&nbsp;&nbsp;&nbsp;&nbsp;cd mi-agente</div>
          <div class="terminal-cmd">&nbsp;&nbsp;&nbsp;&nbsp;claude</div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
```

---

## 7. The closing slide (last slide of the carousel)

The carousel doesn't end on the last step -- it ends on a **closing slide** whose only job is to drive engagement: a follow, a save, a comment, or a DM.

### Vertical structure

| Order | Element | Notes |
|---|---|---|
| 1 | `@lucianomusellaa` (return -- closing brings the handle back) | Top center, scheme highlight color |
| 2 | **Mascot/icon** | ~140-160 px. Sparkle, cursor, agent icon, Claude logo, or hand-drawn SVG character. Signals "warm closer" |
| 3 | **Big primary text** | 56-64 px Roboto Bold, lowercase for friendliness, period at the end. "sígueme para más.", "no te vayas todavía.", "guarda este post." |
| 4 | Thin divider | 80 px wide, 1.5 px, text-primary color |
| 5 | Small grey label | 20-22 px Roboto Medium, text-subtle color. ONE WORD: "comenta", "envía", "guarda", "responde" |
| 6 | **CTA pill** | White-on-dark (LIGHT mode) or dark-on-light (DARK mode), border-radius 14 px. Big bold trigger in ALL CAPS: `"AGENTE"`, `"PROMPTS"`, `"SISTEMA"`. 38-44 px Roboto Bold. ONE WORD, memorable, all caps -- viewers will type it in comments |
| 7 | Caption below CTA | 20-22 px, "y te envío la guía completa", "para recibir el setup", first-person |

### Closing slide rules

- **No eyebrow** (no `PASO X` -- this is not a step)
- **No "Desliza"** (this is the end of the carousel)
- **The trigger word in the CTA pill is ONE word, ALL CAPS, memorable**
- **First-person, conversational** caption: "te envío", "te paso", "te mando"

### Good closing copy (Colombian Spanish)

- "sígueme para más." → comenta → `"AGENTE"` → "y te envío el setup completo"
- "¿quieres armar el tuyo?" → comenta → `"PROMPTS"` → "y te paso mis prompts"
- "no te vayas todavía." → comenta → `"SISTEMA"` → "y te mando la guía"
- "guarda este post." → para que → `"VOLVER"` → "cuando lo necesites"

### Closing slide HTML scaffold (adapt scheme/mode tokens)

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
  /* @font-face block -- see instagram-post-design.md §7 (omitted here for brevity) */
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body { width: 1080px; height: 1350px; overflow: hidden; }
  body {
    background: #efedec;
    font-family: 'Roboto', system-ui, sans-serif;
    color: #0c1314;
    display: flex; flex-direction: column;
    align-items: center; justify-content: space-between;
    padding: 80px 80px 90px;
  }
  .handle { color: #ffb050; font-size: 22px; font-weight: 500; letter-spacing: 0.5px; }
  .center-block { display: flex; flex-direction: column; align-items: center; gap: 28px; flex: 1; justify-content: center; width: 100%; }
  .mascot { width: 160px; height: 160px; }
  .big-text { font-size: 60px; font-weight: 700; line-height: 1.05; text-align: center; letter-spacing: -0.025em; margin-top: 12px; }
  .divider { width: 80px; height: 1.5px; background: #0c1314; margin: 8px 0; }
  .label { font-size: 22px; font-weight: 500; color: #6b6860; }
  .cta-pill {
    background: #0c1314; color: #efedec;
    border-radius: 16px;
    padding: 22px 56px;
    font-size: 42px; font-weight: 700;
    letter-spacing: 0.02em;
  }
  .caption { font-size: 22px; font-weight: 500; color: #6b6860; margin-top: 4px; }
</style>
</head>
<body>
  <div class="handle">@lucianomusellaa</div>
  <div class="center-block">
    <div class="mascot"><!-- SVG character or icon --></div>
    <div class="big-text">sígueme para más.</div>
    <div class="divider"></div>
    <div class="label">comenta</div>
    <div class="cta-pill">"AGENTE"</div>
    <div class="caption">y te envío el setup completo</div>
  </div>
</body>
</html>
```

---

## 8. Step slide checklist (run before exporting each step)

- [ ] **`TUTORIAL · PASO 0X`** eyebrow present, scheme highlight color, ALL CAPS, letter-spacing 2px
- [ ] Headline is 4-8 words, 1-2 lines, Roboto Bold
- [ ] **Exactly 1 word** in Playfair Italic emphasis in scheme highlight color
- [ ] Visual hook present (terminal / orgchart / screenshot / illustration)
- [ ] No tilted elements (step slides must be straight)
- [ ] No solid pills, no eyebrows besides the PASO one
- [ ] No page dots
- [ ] Step number is correct in sequence (no skipped numbers, always 2-digit `01` `02`)
- [ ] All step slides use the same headline font-size for visual consistency
- [ ] Colombian Spanish only
- [ ] Saved to `Outputs/{topic-slug}/paso_{n}_{descriptor}.png`

## 9. Closing slide checklist

- [ ] `@lucianomusellaa` returns at top (it was on the cover, absent on interior steps, present again on the closer)
- [ ] Mascot/icon present at the top of the center block
- [ ] Big primary text in lowercase, period at end
- [ ] Thin divider line below the big text
- [ ] One-word grey label ("comenta", "envía", etc.)
- [ ] CTA pill contains ONE word in ALL CAPS
- [ ] First-person caption below the CTA
- [ ] No `PASO X` eyebrow, no "Desliza", no page dots
- [ ] Saved to `Outputs/{topic-slug}/cierre_cta.png`
