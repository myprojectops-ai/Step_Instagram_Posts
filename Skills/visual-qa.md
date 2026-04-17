---
name: visual-qa
description: Mandatory quality assurance skill that runs after EVERY render. Open and visually inspect every generated PNG before showing it to the user. Catches broken logos, white gaps, unreadable text, and layout mismatches. Applies to ALL post types.
type: skill
---

# Visual QA — Mandatory Post-Render Verification

> **This skill applies to ALL post types** (step-by-step, news, informativos). It runs after every `render.sh` call, before presenting any image to the user. It is non-negotiable and cannot be skipped.

---

## 1. Why this skill exists

Generated HTML can look correct in code but render wrong: logos fail to load, photos don't cover the canvas, filters break, text overflows, transparent PNGs show unexpected backgrounds. The user has zero tolerance for presenting images with invisible bugs — they expect every image shown to them to be verified.

**The rule:** never describe a feature you can't visually confirm in the rendered output.

---

## 2. When to run this check

**After EVERY call to `render.sh`**, without exception. Whether it's 1 file or 20 files, open and inspect each rendered PNG before showing anything to the user.

---

## 3. The QA checklist

For every rendered PNG, open the image with the Read tool and verify:

### 3.1 Photo / background
- [ ] Photo covers the full 1080×1350 canvas (no white or light gaps at edges)
- [ ] No unexpected white/gray bands at top, bottom, left, or right edges
- [ ] If a dark background is expected, the entire canvas reads as dark
- [ ] `object-fit: cover` is working (photo isn't letterboxed or distorted)

### 3.2 Logos and brand assets
- [ ] Every logo referenced in the HTML actually appears in the rendered image
- [ ] Logos are recognizable (not pixelated blobs, blank squares, or invisible)
- [ ] Logo colors/filters work as intended (white logos on dark bg are visible, teal logos with invert filter actually turned white, etc.)
- [ ] No "broken image" icons (the ✕ placeholder Chrome shows when an `<img>` fails)

### 3.3 Text
- [ ] Headline is fully visible and legible (not clipped, not running off-canvas)
- [ ] Headline contrast is sufficient against the background (white text on dark overlay must be crisp)
- [ ] Accent colors (coral, yellow) actually render on the highlighted words
- [ ] No text overflow or wrapping issues (words don't break mid-syllable in ugly ways)
- [ ] Badge text ("AI NEWS", "PASO X") is readable
- [ ] Username `@lucianomusellaa` is visible

### 3.4 Layout
- [ ] Elements are positioned where intended (top bar at top, headline in bottom third for news, etc.)
- [ ] No overlapping elements that shouldn't overlap
- [ ] Gradient overlay is strong enough for readability but not so heavy it kills the photo
- [ ] Watermarks/subtle elements are present but not dominant
- [ ] **Content below y≈1272 renders correctly** — dots, pills, taglines, bottom-row elements must be visible. Chrome headless on Windows subtracts ~96px for window chrome; `render.sh` compensates with a larger viewport + crop, but verify these elements are not cut off

### 3.5 Cross-variation consistency
- [ ] When generating multiple variations, verify each one individually — don't assume "if v1 looks good, v2 is fine too"
- [ ] Compare variations against each other to confirm the intended differences are visible

---

## 4. What to do when a check fails

1. **Identify the root cause** in the HTML/CSS (don't guess — find the actual line)
2. **Fix the HTML**
3. **Re-render** the affected file(s)
4. **Re-verify** the new render
5. Only after the fix is confirmed visually, proceed to present to the user

**Never** present a broken image and describe it as working. If an element didn't render, say so and fix it — don't pretend it's there.

---

## 5. Common failure patterns and fixes

| Symptom | Likely cause | Fix |
|---|---|---|
| Logo renders as blank/white square | PNG with transparency + wrong CSS filter | Remove filter, or use `mix-blend-mode: screen` for white-on-black logos |
| Logo renders as tiny pixelated blob | Image is very small and being upscaled | Use a higher-res source, or keep it small and pair with text label |
| White edges/gaps around photo | Photo doesn't cover full canvas | Add `background: #0A0A0A` to body as fallback + verify `object-fit: cover` |
| Light patches visible through overlay | Linear gradient only goes top→bottom, doesn't cover lateral brightness | Add a radial vignette layer in addition to the linear gradient |
| Text invisible on light part of photo | Gradient overlay too light in that zone | Increase gradient opacity in the zone where text sits |
| AVIF/WebP image not rendering | Browser/renderer doesn't support format | Convert to PNG, or verify Chrome version supports the format |
| CSS filter makes logo invisible | `brightness(0) invert(1)` on transparent PNG kills alpha | Use `mix-blend-mode: screen` instead for white-on-black logos, or `filter: brightness(100)` for teal logos |
| Bottom elements (dots, pills, taglines) missing | Chrome headless viewport bug — content below y≈1272 was not rendered with old `--window-size=1098,1368` | Verify `render.sh` uses `--window-size=1098,1550` + PIL crop to 1080×1350. If still cut off, increase the height further |

---

## 6. Integration with post workflows

This skill is automatically part of every post type's workflow. The step is always:

```
... → render.sh → **VISUAL QA (this skill)** → present to user
```

In the news workflow, this is step 10. In step-by-step, it should be added after every render step. The skill does NOT need to be "called" — it's an implicit obligation every time an image is rendered.
