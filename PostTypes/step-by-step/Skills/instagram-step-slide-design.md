---
name: instagram-step-slide-design
description: Design step-by-step slides for an Instagram carousel — the slides AFTER the cover that walk the viewer through PASO 1, PASO 2, etc. Use whenever the user asks for a step slide, paso, tutorial slide, or any non-cover slide in a step-by-step carousel. Extends instagram-post-design (the base visual system).
type: skill
---

# Instagram Step Slide Design Skill

This skill defines how to design **step slides** — the slides that come *after* the cover in a step-by-step carousel. The cover sold the click; step slides deliver the value. They extend [instagram-post-design.md](instagram-post-design.md), which owns the shared visual system. Read that skill first, then this one.

Reference step slides from [Inspiracion/](../Inspiracion/):
- **`Ej_2.png`** → PASO 1 with body subtitle + UI screenshot
- **`Ej_4.png`** → PASO 2 without body subtitle, just UI screenshot with highlighted item

Always re-open both `Ej_2.png` and `Ej_4.png` before designing step slides — they show the two main variants (with/without body subtitle).

---

## 1. The step slide's job

Where covers stop the scroll, step slides **deliver clarity**. The viewer is already engaged — they swiped. Now each slide must:
- Tell them *exactly* what step they're on (PASO label is non-negotiable)
- Give them the action in plain Spanish (the headline)
- Show them what it looks like (the UI mockup)
- Optionally explain *why* or *how* (the body subtitle)

A step slide that doesn't show a real visual / UI is almost always a wasted slide. Default to including a screenshot or mockup.

---

## 2. The PASO label (mandatory)

Every step slide opens with a small label above the headline:

```
P A S O   1
```

- Text: `PASO {N}` where N is the step number (1, 2, 3…)
- Font: Inter, 24 px, weight 600
- Color: `#8A8780` (secondary grey — same as username)
- Style: **UPPERCASE**, letter-spacing `0.18em` (very wide tracking, gives an editorial / "section header" feel)
- Position: centered, ~18 px above the headline
- Format: literally "PASO 1", "PASO 2", etc. — never "Step 1", never "Paso uno", never numbers without "PASO"

This label is **mandatory** on every step slide. It's how the viewer tracks progress through the carousel.

---

## 3. CRITICAL — Highlight rule for step slides (single only)

> **Step slides use SINGLE highlight only.** Never double.

Pick **one** keyword in the headline and highlight it using either:
- **Coral text** `#E85D3C` (default — use this 80% of the time)
- **Yellow marker** background `#FFE45C` (use when the keyword is short — 1 word, 4–8 chars — and would benefit from extra emphasis)

This is the **opposite** of covers (which default to double). The reason: step slides already have a strong visual element (the UI mockup) and a PASO label competing for attention. Adding a second keyword highlight creates noise. The viewer should land on: PASO label → headline (with one accent word) → mockup, in that order, without anything else fighting for the eye.

If you ever feel tempted to use double highlight on a step slide, instead **rewrite the headline** so only one keyword needs emphasis.

---

## 4. Step slide layout

### Vertical structure (top → bottom)

| Order | Element | Notes |
|---|---|---|
| 1 | `@lucianomusellaa` | Top, ~80 px from top edge, 26 px grey |
| 2 | **`PASO {N}`** label | Centered, uppercase, tracked +0.18em, 24 px grey |
| 3 | **Headline** | 2 lines, 1 keyword highlighted, 52–60 px (smaller than cover headlines), max-width 880 px |
| 4 | *Optional* body subtitle | 1–2 lines, 28–30 px, weight 500, color `#3A3A38`, max-width 800 px, line-height 1.45 |
| 5 | **UI mockup** | The centerpiece. Border-radius 18–24 px, soft shadow, max-width ~720 px |
| 6 | `Desliza →` | Bottom, ~90 px from bottom edge |

Plus, floating on the **left and right edges**, vertically centered:
- **Carousel chevrons** — small white circles (44 px) with thin black `‹` and `›` arrows. These are decorative (they hint that there's more to swipe) and add editorial polish. Optional but recommended.

### Variant A — With body subtitle (Ej_2 style)

Use when the headline alone doesn't fully explain the action. The subtitle adds *context* or the *why* — not instructions. Example:

> **Headline:** "Creá un flujo on **ManyChat**"
> **Subtitle:** "Creá un flujo que se active cuando alguien te escribe por DM o comenta una palabra clave en cualquier post o reel."

Subtitle should be conversational, no jargon, max 2 lines. If it doesn't fit in 2 lines, the headline is wrong — rewrite the headline instead.

### Variant B — Without body subtitle (Ej_4 style)

Use when the **mockup itself** carries the explanation (e.g. a UI list with the relevant item highlighted, a screenshot with an arrow pointing to the right button, a before/after diagram). The headline + visual = enough.

Example:
> **Headline:** "Armá una campaña con **objetivo de TRÁFICO.**"
> *(no subtitle — the screenshot of the campaign objectives list with "Traffic" highlighted does the talking)*

Variant B is the **default** when you have a good visual. Variant A is the fallback when the visual needs context.

---

## 5. The UI mockup (the most important visual)

Step slides live or die by the quality of the UI mockup. It's literally the largest element on the slide and the viewer's eye lands on it second after the headline.

### Sourcing the mockup
1. **Real screenshot** (best) — if the user can provide one, drop it into [Assets/](../../../Assets/) and reference it directly.
2. **Recreated UI in HTML/CSS** — for simple UIs (lists, buttons, cards), it's faster and pixel-perfect to recreate the relevant fragment in HTML inside the slide template. This is what `Ej_4.png` does — that "Choose a campaign objective" panel is just a styled list.

### Mockup styling rules
- **Border-radius:** 18–24 px on the outer container
- **Shadow:** `0 12px 40px rgba(14,14,14,0.08)` plus an outer ambient `0 30px 80px rgba(14,14,14,0.05)` for depth
- **Background:** white `#FFFFFF` (this is one of the *only* places pure white is allowed — it's a UI surface, not a slide background)
- **Max width:** ~720 px so it doesn't dominate the slide
- **Tilt:** never tilt step-slide mockups. Covers can tilt; step slides must be straight (clarity > energy).
- **Highlight inside the mockup:** if the goal is to show the user "click this option", highlight that option using the same yellow `#FFE45C` marker as the slide system. Reuse the brand palette inside the mockup — never introduce new colors.
- **Optional outer accents:** a small coral sparkle/burst icon floating at one corner of the mockup is allowed (rare, used for "this is the AI-powered part" cue).

---

## 6. Carousel chevrons (left/right edge decoration)

Reference: `Ej_4.png` shows these clearly.

- Two circles, one on each side, vertically centered on the slide
- Position: left chevron at `left: 30px, top: 50%`; right chevron at `right: 30px, top: 50%` (translateY -50%)
- Size: 44 × 44 px circles
- Background: `#FFFFFF`
- Shadow: `0 4px 12px rgba(14,14,14,0.08)`
- Inside: a thin chevron arrow icon (`‹` left circle, `›` right circle), color `#1A1A1A`, weight light

These are **decorative**. They don't actually navigate anything when the post is on Instagram — they're a visual hint that this is part of a series. Include them by default on step slides; skip them on covers.

---

## 7. Headline writing rules for step slides

| Rule | Step slide |
|---|---|
| Word count | **4–8 words** (shorter than covers because the cover already set context) |
| Line count | 1–2 lines (almost never 3) |
| Font size | 52–60 px (smaller than cover headlines because the mockup is the visual hero) |
| Highlighted words | **1 keyword** only (single highlight, never double) |
| Tone | **Colombian Spanish, `tú` form** action-imperative: "Crea", "Arma", "Configura", "Agenda", "Conecta", "Define", "Instala", "Convierte". NEVER Argentinian voseo. See section 3.5 of the base skill. |
| Format | Usually starts with a verb. Avoids questions (questions are for covers). |
| Punctuation | Periods OK. Question marks rare. No exclamation marks. |

**Good headlines (Colombian Spanish):**
- "Crea un flujo en **ManyChat**"
- "Arma una campaña con **objetivo de TRÁFICO.**"
- "Conecta tu API key de **Claude**"
- "Configura el **prompt** de venta"
- "Define las reglas en **CLAUDE.md**"

**Bad headlines:**
- "Vamos a crear un flujo en ManyChat ahora" (too long, too soft)
- "ManyChat es la herramienta que vamos a usar" (no verb, no action)
- "Crea un flujo en **ManyChat** y **Claude**" (double highlight — wrong for step slides)
- "Creá un flujo en **ManyChat**" (Argentinian voseo — wrong for this audience)

---

## 8. Step slide-specific anti-patterns

In addition to the base skill's anti-patterns and the cover skill's:

- ❌ Missing `PASO X` label (mandatory)
- ❌ Double-highlighted headline (cover-only — step slides use single highlight)
- ❌ No mockup / no visual (step slides without a visual feel empty — rewrite as a typographic slide only as a last resort)
- ❌ Tilted mockups (covers can tilt; steps must be straight)
- ❌ Subtitle longer than 2 lines (rewrite the headline if you need more)
- ❌ Headline > 8 words (the cover did the explaining; this slide just delivers the action)
- ❌ Logo bubbles (those are cover-only — steps use mockups, not logos)
- ❌ Pure white slide background (the *mockup* is white; the slide is still cream `#F5F2ED`)
- ❌ Numbering as "Paso uno" or "Step 1" — always "PASO 1" exactly
- ❌ Skipping a step number (PASO 1, PASO 2, PASO 3 — never PASO 1, PASO 3)

---

## 9. Workflow when building step slides

1. **Re-read the base skill** [instagram-post-design.md](instagram-post-design.md).
2. **Re-open `Ej_2.png` and `Ej_4.png`** to re-anchor visually.
3. **Confirm with the user** how many steps the carousel has. If they only said "make a post about X", ask: "How many steps? Each step = one slide."
4. **For each step**, draft in plain text:
   - PASO number
   - Headline (one keyword to highlight, marked with `**…**`)
   - Body subtitle if needed (or "none — visual carries it")
   - Mockup description (real screenshot? recreated UI? generated?)
5. **Show the full step breakdown to the user** before generating any image. Wait for approval. This avoids burning render cycles on the wrong copy.
6. **Render** each approved step using the HTML→Chrome headless pipeline from the base skill.
7. **Save** to `Outputs/{topic-slug}/paso_{n}_{descriptor}.png`. Keep the cover and step slides in the same `Outputs/{topic-slug}/` folder so the whole carousel lives together.
8. **Show the carousel as a sequence** (cover → paso 1 → paso 2 → …) so the user sees the flow, not isolated slides.

---

## 10. Step slide HTML scaffold

Starting template. Slot in the headline, optional subtitle, and mockup (real `<img>` or recreated HTML).

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body { width: 1080px; height: 1350px; overflow: hidden; }
  body {
    background: #F5F2ED;
    background-image:
      linear-gradient(#E8E4DD 1px, transparent 1px),
      linear-gradient(90deg, #E8E4DD 1px, transparent 1px);
    background-size: 40px 40px;
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    color: #0E0E0E;
    display: flex; flex-direction: column;
    align-items: center; justify-content: space-between;
    padding: 80px 80px 90px;
    position: relative;
  }
  .username { font-size: 26px; font-weight: 500; color: #8A8780; }
  .center-block {
    display: flex; flex-direction: column; align-items: center;
    gap: 50px; flex: 1; justify-content: center; width: 100%;
  }
  .text-stack { display: flex; flex-direction: column; align-items: center; gap: 18px; }
  .step-label {
    font-size: 24px; font-weight: 600; color: #8A8780;
    text-transform: uppercase; letter-spacing: 0.18em;
  }
  .headline {
    font-size: 56px; font-weight: 800; line-height: 1.18;
    text-align: center; max-width: 880px; letter-spacing: -0.02em;
  }
  .accent-coral { color: #E85D3C; }
  .accent-yellow {
    background: #FFE45C; padding: 4px 14px; border-radius: 8px;
    box-decoration-break: clone; -webkit-box-decoration-break: clone;
    display: inline-block; line-height: 1.05;
  }
  .subtitle {
    font-size: 28px; font-weight: 500; color: #3A3A38;
    line-height: 1.45; text-align: center; max-width: 800px;
    margin-top: 8px;
  }
  .mockup {
    background: #FFFFFF;
    border-radius: 22px;
    box-shadow:
      0 12px 40px rgba(14,14,14,0.08),
      0 30px 80px rgba(14,14,14,0.05);
    max-width: 720px;
    overflow: hidden;
  }
  .swipe { font-size: 26px; font-weight: 700; }
  .footer { display: flex; flex-direction: column; align-items: center; gap: 18px; }
  .indicator { display: flex; gap: 12px; align-items: center; }
  .dot { width: 9px; height: 9px; border-radius: 50%; background: #D5D0C8; }
  .dot.active { width: 13px; height: 13px; background: #E85D3C; }

  /* Carousel chevrons floating on the edges */
  .chev {
    position: absolute; top: 50%; transform: translateY(-50%);
    width: 44px; height: 44px; border-radius: 50%;
    background: #FFFFFF;
    box-shadow: 0 4px 12px rgba(14,14,14,0.08);
    display: flex; align-items: center; justify-content: center;
    color: #1A1A1A; font-size: 26px; font-weight: 400;
  }
  .chev.left { left: 30px; }
  .chev.right { right: 30px; }
</style>
</head>
<body>
  <div class="username">@lucianomusellaa</div>

  <div class="center-block">
    <div class="text-stack">
      <div class="step-label">Paso 1</div>
      <h1 class="headline">
        Creá un flujo on <span class="accent-coral">ManyChat</span>
      </h1>
      <!-- Optional subtitle (Variant A). Delete for Variant B. -->
      <p class="subtitle">Creá un flujo que se active cuando alguien te escribe por DM o comenta una palabra clave en cualquier post o reel.</p>
    </div>

    <div class="mockup">
      <!-- Drop a real screenshot here: <img src="../../Assets/manychat-flow.png" /> -->
      <!-- Or recreate the relevant UI fragment in HTML/CSS -->
    </div>
  </div>

  <div class="footer">
    <div class="indicator">
      <!-- Mark the dot for THIS step. Example: paso 1 → second dot active (cover is first). -->
      <div class="dot"></div>
      <div class="dot active"></div>
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
    </div>
    <div class="swipe">Desliza →</div>
  </div>

  <div class="chev left">‹</div>
  <div class="chev right">›</div>
</body>
</html>
```

---

## 11. Closing slide pattern (the LAST slide of the carousel)

The carousel doesn't end on the last step — it ends on a **closing slide** whose only job is to drive engagement: a follow, a save, a comment, or a DM. Reference: **`Inspiracion/Ej_5.png`**.

The closing slide is a **special variant of a step slide** (no `PASO X` label, no `Desliza →` footer — it's the *last* slide, there's nothing left to swipe to). It should still feel native to the carousel: same cream background, same Inter font, same palette.

### Vertical structure of a closing slide

| Order | Element | Notes |
|---|---|---|
| 1 | `@lucianomusellaa` | Top, same as every slide |
| 2 | **Mascot / icon / character** | A small playful visual at the top of the center block. ~140 px tall. Can be: an emoji-style character (the bear in Ej_5), a sparkle, the Claude Code cursor, a stylized agent icon. The mascot signals "this is the warm closer" and breaks visual monotony from the dense step slides |
| 3 | **Big primary text** | "sígueme para más." or "no te vayas todavía." or similar — 56–64 px, weight 800, lowercase for friendliness, period at the end. **NOT** all-caps |
| 4 | Thin divider line | A short horizontal `<hr>` style line, ~80 px wide, 1 px, color `#1A1A1A`. Adds editorial polish (Ej_5 has it) |
| 5 | Small label text | One word, lowercase, grey: "comenta", "guarda", "envía", "responde". 20–22 px, weight 500, color `#8A8780` |
| 6 | **CTA button / pill** | A white rounded rectangle (`border-radius: 14 px`, soft shadow) containing the **trigger word** in big bold black text. Example: `"AGENTE"`, `"SETUP"`, `"PROMPTS"`. 38–44 px, weight 800, uppercase. The trigger word is what the viewer is asked to comment/DM. This is the conversion driver — keep it ONE word, memorable, all caps |
| 7 | Caption below the CTA | Small line explaining what they get. 20–22 px, weight 500, grey. "y te envío la guía completa" / "para recibir el setup" |

### Closing slide rules

- **No `Desliza →` at the bottom** (this is the end of the carousel)
- **No `PASO X` label** (this is not a step)
- **The trigger word in the CTA pill is ONE word, all caps, memorable** — viewers will literally type it in the comments. Hard to type = no comments.
- **First-person, conversational** in the caption: "te envío", "te paso", "te mando" — feel like a DM
- The mascot/icon at the top is critical for the *vibe shift* from instructional → personal. Don't skip it. If you don't have a real mascot, use a sparkle, a cursor, a Claude logo, or a hand-drawn-style SVG of an agent character.

### Closing slide good copy examples (Colombian Spanish)

- "sígueme para más." → comenta → `"AGENTE"` → "y te envío el setup completo"
- "¿quieres armar el tuyo?" → comenta → `"PROMPTS"` → "y te paso mis prompts"
- "no te vayas todavía." → comenta → `"SISTEMA"` → "y te mando la guía"
- "guarda este post." → para que → `"VOLVER"` → "cuando lo necesites"

### Closing slide HTML scaffold

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body { width: 1080px; height: 1350px; overflow: hidden; }
  body {
    background: #F5F2ED;
    background-image:
      linear-gradient(#E8E4DD 1px, transparent 1px),
      linear-gradient(90deg, #E8E4DD 1px, transparent 1px);
    background-size: 40px 40px;
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    color: #0E0E0E;
    display: flex; flex-direction: column;
    align-items: center; justify-content: space-between;
    padding: 80px 80px 90px;
  }
  .username { font-size: 26px; font-weight: 500; color: #8A8780; }
  .center-block {
    display: flex; flex-direction: column; align-items: center;
    gap: 26px; flex: 1; justify-content: center; width: 100%;
  }
  .mascot { width: 160px; height: 160px; }
  .big-text {
    font-size: 60px; font-weight: 800; line-height: 1.05;
    text-align: center; letter-spacing: -0.025em;
    margin-top: 12px;
  }
  .divider {
    width: 80px; height: 1.5px; background: #1A1A1A;
    margin: 6px 0;
  }
  .label {
    font-size: 22px; font-weight: 500; color: #8A8780;
  }
  .cta-pill {
    background: #FFFFFF;
    border-radius: 16px;
    padding: 22px 56px;
    font-size: 42px; font-weight: 800;
    color: #0E0E0E;
    letter-spacing: 0.02em;
    box-shadow:
      0 12px 32px rgba(14,14,14,0.10),
      0 24px 60px rgba(14,14,14,0.06);
  }
  .caption {
    font-size: 22px; font-weight: 500; color: #8A8780;
    margin-top: 4px;
  }
  .indicator {
    display: flex; gap: 12px; align-items: center;
    margin-top: 18px;
  }
  .dot { width: 9px; height: 9px; border-radius: 50%; background: #D5D0C8; }
  .dot.active { width: 13px; height: 13px; background: #E85D3C; }
</style>
</head>
<body>
  <div class="username">@lucianomusellaa</div>
  <div class="center-block">
    <!-- mascot SVG or img -->
    <div class="mascot"><!-- SVG character / sparkle / icon --></div>
    <div class="big-text">sígueme para más.</div>
    <div class="divider"></div>
    <div class="label">comenta</div>
    <div class="cta-pill">"AGENTE"</div>
    <div class="caption">y te envío el setup completo</div>
    <!-- Slide indicator: closing is the LAST slide → last dot active. -->
    <div class="indicator">
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot active"></div>
    </div>
  </div>
  <!-- intentionally no .swipe footer -->
</body>
</html>
```

---

## 12. Step slide checklist (run before exporting each step)

- [ ] `@lucianomusellaa` at top
- [ ] **`PASO {N}`** label present, uppercase, tracked, grey
- [ ] Headline is 4–8 words, 1–2 lines
- [ ] **Single** keyword highlighted (coral text or yellow marker — never both)
- [ ] Subtitle present only if needed; max 2 lines
- [ ] UI mockup centered, white background, rounded corners, soft shadow, NOT tilted
- [ ] Carousel chevrons on left + right edges (recommended)
- [ ] `Desliza →` at bottom
- [ ] Saved to `Outputs/{topic-slug}/paso_{n}_{descriptor}.png` (same folder as the cover)
- [ ] Step number is correct in sequence (no skipped numbers)
- [ ] All step slides in the carousel use the same headline font-size for visual consistency
