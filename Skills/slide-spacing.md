---
name: slide-spacing
description: Universal spacing and layout rules that apply to EVERY slide across ALL post types (step-by-step, news, informativos). Content must fill the usable canvas proportionally — never leave large empty zones. Scale elements to content, or center when content is shorter than the container.
type: skill
---

# Slide Spacing & Layout — Universal Rules

> **Scope:** applies to every slide of every post type. This skill is mandatory reference material during (a) when writing a slide's HTML and (b) visual QA before presenting to the user. The [autoloaded CLAUDE.md](../CLAUDE.md) points to this skill in its brand-wide rules.

## 1. The core principle

> **Content must occupy ~70–85% of the usable canvas. Never leave large empty zones in the middle or at the bottom of a slide.**

The canvas is 1080×1350. The "usable canvas" excludes the Instagram safe-zone margins (~60–80px on the sides, ~60–100px top/bottom for the feed thumbnail). Content should spread to fill that usable area in a visually balanced way — not clump at the top or bottom.

### Why this matters

Sparse slides feel unfinished, amateur, or like a placeholder. Good editorial design uses the whole canvas deliberately. When content happens to be short (a single punchline, a small quote, a few lines), the slide must **respond** — either scale the content up or redistribute it across the available space.

---

## 2. The two rules for variable content length

When the same template holds content of varying length (short quote vs long quote, one stat vs a paragraph), pick one of these two strategies:

### Rule A — "Fit to fill" (scale the font, keep container)
Increase the font size so the text physically fills more of the container. Best for single-focus elements like **quote cards, stat cards, headlines**.

| Content length | Font size (on a ~1080×1000 card) |
|---|---|
| 1 short line (< 10 words) | 70–90px |
| 1 medium line (10–20 words) | 54–64px |
| 2–3 lines | 44–52px |
| 4–6 lines (paragraph) | 34–44px |
| 7+ lines | 28–34px + use smaller container |

The rule of thumb: measure the container height (in px), divide by the number of text lines, and make the font size roughly `container_height / (lines × 2)`. Adjust visually from there.

### Rule B — "Center in space" (keep font, redistribute vertically)
Use flexbox to distribute the container's content vertically. Best for **multi-element slides** like tweet slides, text+photo slides, closer slides.

```css
.container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;   /* or center, or space-around */
  height: 100%;
}
```

When a slide has a header + middle + footer, always use `justify-content: space-between` so the three zones naturally spread across the canvas.

---

## 3. Spacing patterns by slide archetype

### 3.1 Single-focus card (quote, stat, punchline)

White card with one element + small label + small attribution.

```
┌──────────────────┐
│ LABEL (top)      │
│                  │
│   [empty air]    │
│                  │
│  BIG CONTENT     │ ← vertically centered
│  (quote / stat)  │   fill the middle
│                  │
│   [empty air]    │
│                  │
│ attribution      │
│ source (bottom)  │
└──────────────────┘
```

**CSS pattern:**
```css
.card {
  display: flex;
  flex-direction: column;
  padding: 52px 54px;
}
.card-top { /* label, stays at top */ }
.card-body {
  flex: 1;                         /* takes all available space */
  display: flex;
  flex-direction: column;
  justify-content: center;         /* centers content vertically */
}
.card-bottom { /* attribution, margin-top:auto pushes to bottom */ }
```

**Font sizing:**
- Big stat number: **180–240px** (fills visually)
- Pull quote (2–4 sentences): **46–54px**
- Short quote or 1-line stat explanation: **54–62px**

### 3.2 Multi-element slide (tweet + closer, multiple cards)

Distribute N elements evenly across the canvas height using flex.

```
┌──────────────────┐
│ [Alta Studio]    │ ← top anchor
│                  │
│ LABEL            │ ← section label
│                  │
│ ┌──────────────┐ │
│ │  Element 1   │ │ ← main content
│ │  (tweet)     │ │
│ └──────────────┘ │
│                  │
│ [Divider]        │ ← visual separator
│ Element 2        │ ← secondary content
│                  │
│    • • • • •     │ ← page dots
└──────────────────┘
```

**CSS pattern:**
```css
body {
  display: flex;
  flex-direction: column;
  justify-content: space-between;  /* evenly distribute children */
}
.content-area {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-around;   /* or space-between */
  padding: 160px 60px 70px;        /* top clears logo, bottom clears dots */
}
```

**Rule:** if there's more than 150px of empty space between two elements in the middle of the canvas, redistribute. Either:
- Move elements closer together and accept some bottom margin
- Add a divider/label/visual anchor between them
- Scale one element bigger

### 3.3 Text + photo slide (Template A in news)

Text in top zone, photo at bottom. Text zone must use its height.

```
┌──────────────────┐
│ [Alta Studio]    │
│                  │
│ LABEL            │ ← near top
│                  │
│ Text block       │ ← centered in text zone
│ centered         │    OR top-aligned with extra line-height
│ vertically       │
│                  │
├──────────────────┤ ← photo boundary
│                  │
│  [photo]         │ ← bottom zone
│                  │
└──────────────────┘
```

If text is SHORT (2–3 lines): increase font size OR center vertically in text zone using flex.
If text is LONG (6+ lines): use smaller font and top-align.

### 3.4 Cover patterns (per post type)

Canonical cover patterns are defined in [Brand/brand-spec.md §3](../Brand/brand-spec.md). Summary:

**Tutorial cover (step-by-step):** background color from the chosen mode (LIGHT cream `#efedec` or DARK navy gradient). Layout: `@lucianomusellaa` orange small caps at top → headline (Roboto Bold + 1 word in Playfair Italic accent color) → solid-color pill with "en X pasos" in white → visual hook (terminal mockup, illustration, orgchart) → "Desliza" pill at bottom. See `Brand/Templates/Tutorial/{COLOR}/{STYLE}/{MODE}/` for reference PNGs.

**News cover:** full-bleed 4:5 Higgsfield photo fills entire canvas. CSS gradient darkens the bottom ~40%. Headline (Roboto Black ALL CAPS, white) at `top:860px` and bottom-row (subtitle + optional SWIPE pill) at `top:1268px` are SEPARATE absolute-positioned elements (Chrome clips nested children). 1-3 emphasis words rendered in Playfair Italic in the highlight color. See `Brand/Templates/Noticias/{COLOR}/{MODE}/`.

**Informativo cover:** full-canvas Higgsfield composition (background + visual structure + decorative elements) with HTML text overlay aligned to the composition's empty zones. See `PostTypes/informativos/Skills/informativo-post-design.md`.

Font scaling for cover headlines (all post types, all modes):
- 2-3 line headline: **70-84px**
- 4 line headline: **62-68px**
- 5 line headline: **54-58px**

---

## 4. Vertical margin/padding guide (Instagram-safe)

| Zone | Margin |
|---|---|
| Top of canvas to first content (with logo) | ~160–180px (clears the 100px logo + 60px air) |
| Top of canvas to first content (no logo) | ~140–160px |
| Bottom of canvas to last content | ~70–120px (safe zone for dots/pill). **IMPORTANT:** Chrome headless on Windows subtracts ~96px from `--window-size` height for window chrome. `render.sh` uses `--window-size=1098,1550` + PIL crop to 1080×1350 to compensate. Content at y>1272 (dots, pills, taglines) will be invisible if the viewport is too small. Always verify bottom elements render. |
| Between major content blocks | Proportional — redistribute to fill, don't leave >150px dead space |
| Card padding (inside white cards) | 52px top/bottom, 54px sides (proportional) |
| Between label and main content in a card | 20–40px |

---

## 5. Visual QA checklist — run on every rendered slide

Before presenting any slide to the user, check:

- [ ] **Does content fill the usable canvas?** If there's a big empty zone (>150px in the middle, or >120px at the bottom outside of safe zone), **redistribute or rescale**.
- [ ] **Is the main element proportional to its container?** A quote that takes 1/3 of a white card is wrong — either bigger font, or redistribute.
- [ ] **Are margins consistent?** Top margin above first content should roughly match bottom margin below last content.
- [ ] **Is there a "top-heavy" or "bottom-heavy" feel?** If yes, use flex `justify-content: center` or `space-between` to balance.
- [ ] **Does the slide look empty at first glance?** If yes, scale font up or add a supporting element.

If any of these fail, **fix before presenting**. Do not present a sparse slide and apologize — fix it first.

---

## 6. Anti-patterns

- ❌ Fixed font size that's too small for the content holder (e.g., 33px quote in a 1000px tall card)
- ❌ Content anchored only at top with empty space below
- ❌ >150px of empty black/white space in the middle of a slide with no reason
- ❌ Asymmetric top/bottom margins when content doesn't demand it
- ❌ Leaving a body slide "sparse" because the content is short — always scale or redistribute
- ❌ Using `position: absolute; top: X` for content that should flow with the container's shape
- ❌ Ignoring the rule "if template holds variable content, scale or redistribute"

---

## 7. How this plugs into the workflow

1. **When writing HTML** — actively apply the "fit to fill" or "center in space" rule based on content length. Use flex containers, not rigid absolute positioning.
2. **During Visual QA** (see [visual-qa.md](visual-qa.md)) — open every PNG and run the §5 checklist. Mark any spacing issue as a blocker before presenting.
3. **When user gives spacing feedback** — update the relevant post-type skill with the specific pattern that worked, AND update this skill if the pattern generalizes.

This is a **universal** skill — every slide in every post type must pass these checks.
