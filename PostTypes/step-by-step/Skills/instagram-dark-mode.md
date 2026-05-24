---
name: instagram-dark-mode
description: Dark-mode variant guidance for step-by-step posts. With brand v2, dark mode is a first-class option asked at the start of every post (not a conversion-after-the-fact). This skill documents the DARK token mappings and any patterns that differ from LIGHT mode.
type: skill
---

# Step-by-Step Dark Mode

> **In brand v2, mode is asked at the start of every post** (along with the color scheme). Dark mode is no longer an opt-in conversion -- it's chosen up front per the user's preference. This skill exists as a reference for the dark-mode tokens and any patterns that differ from LIGHT mode.

The canonical palette for both modes lives in [Brand/brand-spec.md](../../../Brand/brand-spec.md). This file documents the *deltas* between LIGHT and DARK for step-by-step posts specifically.

---

## 1. Token mapping (LIGHT → DARK)

| Role | LIGHT mode | DARK mode |
|---|---|---|
| Background (primary) | `#efedec` (canonical cream) | `#11191b` (canonical warm dark) |
| Background (alt) | `#e4dfde` / `#b4c8cd` / `#ffffff` | `#0c1314` / `#000000` / `#002b53` / `#00386e` |
| Text (primary) | `#0c1314` | `#ffffff` |
| Text (body) | `#0c1314` / `#11191b` | `#e6ecee` |
| Text (subtle / labels) | `#6b6860` / `#b4c8cd` | `#c9d7da` / `#efedec` |
| Eyebrow / handle | scheme highlight (e.g. `#ffb050`) | scheme highlight (UNCHANGED) |
| Headline Playfair Italic emphasis | scheme highlight | scheme highlight (UNCHANGED) |
| Solid pill background | scheme `solid` (e.g. `#ff9d00`) | scheme `solid` (UNCHANGED) |
| Solid pill text | `#ffffff` | `#ffffff` (UNCHANGED) |
| Outline pill (Desliza) border + text | `#0c1314` | `#ffffff` |
| Terminal mockup background | `#0c1314` | `#000000` (slightly darker than slide bg so it reads as raised) |
| Terminal mockup bar | `#1a2225` | `#0c1314` |
| Terminal mockup text | `#efedec` | `#efedec` (UNCHANGED) |
| Closing CTA pill bg / text | bg `#0c1314`, text `#efedec` | bg `#ffffff`, text `#0c1314` (inverts so the pill stays the contrast highlight) |

**Things that stay identical between modes:**
- All accent colors per scheme (orange / red / blue families) -- they read well on both bg
- Font choices (Roboto + Playfair Italic)
- Layout, spacing, font sizes, line heights
- Colombian Spanish, `@lucianomusellaa`, all copy rules

---

## 2. Gradient mode variants (LIGHT_DARK / DARK_LIGHT / GRADIENTES)

The user's chosen template subfolder may specify a gradient variant. Override the flat background accordingly:

| Variant | CSS background |
|---|---|
| `LIGHT_DARK` (light top fading to dark) | `linear-gradient(to bottom, #efedec 0%, #11191b 100%)` |
| `DARK_LIGHT` (dark top fading to light) | `linear-gradient(to bottom, #11191b 0%, #efedec 100%)` |
| `GRADIENTES/DARK` | `linear-gradient(to bottom, #000000 0%, #00386e 100%)` (black → navy) |
| `GRADIENTES/LIGHT` | `linear-gradient(to bottom, #efedec 0%, #c9d7da 100%)` (cream → soft blue-gray) |

When using a gradient, the **text color is determined by the gradient's text-readable zone**:
- If the headline sits on the dark portion → use `#ffffff` text
- If the headline sits on the light portion → use `#0c1314` text
- For long headlines spanning both, prefer the more contrasted color (usually white in a LIGHT_DARK or DARK gradient)

The terminal mockup may switch its internal palette to match the surroundings -- in a DARK gradient bottom, a terminal with light-mode body chrome (white bg, dark text) creates strong visual separation. See template `Brand/Templates/Tutorial/AMARILLO/GRADIENTES/DARK_LIGHT/*-09.png` for the canonical example.

---

## 3. Anti-patterns (dark mode specific)

- ❌ Pure black `#000000` as primary background -- always use the warm dark `#11191b` for flat dark. Pure black is for accent zones (e.g., the inside of a terminal mockup that needs to be slightly darker than the slide).
- ❌ Pure white `#ffffff` as primary text -- but ALMOST: use `#ffffff` for headlines (high contrast) and `#e6ecee` for body. Both are valid per brand-spec; choose `#ffffff` for emphasis and `#e6ecee` for less-emphatic text.
- ❌ Forgetting to invert the outline "Desliza" pill (still defaults to `#0c1314` border = invisible on dark bg)
- ❌ Mixing LIGHT and DARK slides in the same carousel -- a post is either fully LIGHT or fully DARK
- ❌ Saving DARK variants in the same folder as a LIGHT variant for the same topic. Use folder suffix `-dark` if you have both: `Outputs/{topic-slug}/` and `Outputs/{topic-slug}-dark/`.
- ❌ Yellow marker rectangles with cream text -- if you ever use a solid yellow `#ffb050` pill as a header background, the text inside must be dark (`#0c1314`), even in dark mode. Light text on yellow is unreadable.

---

## 4. Quick checklist for dark-mode slides

- [ ] Body background is `#11191b` (flat DARK) OR a documented gradient variant
- [ ] Primary text is `#ffffff` (headlines) and `#e6ecee` (body) -- not pure white everywhere
- [ ] Eyebrow / handle / italic emphasis use the scheme highlight color (same as light)
- [ ] Outline pill ("Desliza") has white border + white text
- [ ] Terminal mockup reads as a raised panel (slightly darker bg than slide, OR with a thin coral border)
- [ ] Solid pill text remains `#ffffff` on the scheme `solid` token
- [ ] No half-and-half carousels (all slides DARK if one is)
