---
name: instagram-cover-design
description: Design the COVER / thumbnail / first slide of an Instagram carousel post — the slide that has to stop the scroll. Use whenever the user asks for a cover, thumbnail, hero image, portada, or "the first slide" of a carousel about a tool/topic. Extends instagram-post-design (the base visual system).
type: skill
---

# Instagram Cover Design Skill

This skill defines how to design **cover slides** — the *first* slide of a carousel that has one job: **stop the scroll**. It extends [instagram-post-design.md](instagram-post-design.md), which owns the shared visual system (canvas, palette, fonts, render pipeline). Read that skill first, then this one.

Reference covers from [Ejemplos/](../Ejemplos/):
- **`Ej_.png`** → cover with two logos connected (this is the layout the user explicitly chose)
- **`Ej_1.png`** → cover with screenshot/UI mockup
- **`Ej_3.png`** → cover with phone/UI screenshot

Always re-open at least `Ej_.png` and one other before designing a cover, to re-anchor visually.

---

## 1. The cover's only job

A cover must do **one** thing: make someone stop scrolling. Everything else (clarity, beauty, brand) is secondary to that. The user's stated goal is "extremely catchy at first glance". Optimize ruthlessly for the **first 0.5 seconds** of viewing.

This means:
- The headline must be readable from a thumbnail (sized down to ~150 px wide in the feed grid)
- The visual must communicate the topic *without* reading the headline
- The accent colors must create immediate contrast against the cream background

---

## 2. CRITICAL — Highlight rule for covers (user-confirmed default)

> **Covers DEFAULT to the double-highlight pattern.**

Paint **two** keywords from the headline using **both** accent colors at the same time:
- One keyword in **coral text** `#E85D3C`
- The other keyword on a **yellow marker** background `#FFE45C` (rounded rect, 8 px radius, padding 4 px / 16 px)

This is the inverse of the general rule in the base skill (which says "two accent colors only on rare covers"). For *this* user, double-highlight on covers is the **standard**, not the exception. Confirmed in feedback after they reviewed 5 cover variants and chose `v5_double` over the single-highlight options.

**Single-highlight covers** (just one keyword in coral, or just one on yellow) are still allowed when:
- The headline only contains *one* keyword that matters (e.g. one product name and a generic verb)
- The user explicitly asks for a "cleaner" or "simpler" cover
- A/B-style variations to compare against the double-highlight default

When single-highlight: default to **coral text** unless the keyword is short and benefits from the yellow marker (1 word, 4–8 chars).

---

## 3. Cover layout patterns

### Layout A — Two logos connected (the default for "X + Y" topics)
*Reference: `Ej_.png`. This is what the user picked for the first test post.*

Use this whenever the cover topic is about **combining two tools / products / concepts** — anything with the structure "X with Y", "X + Y", "from X to Y".

**Vertical structure (top → bottom):**
1. `@lucianomusellaa` (top, ~80 px from top edge)
2. Big space (`gap: 110px`)
3. **Headline** — 2–3 lines, double-highlight (one keyword coral, the other on yellow marker), font-size 60–68 px, max-width 920 px
4. Big space
5. **Logo row**: `[white circle bubble with logo A] — [horizontal line + link icon] — [coral circle bubble with logo B]`
   - Bubbles: 180 × 180 px, perfect circles
   - Left bubble: white background `#FFFFFF`, soft shadow `0 14px 40px rgba(14,14,14,0.10)`, contains the brand logo of the "input" tool (usually black/dark on white)
   - Right bubble: coral fill `#E85D3C`, contains a white logo or icon for the "output" / AI tool
   - Connector: 120 × 2.5 px solid line `#1A1A1A`, with a 44 px white circle in the middle containing a small black **link/chain icon** (inline SVG, 22 px, stroke 2.4)
6. `Deslizá →` (bottom, ~90 px from bottom edge)

### Layout B — Screenshot / UI mockup
*Reference: `Ej_1.png`, `Ej_3.png`*

Use this when the cover topic is about **a single tool, dashboard, ad campaign, or screenshot-able thing** (not a combination).

**Vertical structure:**
1. `@lucianomusellaa` (top)
2. **Headline** (upper third, double-highlight as above, can be slightly smaller — 56–62 px — to leave room for the mockup)
3. **Mockup**: a real screenshot or generated UI
   - Border-radius: 18–24 px
   - Soft drop shadow: `0 12px 40px rgba(14,14,14,0.08)` plus an outer `0 30px 80px rgba(14,14,14,0.06)` for depth
   - Slight rotation (-2° to +2°) for energy — optional, used when the headline is very straight
   - Optional: a coral burst/sparkle icon floating at one corner (top-right or bottom-left) at ~80 px size, as a visual accent
   - Max width: ~720 px so it doesn't dominate
4. `Deslizá →` (bottom)

### Layout C — Pure typographic cover (no visual)
*No direct reference in `Ejemplos/` — use sparingly when the headline itself IS the hook.*

Use only when the message is so strong it doesn't need a visual (e.g. a controversial claim, a number, a one-liner). Ex: "**$100k/mes con un solo flujo de ManyChat.**"

**Vertical structure:**
1. `@lucianomusellaa`
2. Massive headline dead center, 80–96 px, 2–3 lines, double-highlight
3. `Deslizá →`

---

## 4. Headline writing rules for covers

Covers have stricter headline rules than step slides (steps can be more verbose because the user is already engaged).

| Rule | Cover |
|---|---|
| Word count | **5–10 words max** (ideally 6–8) |
| Line count | 2–3 lines |
| Font size | 60–76 px (Layout C goes up to 96 px) |
| Highlighted words | **2 keywords** (double-highlight default) |
| Tone | **Colombian Spanish, `tú` form** ("Agenda", "Usa", "Crea", "Arma") — NEVER Argentinian voseo. See section 3.5 of the base skill. |
| Punctuation | Question marks (`¿…?`) and dots are great. Avoid exclamation marks (cheap). |
| Forbidden | Emojis in the headline. Generic verbs like "aprende" (use "agenda", "configura", "arma"). Argentinian voseo (creá, usá, definí). |

**Question vs statement:** Both work. Questions feel more conversational and pull the eye ("¿Cómo agendar…?"). Statements feel more authoritative ("Agendá llamadas con…"). Default to **question form** unless the topic is a bold claim or a number — then statement.

**Keywords to highlight:** always pick the *two most concrete nouns* in the headline. Tool names (Claude, ManyChat, Gemini, Notion), numbers ($100k, 10x, 2 horas), or strong verbs (TRÁFICO, VENTAS) — never abstract words like "ventas" or "estrategia".

---

## 5. Cover-specific anti-patterns

In addition to the base skill's anti-patterns:

- ❌ Three or more highlighted keywords (visual noise — pick the 2 most important)
- ❌ Logos without circular bubbles (looks unfinished)
- ❌ Bubbles without the connector line (loses the "combination" metaphor)
- ❌ Bubbles bigger than the headline visually (the headline must dominate)
- ❌ More than one line of body text below the headline (covers don't carry body text — that's for step slides)
- ❌ "PASO X" labels on covers (those belong on step slides)
- ❌ Headlines > 10 words (won't be readable in the feed thumbnail)
- ❌ Tilted headlines (only the mockup can tilt slightly, never text)

---

## 6. Workflow when building a cover

1. **Re-read the base skill** [instagram-post-design.md](instagram-post-design.md) for the visual system + render pipeline.
2. **Re-open `Ej_.png`** (and `Ej_1.png` if a mockup-style cover is needed).
3. **Confirm the topic and the two highlight keywords** with the user. If they didn't specify keywords, propose 2 options and let them pick before generating.
4. **Decide the layout**: A (two logos) is the default for "X + Y" topics; B (mockup) for single-tool topics; C (typographic) for bold claims.
5. **Generate 3–5 cover variations** in `Outputs/{topic-slug}/` so the user can compare. Vary by:
   - Headline phrasing (question vs statement, short vs long)
   - Which word gets coral vs yellow
   - Layout (A vs B if both fit)
6. **Render** each variation to PNG using the HTML→Chrome headless pipeline from the base skill. Save as `cover_v{n}_{descriptor}.png`.
7. **Show all variations** and ask for feedback. Iterate on the chosen one.

---

## 7. Cover-specific HTML scaffold

Starting template for **Layout A** (the default). Layout B and C are derivatives — adjust the `.center-block` contents.

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700;800;900&display=swap" rel="stylesheet">
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
    gap: 100px; flex: 1; justify-content: center; width: 100%;
  }
  .headline {
    font-size: 64px; font-weight: 800; line-height: 1.25;
    text-align: center; max-width: 920px; letter-spacing: -0.02em;
  }
  .accent-coral { color: #E85D3C; }
  .accent-yellow {
    background: #FFE45C; padding: 4px 16px; border-radius: 8px;
    box-decoration-break: clone; -webkit-box-decoration-break: clone;
    display: inline-block; line-height: 1.05;
  }
  .swipe { font-size: 26px; font-weight: 700; }
  .footer { display: flex; flex-direction: column; align-items: center; gap: 18px; }
  .indicator { display: flex; gap: 12px; align-items: center; }
  .dot { width: 9px; height: 9px; border-radius: 50%; background: #D5D0C8; }
  .dot.active { width: 13px; height: 13px; background: #E85D3C; }

  .logo-row { display: flex; align-items: center; gap: 0; }
  .logo-bubble {
    width: 180px; height: 180px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
  }
  .logo-bubble.white { background: #FFFFFF; box-shadow: 0 14px 40px rgba(14,14,14,0.10); }
  .logo-bubble.coral { background: #E85D3C; }
  .connector {
    width: 120px; height: 2.5px; background: #1A1A1A;
    position: relative; flex-shrink: 0;
  }
  .link-icon {
    position: absolute; left: 50%; top: 50%;
    transform: translate(-50%, -50%);
    width: 44px; height: 44px; border-radius: 50%;
    background: #FFFFFF; border: 2px solid #1A1A1A;
    display: flex; align-items: center; justify-content: center;
  }
</style>
</head>
<body>
  <div class="username">@lucianomusellaa</div>
  <div class="center-block">
    <h1 class="headline">
      <!-- HEADLINE: 2–3 lines. Double-highlight by default. Example: -->
      ¿Cómo agendar llamadas<br>de venta con
      <span class="accent-coral">Claude</span> y
      <span class="accent-yellow">ManyChat</span>?
    </h1>
    <div class="logo-row">
      <div class="logo-bubble white">
        <!-- LEFT LOGO: brand A -->
      </div>
      <div class="connector">
        <div class="link-icon">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#1A1A1A" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
            <path d="M10 13a5 5 0 0 0 7.07 0l3-3a5 5 0 0 0-7.07-7.07l-1.5 1.5"/>
            <path d="M14 11a5 5 0 0 0-7.07 0l-3 3a5 5 0 0 0 7.07 7.07l1.5-1.5"/>
          </svg>
        </div>
      </div>
      <div class="logo-bubble coral">
        <!-- RIGHT LOGO: brand B (white-on-coral) -->
      </div>
    </div>
  </div>
  <div class="footer">
    <div class="indicator">
      <!-- The cover is always slide 1 → first dot active. Add ONE dot per slide in the carousel. -->
      <div class="dot active"></div>
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
    </div>
    <div class="swipe">Desliza →</div>
  </div>
</body>
</html>
```

---

## 8. Cover checklist (run before exporting)

- [ ] `@lucianomusellaa` at top (NOT @ramiro.cubria — common mistake)
- [ ] Headline is 5–10 words, 2–3 lines
- [ ] **Two** keywords highlighted: one coral, one on yellow (the user's confirmed default)
- [ ] Logos in circular bubbles, white-left + coral-right, with link-icon connector
- [ ] No "PASO" label (that's for step slides)
- [ ] No body text below the headline
- [ ] `Deslizá →` at bottom
- [ ] Saved to `Outputs/{topic-slug}/cover_v{n}_{descriptor}.png`
- [ ] Generated 3–5 variations for the user to compare, not just 1
