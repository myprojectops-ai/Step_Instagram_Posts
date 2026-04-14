---
name: instagram-dark-mode
description: Convert any step-by-step post (cover, step slides, closing slide) to a dark-mode variant — same visual identity, same layouts, same typography, only the contrast palette is inverted. Use ONLY when the user explicitly asks for "modo oscuro", "dark mode", or asks to flip an existing post to dark. Default is always light mode (cream).
type: skill
---

# Instagram Dark Mode Skill

This skill defines how to render the **dark mode variant** of any step-by-step post. It is **opt-in only** — the project default is the warm cream light mode defined in [instagram-post-design.md](instagram-post-design.md). Dark mode is used **only** when the user explicitly says so.

Think of this like switching your phone to dark mode: nothing about the layout, hierarchy, spacing, fonts, or copy changes. The eye lands on the same elements in the same order. Only the **contrast palette** flips — what was warm-cream-on-dark-text becomes warm-dark-on-cream-text — so the post still feels native to the brand even though the background is dark.

---

## 1. When to use this skill

**ONLY when the user explicitly triggers dark mode.** Phrases like:
- "haz este post en modo oscuro"
- "convierte este post a modo oscuro"
- "pasa este post a modo oscuro"
- "el siguiente post en modo oscuro"
- "dark mode"
- "modo oscuro"
- "quiero la versión dark"

If the user does NOT say one of these (or similar), **always default to light mode** — never volunteer dark mode unprompted, never ask "¿lo quieres claro u oscuro?" The user prefers light by default and will tell me when they want dark.

### Two scenarios

**Scenario A — Convert an existing post.** The user has an existing light-mode post in `Outputs/{topic-slug}/` and wants a dark version. Create a sibling folder `Outputs/{topic-slug}-dark/` with the dark variants. Never overwrite the original light version.

**Scenario B — Generate a new post directly in dark mode.** Same workflow as a normal step-by-step post (read README, ask post type, re-anchor, propose breakdown, render), but every slide is built with the dark palette from the start. Save it under `Outputs/{topic-slug}-dark/` so the suffix flags the variant.

---

## 2. Color mapping (light → dark)

This is the **single source of truth**. Every color used in the light skill has exactly one dark counterpart. Don't invent intermediate values.

| Role | Light value | Dark value | Notes |
|---|---|---|---|
| Slide background | `#F5F2ED` (cream) | `#17140F` (warm dark, NOT pure black) | Stays warm — dark brown-black, never `#000000` |
| Background grid lines | `#E8E4DD` | `#26221C` | Subtle warm-dark grid, same 40px spacing |
| Primary text | `#0E0E0E` | `#F5F2ED` | The light mode background color *becomes* the dark mode text — perfect inversion |
| Subtitle / body text | `#3A3A38` | `#C8C5BD` | Soft warm off-white |
| Secondary (username, labels, "PASO X") | `#8A8780` | `#9F9C94` | Slightly lighter to maintain readability |
| **Accent coral** | `#E85D3C` | `#E85D3C` | **Unchanged** — vibrant on both backgrounds. The only color that stays identical. |
| **Highlight yellow** | `#FFE45C` | `#FFE45C` | **Unchanged** — pops even harder against dark, looks beautiful |
| Mockup card surface | `#FFFFFF` | `#252220` | The "raised panel" color — sits *above* the slide background |
| Mockup card header strip | `#F8F6F2` | `#2D2A24` | Slightly lighter than the panel for the file/header strip |
| Mockup card text | `#0E0E0E` | `#F5F2ED` | Same inversion as primary text |
| Mockup borders / dividers | `#E8E4DD`, `#F0EDE8` | `#332F28` | Warm dark divider |
| Form input backgrounds (inside mockups) | `#F5F2ED` | `#1A1612` | The slide background color reused inside the card creates a "sunken input" look |
| Soft shadows on cards | `0 12px 40px rgba(14,14,14,0.08)` plus outer | **Removed** OR replaced with `1px solid rgba(245,242,237,0.08)` + optional `0 0 60px rgba(232,93,60,0.06)` glow | Dark mode rarely needs shadows — contrast comes from the background. A thin warm-white border or a subtle coral glow is enough |
| Slide indicator inactive dot | `#D5D0C8` | `#3F3B34` | Same role: muted, visible but quiet |
| Slide indicator active dot | `#E85D3C` | `#E85D3C` | Unchanged |
| Connector line / chevron icons | `#1A1A1A` | `#F5F2ED` | Inverted with the text |
| Cierre CTA pill background | `#FFFFFF` | `#252220` | Same as mockup card |
| Cierre CTA pill text | `#0E0E0E` | `#F5F2ED` | Inverted |
| Carousel chevron circles (left/right edges) | `#FFFFFF` with `#1A1A1A` arrow | `#252220` with `#F5F2ED` arrow | Match the mockup card surface |

### Things that stay the same (NEVER change in dark mode)

- The two accent colors: **coral `#E85D3C` and yellow `#FFE45C`** stay identical. They're brand identity, not mode-dependent. Yellow especially looks stunning on warm dark — that contrast is part of the appeal.
- All sizing, spacing, margins, padding, font sizes, font weights, line heights
- The double-highlight rule on covers and single-highlight rule on step slides
- The slide indicator structure
- The closing slide structure
- The Colombian Spanish copy
- The `@lucianomusellaa` username

---

## 3. Conversion workflow (Scenario A: existing post → dark)

### Step 1 — Read the original folder
List `Outputs/{topic-slug}/` and read every `.html` file. Identify which slides exist (cover variants, pasos, cierre).

### Step 2 — Create the dark output folder
```bash
mkdir -p "PostTypes/step-by-step/Outputs/{topic-slug}-dark"
```
The `-dark` suffix is non-negotiable — it makes the variant immediately recognizable in the file tree and prevents collisions with the light original.

### Step 3 — Duplicate each HTML and apply the color mapping
For each `.html` in the original folder:
1. Read it
2. Apply the color mapping from section 2 systematically (background, text, mockup colors, shadows, dots, chevrons, CTA pill)
3. Write the new version to `Outputs/{topic-slug}-dark/{original_filename}.html`
4. **Do not change anything except colors and shadow declarations.** Layout, spacing, copy, SVG paths, mockup structure — everything else is byte-for-byte identical.

**Tip:** if the original file has hex codes inlined throughout the `<style>` block, doing find-and-replace per color is the safest approach. Walk through the color mapping table top to bottom and replace each light value with its dark counterpart in the new file.

### Step 4 — Special handling for terminal mockups
Terminal blocks were already dark in light mode (`#1A1A1A` background, `#2A2A2A` bar). In dark mode they would visually blend with the new slide background. **Lift them above the slide background** by changing:
- Terminal background `#1A1A1A` → `#0E0C09` (slightly *darker* than the slide background `#17140F`, so the terminal sinks slightly and reads as a distinct surface)
- Terminal bar `#2A2A2A` → `#1F1B16`
- OR alternatively: keep terminal at `#1A1A1A` but add a thin coral border `1px solid rgba(232,93,60,0.15)` to separate it visually

Pick one approach per post and use it consistently across all terminal mockups in the same post.

### Step 5 — Special handling for code snippet cards
Code snippets that were rendered on white `#FFFFFF` cards (like `paso_2_crea_agente.html` with the Python SDK) need their syntax highlighting tokens reviewed:
- Keep coral `#E85D3C` for keywords (great on dark)
- Keep yellow `#FFE45C` if used
- Green strings `#2D8A2D` → brighten to `#7FD17F` for dark
- Blue properties `#2D5A8A` → brighten to `#7FB3D9`
- Purple variables `#5A2D8A` → brighten to `#B985E0`
- Comment grey `#8A8780` → keep or lighten to `#9F9C94`
- Line numbers grey `#D5D0C8` → `#3F3B34`
- "Default text" `#0E0E0E` → `#F5F2ED`

**Rule of thumb:** if the syntax color was a *dim* version intended to read on white, brighten it. If it was already vibrant (coral, yellow), keep it.

### Step 6 — Render and verify
```bash
./render.sh PostTypes/step-by-step/Outputs/{topic-slug}-dark
```
Then read each rendered PNG visually and check:
- Background is warm dark, not pure black
- Text is warm cream, fully readable, no contrast issues
- Coral and yellow accents pop even harder than in light mode
- Mockups read as raised panels above the slide
- Slide indicator dots are visible
- Carousel chevrons aren't lost against the dark background
- Nothing accidentally stayed light (orphan white shadows, white borders, etc.)

### Step 7 — Present both versions side by side
Show the user the dark variant slide-by-slide. Optionally pair each dark slide with its light original so they can compare. Then ask the standard favorites question (still applies to dark posts — the favorites folder is shared with light mode).

---

## 4. New post directly in dark mode (Scenario B)

Follow the normal step-by-step workflow from [`../README.md`](../README.md), but:

- In Step 1 (re-anchor), additionally read this skill
- In Step 5, name the folder with the `-dark` suffix from the start: `Outputs/{topic-slug}-dark/`
- In Step 6, when writing each HTML, use the dark scaffold (section 6 below) instead of the light scaffolds in the other 3 skills
- All other rules (highlight rules, slide indicator, Colombian Spanish, mandatory mockups on step slides, closing slide structure) stay identical

---

## 5. Dark mode anti-patterns

In addition to all anti-patterns from the light skills:

- ❌ Pure black background `#000000` — kills the warmth, feels generic. Always warm dark `#17140F`.
- ❌ Pure white text `#FFFFFF` — too harsh. Use the warm cream `#F5F2ED` (the same value as the light mode background).
- ❌ Bright neon accent colors — coral and yellow are already vibrant. Don't push them brighter for "extra pop on dark".
- ❌ Heavy drop shadows — dark mode rarely needs them. If a card needs separation, use a thin warm-white border or a subtle coral glow.
- ❌ Forgetting the grid — the subtle grid still exists in dark mode (`#26221C`), it's just darker. Don't drop it.
- ❌ Mixing light and dark slides in the same carousel — a post is either fully light or fully dark, never half-and-half.
- ❌ Saving dark variants into the same folder as the light original — always use the `-dark` folder suffix.
- ❌ Changing copy or layout when converting — dark mode is a *visual* variant. Touching text or spacing means I'm doing something other than dark mode.

---

## 6. Dark mode HTML scaffold

Use this as the starting point for any dark mode slide. Adjust per slide type (cover / step / closing) using the same logic the light skills use — the only difference is the palette.

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
    background: #17140F;
    background-image:
      linear-gradient(#26221C 1px, transparent 1px),
      linear-gradient(90deg, #26221C 1px, transparent 1px);
    background-size: 40px 40px;
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    color: #F5F2ED;
    display: flex; flex-direction: column;
    align-items: center; justify-content: space-between;
    padding: 80px 80px 90px;
    position: relative;
  }
  .username { font-size: 26px; font-weight: 500; color: #9F9C94; }
  .center-block {
    display: flex; flex-direction: column; align-items: center;
    gap: 50px; flex: 1; justify-content: center; width: 100%;
  }
  .text-stack { display: flex; flex-direction: column; align-items: center; gap: 18px; }
  .step-label {
    font-size: 24px; font-weight: 600; color: #9F9C94;
    text-transform: uppercase; letter-spacing: 0.18em;
  }
  .headline {
    font-size: 56px; font-weight: 800; line-height: 1.18;
    text-align: center; max-width: 880px; letter-spacing: -0.02em;
    color: #F5F2ED;
  }
  /* Accent colors stay identical to light mode */
  .accent-coral { color: #E85D3C; }
  .accent-yellow {
    background: #FFE45C; padding: 4px 14px; border-radius: 8px;
    color: #0E0E0E; /* the yellow marker text stays dark — yellow needs dark text on top, not white */
    box-decoration-break: clone; -webkit-box-decoration-break: clone;
    display: inline-block; line-height: 1.05;
  }
  .subtitle {
    font-size: 28px; font-weight: 500; color: #C8C5BD;
    line-height: 1.45; text-align: center; max-width: 800px;
  }
  /* Mockup card — raised dark panel above the slide background */
  .mockup {
    background: #252220;
    border-radius: 22px;
    border: 1px solid rgba(245,242,237,0.08);
    max-width: 720px;
    overflow: hidden;
    color: #F5F2ED;
  }
  .swipe { font-size: 26px; font-weight: 700; color: #F5F2ED; }
  .footer { display: flex; flex-direction: column; align-items: center; gap: 18px; }
  .indicator { display: flex; gap: 12px; align-items: center; }
  .dot { width: 9px; height: 9px; border-radius: 50%; background: #3F3B34; }
  .dot.active { width: 13px; height: 13px; background: #E85D3C; }

  /* Carousel chevrons — dark panels with cream arrows */
  .chev {
    position: absolute; top: 50%; transform: translateY(-50%);
    width: 44px; height: 44px; border-radius: 50%;
    background: #252220;
    border: 1px solid rgba(245,242,237,0.08);
    display: flex; align-items: center; justify-content: center;
    color: #F5F2ED; font-size: 26px; font-weight: 400;
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
        Crea un agente con <span class="accent-coral">Claude</span>
      </h1>
      <!-- Optional subtitle -->
    </div>

    <div class="mockup">
      <!-- Slot for mockup content -->
    </div>
  </div>

  <div class="footer">
    <div class="indicator">
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

### Note on the yellow marker text color

When a word is wrapped in `.accent-yellow` (the yellow marker background), the text **inside** the marker must stay **dark** (`#0E0E0E`), even in dark mode. Yellow is a light color — putting cream text on yellow is unreadable. The marker is the one place in dark mode where the inline text inverts back to dark, and that's intentional. The light scaffolds don't need to set this explicitly because the body text is already dark, but the dark scaffold MUST set `color: #0E0E0E` inside `.accent-yellow`.

---

## 7. Dark mode checklist (run before exporting)

- [ ] Folder ends in `-dark` (e.g. `Outputs/agentes-claude-v2-dark/`)
- [ ] Background is warm dark `#17140F`, NOT pure black
- [ ] Grid lines are present and use `#26221C`
- [ ] Primary text is `#F5F2ED` (warm cream), not pure white
- [ ] Coral `#E85D3C` and yellow `#FFE45C` are unchanged from light mode
- [ ] Yellow marker text inside `.accent-yellow` is `#0E0E0E` (dark), not cream
- [ ] Mockup cards are `#252220` with a thin warm border, not white, not pure black
- [ ] Heavy drop shadows have been removed or replaced with thin borders / subtle glows
- [ ] Slide indicator inactive dots are `#3F3B34`, active dot is still coral
- [ ] Carousel chevrons are `#252220` with cream arrows
- [ ] Closing CTA pill is `#252220` with cream text
- [ ] Terminal mockups have been re-balanced (slightly darker than slide bg, OR with a coral border)
- [ ] Code snippet syntax highlighting tokens have been brightened where needed
- [ ] Layout, spacing, fonts, copy, SVG paths are **identical** to the light original (or to what a light version would look like, if generating fresh)
- [ ] Saved with the same filename as the light original, in the `-dark` folder
- [ ] All slides in the carousel are dark (no half-and-half)
