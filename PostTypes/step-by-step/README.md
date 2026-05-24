# Step-by-step posts -- workflow

This is the **most mature** post type. Its visual system, layouts, and copy rules live in the 4 skills inside [`Skills/`](Skills/) and in [Brand/brand-spec.md](../../Brand/brand-spec.md). Whenever the user triggers a step-by-step post, follow this workflow **in order**. Do not skip steps. Do not render images before the user approves the breakdown.

## What this type is for

Tutorials, how-tos, "X pasos para Y", anything where the carousel walks the viewer through a sequence of actions. Carousel structure: **cover → paso 01 → paso 02 → ... → cierre**.

## Trigger phrases

- "nuevo post: {tema}"
- "hagamos un post sobre {tema}"
- "generemos un carrusel de {tema}"
- "quiero un post de {tema}"
- "post paso a paso de {tema}" / "tutorial de {tema}"

---

## Skills to read FIRST (every job)

In this exact order:

1. [Brand/brand-spec.md](../../Brand/brand-spec.md) -- canonical palette, fonts, slide patterns
2. [Skills/instagram-post-design.md](Skills/instagram-post-design.md) -- step-by-step base (workflow, Colombian Spanish, scaffolds)
3. [Skills/instagram-cover-design.md](Skills/instagram-cover-design.md) -- cover layouts (Tutorial cover pattern with italic emphasis + solid pill + visual hook)
4. [Skills/instagram-step-slide-design.md](Skills/instagram-step-slide-design.md) -- step slides + closing slide
5. [Skills/instagram-dark-mode.md](Skills/instagram-dark-mode.md) -- only when the user chose DARK mode at the start

Plus the global mandatory skills:
- [Skills/visual-qa.md](../../Skills/visual-qa.md) -- mandatory post-render QA
- [Skills/slide-spacing.md](../../Skills/slide-spacing.md) -- universal spacing rules

**Mandatory before any new post** (see root [CLAUDE.md](../../CLAUDE.md) §1.5):
- Open at least 2 reference PNGs from `Brand/Templates/Tutorial/{COLOR}/{STYLE}/{MODE}/` matching the user's choices
- Review at least 2 images from [Inspiracion/](Inspiracion/), prioritizing ones not viewed in recent jobs
- Review **all** images in [Favoritos_Claude_Generated/](Favoritos_Claude_Generated/)
- Plan at least one structural variation vs. the most recent step-by-step post so the new one doesn't visually rhyme with the previous

---

## Type-specific non-negotiable rules

(These extend the brand-wide rules in the root [CLAUDE.md](../../CLAUDE.md) and Brand/brand-spec.md. They are step-by-step specific.)

### Headline emphasis pattern
- **Cover slide:** 1 word in Playfair Display Italic in the scheme highlight color
- **Step slides:** 1 word in Playfair Display Italic in the scheme highlight color (same pattern, shorter overall headline)
- **Closing slide:** typically a bold black/white primary text without italic emphasis (the visual + CTA pill carry the emphasis)
- Never use 2 italic words in the same headline. Single emphasis only.

### Eyebrow on step slides
- Every step slide opens with `TUTORIAL · PASO 0X` (zero-padded 2-digit number) in the scheme highlight color, ALL CAPS, letter-spacing 2px
- Covers do NOT have an eyebrow
- Closing slides do NOT have an eyebrow

### Handle position
- `@lucianomusellaa` appears on the **cover and the closing slide only**
- Interior step slides do NOT show the handle (saves vertical space for content)
- This is a brand v2 change from the old "handle on every slide" rule

### No page dots
- Instagram adds carousel pagination natively. **Never add dot indicators** to slides. Per `feedback_no_page_dots.md`.

### File naming inside the post folder
- `cover_v{n}_{descriptor}.html` for cover variations (generate 2-3)
- `paso_{n}_{descriptor}.html` for step slides (e.g. `paso_1_instala.html`)
- `cierre_cta.html` for the closing slide

---

## Standard workflow (11 steps)

### Step 0 -- Confirm post type + color + mode (MANDATORY)
Per root [CLAUDE.md §1](../../CLAUDE.md), ask the user to confirm three things: post type, color scheme (AMARILLO / ROJO / AZUL), and mode (LIGHT / DARK). Never assume.

### Step 1 -- Re-anchor visually (silent, fast -- but MANDATORY)
- Read the skills listed above
- **Open `Brand/Templates/Tutorial/{COLOR}/{STYLE}/{MODE}/`** for the user's choices and read at least 2 PNGs
- **List `Inspiracion/`** and open at least 2 reference images
- **List and read every image in `Favoritos_Claude_Generated/`** (the user's curated past favorites)
- **List `Logos/` (project root)** so I know which real brand assets are available
- Plan at least one structural variation vs. the most recent step-by-step post

### Step 2 -- Gather context (ask only what's missing)
In one message, only ask the questions whose answers I don't already have:
1. **How many slides?** (Default: cover + 4 pasos + closing = 6 slides)
2. **Source material?** URL / doc / paste-in?
3. **Specific italic emphasis word** the user wants in the cover headline?
4. **Real screenshots / logos** in `Assets/` or `Logos/` I should use?
5. **Tone / angle**: instructional (default), bold claim, case study, opinion?

### Step 3 -- Propose the breakdown in plain text (DO NOT render yet)
Write the full carousel breakdown as text:
- For the cover: 2-3 headline variants with the exact italic emphasis word for each + optional "en X pasos" pill
- For each step: `PASO 0X` + headline (with `**italic-word**`) + body subtitle (or "none -- visual carries it") + visual hook description
- For the closing: pre-text + big text + CTA pill word + caption

Ask: *"¿Apruebas el desglose o ajustamos algo antes de generar?"*

### Step 4 -- Wait for approval
Do not write any HTML until the user approves.

### Step 5 -- Create the output folder (dated)
```bash
mkdir -p "PostTypes/step-by-step/Outputs/$(date +%Y-%m-%d)_{topic-slug}"
```
Slug: kebab-case, ≤4 words. **Folder MUST start with `YYYY-MM-DD_` prefix** (today's date) so the auto-prune step can sort and keep only the last 5 posts per type. See root CLAUDE.md §3.6.

### Step 6 -- Generate any missing logos via Higgsfield MCP
If a brand mentioned in the post lacks a logo in `Logos/`, generate it via `mcp__higgsfield__generate_image`. Save to `Logos/` after user review. See root CLAUDE.md §3.5.

### Step 7 -- Write the HTML files
- Use the scaffolds from the skills as starting points
- Inline all CSS in each file (no external stylesheets)
- Use the `@font-face` block from `Brand/brand-spec.md §2` -- local TTFs, no Google Fonts CDN
- NO page dots
- Match palette tokens to the user's chosen scheme + mode

### Step 8 -- Render with `./render.sh`
```bash
./render.sh PostTypes/step-by-step/Outputs/{topic-slug}
```

### Step 9 -- Verify each PNG visually (Visual QA -- mandatory)
Read each rendered `.png` to confirm fonts loaded (Roboto + Playfair Italic, not fallback), palette matches scheme/mode, Colombian Spanish, no page dots, no layout overflow.

### Step 10 -- Present to the user
Show the carousel as a sequence (cover → paso 01 → ... → cierre). Offer iterations.

### Step 11 -- Capture favorites (MANDATORY)
Once the user is happy:

> *"¿Cuáles imágenes de este post son tus favoritas? Las guardo en `Favoritos_Claude_Generated/` para usar como referencia en posts futuros."*

```bash
cp "PostTypes/step-by-step/Outputs/{topic-slug}/{slide_name}.png" \
   "PostTypes/step-by-step/Favoritos_Claude_Generated/{topic-slug}_{slide_name}.png"
```

- **Always `cp`, never `mv`**
- Prefix destination with the topic slug
- If "ninguna" or skip, don't save anything but still ask

### Step 12 -- Prune old outputs (MANDATORY, after favorites)
```bash
python Brand/prune_outputs.py step-by-step
```
Keeps the 5 most-recent dated folders, deletes older ones. Favorites already copied in Step 11 survive (they live in `Favoritos_Claude_Generated/`, which is never pruned). Historical pre-migration folders without a date prefix are also never touched. See root CLAUDE.md §3.6.
