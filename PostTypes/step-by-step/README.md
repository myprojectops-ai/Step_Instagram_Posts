# Step-by-step posts — workflow

This is the **mature** post type. Its visual system, layouts and copy rules are fully defined in the 3 skills inside [`Skills/`](Skills/). Whenever the user triggers a step-by-step post, follow this workflow **in order**. Do not skip steps. Do not render images before the user approves the breakdown.

## What this type is for

Tutorials, how-tos, "X pasos para Y", anything where the carousel walks the viewer through a sequence of actions. The carousel is structured as: **cover → paso 1 → paso 2 → … → cierre**.

## Trigger phrases

- "nuevo post: {tema}"
- "hagamos un post sobre {tema}"
- "generemos un carrusel de {tema}"
- "quiero un post de {tema}"
- "post paso a paso de {tema}" / "tutorial de {tema}"

---

## Skills to read FIRST (every job)

In this exact order:

1. [Skills/instagram-post-design.md](Skills/instagram-post-design.md) — base visual system (palette, fonts, render pipeline, anti-patterns, slide indicator)
2. [Skills/instagram-cover-design.md](Skills/instagram-cover-design.md) — cover layouts (Layout A: two logos / Layout B: mockup / Layout C: typographic)
3. [Skills/instagram-step-slide-design.md](Skills/instagram-step-slide-design.md) — step slides + closing slide

### Opt-in skill — dark mode

4. [Skills/instagram-dark-mode.md](Skills/instagram-dark-mode.md) — **only when the user explicitly asks** for "modo oscuro" / "dark mode" / "convierte este post a modo oscuro". Defines the warm-dark palette (background `#17140F`, text `#F5F2ED`) and the conversion rules. Coral and yellow accents stay unchanged. Default is always light — never volunteer dark mode unprompted.

Also, **mandatory before any new post** (see root [CLAUDE.md](../../CLAUDE.md) section 1.5):
- Review at least 2 reference images from [Inspiracion/](Inspiracion/), prioritizing ones I haven't viewed in recent jobs
- Review **all** images currently inside [Favoritos_Claude_Generated/](Favoritos_Claude_Generated/) (the user's curated favorites from past sessions)
- Plan at least one structural variation vs. the most recent step-by-step post so the new one doesn't visually rhyme with the previous

---

## Type-specific non-negotiable rules

(These extend the brand-wide rules in the root [CLAUDE.md](../../CLAUDE.md). They are step-by-step specific.)

### Highlight rules
- **Cover slides** → DOUBLE highlight by default: one keyword in coral, the other on yellow marker (user-confirmed preference, validated against 5 alternatives)
- **Step slides** → SINGLE highlight only: one keyword in coral OR on yellow, never both
- **Closing slide** → may use a single coral accent in the big text

### Slide indicator (mandatory)
- Every slide in a carousel includes a **slide indicator** at the bottom: `N` small dots (one per slide), the current slide's dot bigger and coral, the rest small and grey `#D5D0C8`
- See [Skills/instagram-post-design.md](Skills/instagram-post-design.md) section 4.5 for the full spec
- Position: above `Desliza →` on slides 1..N-1; at the bottom of the closing slide (which has no `Desliza →`)

### File naming inside the post folder
- `cover_v{n}_{descriptor}.html` for cover variations (always generate 3+)
- `paso_{n}_{descriptor}.html` for step slides
- `cierre_cta.html` for the closing slide

---

## Standard workflow (10 steps)

### Step 0 — Confirm post type (MANDATORY)
Before anything else, **always ask the user to confirm** that this is a step-by-step post (not news, not informativo). Phrasings can be ambiguous. Never assume — even if the trigger phrase is obvious. See root [CLAUDE.md](../../CLAUDE.md) section 1 for the exact question.

### Step 1 — Re-anchor visually (silent, fast — but MANDATORY)
- Read the 3 skill files listed above
- **List `Inspiracion/`** to catch any newly added references; open at least 2 (preferring ones not viewed in recent jobs)
- **List and read every image in `Favoritos_Claude_Generated/`** — these are the user's curated past favorites and the strongest signal of what works
- **List `Logos/` (project root)** so I know which real brand assets are available for any brand the post mentions. See root [CLAUDE.md](../../CLAUDE.md) section 3.5.1 — never fabricate a brand logo.
- Check `memory/MEMORY.md` for any user preferences I should know
- Plan at least one structural variation vs. the most recent step-by-step post (different cover layout, different visual element, different hook structure) so the new post doesn't visually rhyme with the previous one. **Variety is essential.**

### Step 2 — Gather context (ask the user only what's missing)
Ask, in one message, only the questions whose answers I don't already have:
1. **How many slides?** (Default: cover + 4 pasos + closing = 6 slides)
2. **Source material?** Is there a URL / doc / paste-in I should base the steps on? (If yes, fetch it now)
3. **Any specific keyword(s)** the user wants highlighted in the cover headline?
4. **Are there real screenshots / logos** in `Assets/` or `Logos/` I should use, or should I recreate UIs in HTML?
5. **Tone / angle**: instructional (default), bold claim, case study, opinion?

If the user already gave me a URL or all this info upfront, **don't re-ask** — go to step 3.

### Step 3 — Propose the breakdown in plain text (DO NOT render yet)
Write the full carousel breakdown as text:
- For the cover: 3 headline variants with the exact double-highlight keywords for each
- For each step: PASO N + headline (with keyword in `**bold**`) + subtitle (or "none — visual carries it") + mockup description
- For the closing: pre-text + big text + CTA pill word + caption

Then ask: *"¿Apruebas el desglose o ajustamos algo antes de generar?"*

### Step 4 — Wait for approval
Do not write any HTML until the user approves. If they want changes, iterate on the text breakdown.

### Step 5 — Create the output folder
```bash
mkdir -p "PostTypes/step-by-step/Outputs/{topic-slug}"
```
The slug must be kebab-case, ≤4 words.

### Step 6 — Write the HTML files
- Use the scaffolds from the skills as starting points
- Inline all CSS in each file (no external stylesheets — Chrome headless renders these standalone)
- Include the slide indicator footer on every slide (with the correct dot active)
- Use Inter via Google Fonts CDN, JetBrains Mono for any code

### Step 7 — Render with `./render.sh`
```bash
./render.sh PostTypes/step-by-step/Outputs/{topic-slug}
```
This converts every `.html` in the folder to a `.png` of the same name.

### Step 8 — Verify each PNG visually
Read each rendered `.png` with the Read tool to confirm:
- Username is `@lucianomusellaa`
- Spanish is Colombian (no `á` at end of imperatives)
- Slide indicator has the correct dot active
- No layout overflow / clipping
- Highlights match the breakdown

### Step 9 — Present to the user
Show the carousel as a sequence (cover → paso 1 → ... → cierre) using markdown links to each PNG. Offer iterations: copy tweaks, layout swaps, color adjustments.

### Step 10 — Iterate slide by slide until ready
Each iteration should be the **smallest possible change**. Re-render only the affected slide(s), not the whole carousel.

### Step 11 — Capture favorites (MANDATORY)
Once the user is happy with the final post, **always ask**:

> *"¿Cuáles imágenes de este post son tus favoritas? Las guardo en `Favoritos_Claude_Generated/` para usar como referencia en posts futuros."*

For each image the user names:
```bash
cp "PostTypes/step-by-step/Outputs/{topic-slug}/{slide_name}.png" \
   "PostTypes/step-by-step/Favoritos_Claude_Generated/{topic-slug}_{slide_name}.png"
```
- **Always `cp`, never `mv`** — the original outputs stay where they are.
- Prefix the destination filename with the topic slug so it's clear which post it came from.
- If the user says "ninguna" or skips, don't save anything but still ask. The answer is data either way.
