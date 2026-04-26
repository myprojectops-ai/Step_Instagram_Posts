---
name: informativo-visual-iteration
description: Self-iteration skill for informativo posts â€” render with PIL, screenshot, check alignment against exact blob positions (scipy connected components), fix, repeat until visually correct before presenting to user.
type: skill
---

# Informativo Visual Iteration Skill

> **This skill is MANDATORY for every informativo post.** Never present a rendered image to the user without completing the self-iteration loop first.

## The problem this solves

Informativo posts use Codex image tool compositions + PIL text overlay. The text must align precisely with organic blob shapes in the composition. Manual position estimates can be off by **100+ pixels** on irregular shapes. This skill ensures positions are calculated precisely and verified visually before the user sees anything.

---

## Step 0 â€” Find exact blob positions with scipy (BEFORE any rendering)

**Never guess pixel coordinates.** Use connected component analysis on the composition image to find the exact center of each white interior:

```python
from PIL import Image
import numpy as np
from scipy import ndimage

comp = Image.open("composition.png").convert("RGB")
if comp.size != (1080, 1350):
    comp = comp.resize((1080, 1350), Image.LANCZOS)
arr = np.array(comp)

# Pure white pixels (>252) = blob interiors, not cream background (~245)
white = np.all(arr > 252, axis=2)
labeled, n = ndimage.label(white)

for i in range(1, n + 1):
    mask = labeled == i
    size = np.sum(mask)
    if size > 3000:  # only large regions = actual blob interiors
        coords = np.argwhere(mask)
        cy = int(coords[:, 0].mean())
        cx = int(coords[:, 1].mean())
        y1, x1 = int(coords[:, 0].min()), int(coords[:, 1].min())
        y2, x2 = int(coords[:, 0].max()), int(coords[:, 1].max())
        w, h = x2 - x1, y2 - y1
        print(f"center=({cx},{cy}), bbox=({x1},{y1})-({x2},{y2}), size={w}x{h}")
```

This gives:
- **center (cx, cy)** â€” where to center the text block
- **bbox width and height** â€” maximum area for text (use ~75-85% of this to leave padding)

Store these values and use them for ALL text positioning. Do NOT manually estimate.

---

## Step 1 â€” PIL compositing (NOT Chrome/render.sh)

**Always use PIL for informativo text compositing.** Chrome on Windows creates border artifacts with background-image compositions.

```python
from PIL import Image, ImageDraw, ImageFont

comp = Image.open("composition.png").convert("RGBA")
if comp.size != (1080, 1350):
    comp = comp.resize((1080, 1350), Image.LANCZOS)
canvas = comp.copy()
draw = ImageDraw.Draw(canvas)

# Fonts from Assets/Fonts/
font_name = ImageFont.truetype("Assets/Fonts/Inter-ExtraBold.ttf", 30)
font_badge = ImageFont.truetype("Assets/Fonts/Inter-Bold.ttf", 14)
font_desc = ImageFont.truetype("Assets/Fonts/Inter-Medium.ttf", 18)
font_title = ImageFont.truetype("Assets/Fonts/Inter-Black.ttf", 38)
font_handle = ImageFont.truetype("Assets/Fonts/Inter-Medium.ttf", 20)

# Draw text centered on blob centers from Step 0
# ... (name, badge pill, wrapped description for each tool)

canvas.convert("RGB").save("output.png", quality=95)
```

### Key rules for PIL compositing:
- **No white card backgrounds** â€” text goes directly on the composition. White ovals already provide contrast.
- **Center text on scipy-detected blob centers** â€” not manual estimates.
- **Wrap descriptions** to fit within ~75% of the blob's detected width.
- **Handle goes at the BOTTOM** of the image (not top) for informativo posts.
- **Title** should be large (38px+) and centered in the composition's title bar area.

---

## Step 2 â€” The self-iteration loop

```
FOR EACH render attempt:
  1. RENDER the image with PIL
  2. READ the rendered PNG (use Read tool to visually inspect)
  3. CHECK every element against the checklist below
  4. IF any check fails â†’ identify what's wrong, FIX it, go back to step 1
  5. IF all checks pass â†’ the image is ready to present to the user
```

**Maximum iterations:** 5. If after 5 attempts there are still minor issues, present the best version with honest notes.

---

## Checklist â€” verify on EVERY render

### Edge-to-edge
- [ ] Image is exactly 1080x1350 â€” no white, black, or colored strips on any edge
- [ ] Composition reaches all 4 corners
- [ ] `canvas.size == (1080, 1350)` verified in code before saving

### Text inside white ovals
- [ ] Each text block (name + badge + description) is visually INSIDE its blob's white interior
- [ ] No text overlaps with colored blob borders
- [ ] No text overlaps with composition icons/logos (sailboat, brand symbols, etc.)
- [ ] Text has visible padding from blob edges

### Title and handle
- [ ] Title is large, centered in the composition's title bar area
- [ ] Highlighted keywords (coral number, yellow marker) are visible
- [ ] `@lucianomusellaa` is at the BOTTOM, visible, not overlapping with anything

### Typography
- [ ] All text is readable â€” names are big (28-36px), descriptions are legible (16-18px)
- [ ] No text is cut off
- [ ] Badge pills have correct brand colors
- [ ] Descriptions don't overflow the blob area

### Spacing
- [ ] Name and badge are NOT overlapping (check especially on smaller blobs)
- [ ] Adequate gap between name â†’ badge â†’ description (min 6px)
- [ ] Footer/handle not cut off at bottom edge

---

## Key rule: NEVER present unchecked renders

The user's time is more valuable than render cycles. It's better to iterate 5 times silently and present one clean image than to show 5 broken iterations asking for feedback on each.

If the self-QA catches an issue, fix it **without telling the user about the intermediate failure**. Only mention the iteration process if the user asks or if you hit the 5-iteration limit.

