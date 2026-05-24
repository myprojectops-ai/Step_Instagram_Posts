---
name: instagram-cover-design
description: Design the COVER / first slide of a step-by-step Instagram carousel -- the slide that has to stop the scroll. Use whenever the user asks for a cover, thumbnail, portada, or first slide of a tutorial. Extends instagram-post-design (the base) and Brand/brand-spec.md (the canonical visual system).
type: skill
---

# Step-by-Step Cover Design

This skill defines how to design **tutorial cover slides** -- the first slide of a carousel that has one job: **stop the scroll**. It extends [instagram-post-design.md](instagram-post-design.md) and [Brand/brand-spec.md](../../../Brand/brand-spec.md).

**Always open at least 2 reference templates from `Brand/Templates/Tutorial/{COLOR}/{STYLE}/{MODE}/` before designing a cover.** These are the canonical visual ground truth.

---

## 1. The cover's only job

A cover must do **one** thing: make someone stop scrolling. Optimize ruthlessly for the **first 0.5 seconds** of viewing.

This means:
- The headline must be readable from a thumbnail (~150 px wide in the feed grid)
- The visual hook must communicate the topic *without* reading the headline
- The italic emphasis word must create immediate editorial contrast

---

## 2. Cover headline rule (canonical pattern from templates)

Tutorial covers use **single Playfair Italic emphasis** -- one keyword from the headline rendered in italic serif in the scheme's highlight color. This is the new "double highlight" replacement: a single italic-serif accent word adds editorial character vs. surrounding Roboto Bold.

| Property | Value |
|---|---|
| Headline word count | 5-10 words (ideally 6-8) |
| Lines | 2-3 |
| Font size | 72-80 px (smaller for longer headlines) |
| Emphasis | **1 word** in Playfair Display Italic in scheme highlight color (e.g. `#ffb050` for AMARILLO) |
| Tone | Colombian Spanish, `tú` form -- "Crea", "Configura", "Arma", "Agenda" |

**Keywords to italicize:** always the *most concrete noun*. Tool names (`Claude Code`, `Subagentes`, `MCPs`), product names, or strong concept nouns (`tu agente`, `el cerebro`). Never abstract words like "estrategia" or "ventas".

**Optional pill below the headline:** "en X pasos" in a solid-fill rectangle using the scheme's `solid` token (e.g. `#ff9d00` for AMARILLO) with white text in Roboto Medium. Use only when the carousel has a clear step count and the user wants to advertise it on the cover.

---

## 3. Cover layout pattern (from templates)

The canonical tutorial cover layout (templates `Brand/Templates/Tutorial/AMARILLO/PLANO/LIGHT_DARK/*-14.png`, etc.):

```
┌─ 1080 × 1350 ────────────────────────────────────────┐
│                                                       │
│                   @lucianomusellaa                    │ ← scheme highlight color, top center
│                                                       │
│                                                       │
│              Crea tu propio                           │ ← Roboto Bold 72-80px
│              agente de IA con                         │
│              ┌────────────┐                           │
│              │ Claude Code│                           │ ← Playfair Italic, scheme highlight color
│              └────────────┘                           │
│                                                       │
│             ┌─────────────────────────┐               │
│             │ █████  en 4 pasos       │               │ ← solid color pill, white text
│             └─────────────────────────┘               │
│                                                       │
│         [terminal mockup, illustration,               │ ← visual hook (chooses per topic)
│          orgchart, or other concept-relevant]         │
│                                                       │
│             ╭──────────────╮                          │
│             │   Desliza    │                          │ ← outline pill, text-primary color
│             ╰──────────────╯                          │
└───────────────────────────────────────────────────────┘
```

### Variations within the pattern

- **Terminal mockup hook** -- macOS-style window with 3 dots, prompt + cursor (the cursor accent in scheme highlight color). Default for Claude Code / dev tutorials.
- **Illustration hook** -- minimalist SVG illustration of the concept (an agent character, a brain network, etc.). For more abstract tutorials.
- **Orgchart hook** -- cards in a tree structure for "agent + subagents" tutorials. See template `Brand/Templates/Tutorial/AMARILLO/PLANO/LIGHT_DARK/*-18.png`.
- **Screenshot hook** -- a real UI screenshot when the tutorial is about configuring something specific.

The visual hook should occupy the bottom-center ~40-50% of the canvas (after headline + pill).

### Backgrounds per mode

- **LIGHT (PLANO):** flat cream `#efedec`
- **DARK (PLANO):** flat warm-dark `#11191b`
- **LIGHT GRADIENT (LIGHT DARK or DARK LIGHT):** linear gradient from cream top to soft gray-blue bottom OR vice versa
- **DARK GRADIENT:** black top → navy `#00386e` bottom (or vice versa)

The user's chosen template subfolder dictates which background variant. When in doubt, default to PLANO.

---

## 4. Cover-specific anti-patterns

In addition to anti-patterns from the base skill:

- ❌ Two or more italic emphasis words (this is the single-emphasis rule -- 1 word only)
- ❌ Headlines > 10 words (won't be readable in the feed thumbnail)
- ❌ Tilted headlines or visual hooks (covers must be straight)
- ❌ Logos without the visual-hook structure (logos float without context = unfinished)
- ❌ "PASO X" eyebrow on a cover (eyebrows are for step slides)
- ❌ More than one solid pill on a cover ("en 4 pasos" only -- never stack pills)
- ❌ Multi-line pill text -- the pill is always ONE short phrase

---

## 5. Workflow when building a cover

1. **Read the base skill** [instagram-post-design.md](instagram-post-design.md) for fonts, scaffolds, Colombian Spanish rules.
2. **Read brand-spec.md** for palette tokens for the chosen scheme + mode.
3. **Open at least 2 reference covers** from the user's chosen template subfolder.
4. **Confirm the topic and the italic emphasis word** with the user. If they didn't specify, propose the strongest option in the breakdown step.
5. **Generate 2-3 cover variations** in `Outputs/{topic-slug}/` so the user can compare. Vary by:
   - Headline phrasing (question vs statement, short vs long)
   - Which word gets the italic emphasis
   - Visual hook (terminal vs illustration vs orgchart)
   - Pill present vs absent
6. **Render** each via `render.sh`. Save as `cover_v{n}_{descriptor}.html`/`.png`.
7. **Visual QA** every PNG.
8. **Show all variations** and ask for the user's pick.

---

## 6. Cover HTML scaffold (Tutorial Layout, LIGHT + AMARILLO -- adapt tokens per mode/scheme)

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
  /* @font-face block from brand-spec -- see instagram-post-design.md §7 */
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
    align-items: center; justify-content: space-between;
    padding: 80px 80px 90px;
  }
  .handle { color: #ffb050; font-size: 22px; font-weight: 500; letter-spacing: 0.5px; }
  .center-block { display: flex; flex-direction: column; align-items: center; gap: 60px; flex: 1; justify-content: center; width: 100%; }
  .text-stack { display: flex; flex-direction: column; align-items: center; gap: 50px; }
  .headline {
    font-size: 76px; font-weight: 700; line-height: 1.08;
    text-align: center; max-width: 900px; letter-spacing: -0.02em;
  }
  .emphasis { font-family: 'Playfair Display'; font-style: italic; font-weight: 400; color: #ffb050; }
  .pill-solid {
    background: #ff9d00; color: #ffffff;
    padding: 22px 56px;
    font-size: 48px; font-weight: 500;
    border-radius: 4px;
  }
  .hook { /* visual hook container -- terminal mockup, illustration, etc. */
    max-width: 920px; width: 100%;
  }
  .swipe-pill {
    border: 2px solid #0c1314; color: #0c1314;
    padding: 14px 56px;
    font-size: 28px; font-weight: 500;
    border-radius: 999px;
    background: transparent;
  }
  /* Terminal mockup style (example visual hook) */
  .terminal {
    background: #0c1314; border-radius: 12px; overflow: hidden;
    box-shadow: 0 12px 40px rgba(0,0,0,0.08);
  }
  .terminal-bar { background: #1a2225; padding: 14px 18px; display: flex; align-items: center; gap: 8px; }
  .terminal-dot { width: 12px; height: 12px; border-radius: 50%; }
  .terminal-dot.r { background: #ff6058; } .terminal-dot.y { background: #ffbe2e; } .terminal-dot.g { background: #28c93f; }
  .terminal-title { color: #8a9499; font-size: 14px; flex: 1; text-align: center; font-family: ui-monospace, Menlo, monospace; }
  .terminal-body { padding: 32px 36px; font-family: ui-monospace, Menlo, monospace; color: #efedec; font-size: 22px; line-height: 1.8; }
  .terminal-prompt { color: #ffb050; }
  .terminal-cursor { display: inline-block; width: 12px; height: 22px; background: #ffb050; vertical-align: middle; margin-left: 4px; }
</style>
</head>
<body>
  <div class="handle">@lucianomusellaa</div>
  <div class="center-block">
    <div class="text-stack">
      <h1 class="headline">Crea tu propio<br>agente de IA con<br><span class="emphasis">Claude Code</span></h1>
      <div class="pill-solid">en 4 pasos</div>
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
          ~/mi-agente <span class="terminal-prompt">$</span> claude<span class="terminal-cursor"></span>
        </div>
      </div>
    </div>
  </div>
  <div class="swipe-pill">Desliza</div>
</body>
</html>
```

### Adapting to other schemes/modes

- **ROJO scheme:** swap `#ffb050` → `#e60000`, `#ff9d00` → `#c30000` in `.handle`, `.emphasis`, `.pill-solid`, terminal accents.
- **AZUL scheme:** `#ffb050` → `#0056a6`, `#ff9d00` → `#00386e`.
- **DARK mode:** body `background: #11191b`, `color: #ffffff`, `.swipe-pill { border-color: #ffffff; color: #ffffff; }`. Terminal stays dark (no change).
- **GRADIENT background:** replace `background: #efedec` with `background: linear-gradient(to bottom, #efedec 0%, #00386e 100%);` (or per template variant).

---

## 7. Cover checklist (run before exporting)

- [ ] `@lucianomusellaa` at top in scheme highlight color (NOT @ramiro.cubria)
- [ ] Headline is 5-10 words, 2-3 lines
- [ ] **Exactly 1 word** in Playfair Italic emphasis in scheme highlight color
- [ ] Solid pill (optional) uses scheme `solid` token with white Roboto Medium text
- [ ] Visual hook present (terminal / illustration / orgchart / screenshot)
- [ ] "Desliza" outline pill at bottom
- [ ] No "PASO X" eyebrow (that's step slides only)
- [ ] No page dots (IG adds them natively)
- [ ] Background matches chosen mode (LIGHT or DARK + style variant)
- [ ] Colombian Spanish (no `creá`, `usá`, `vos`, etc.)
- [ ] Saved to `Outputs/{topic-slug}/cover_v{n}_{descriptor}.png`
- [ ] Generated 2-3 variations for the user to compare
