# Visual_posts — Project Instructions

This project generates **catchy Instagram carousel posts** for **@lucianomusellaa** using a defined visual system inspired by AI content creators (reference: @ramiro.cubria — visual style only, NOT his handle, NOT his Spanish dialect).

You are operating inside this project. Read this file first whenever a session starts here. Everything below is binding.

---

## 1. Trigger phrase — how the user kicks off a new post

When the user says any of these (or similar):
- **"nuevo post: {tema}"**
- **"hagamos un post sobre {tema}"**
- **"generemos un carrusel de {tema}"**
- **"quiero un post de {tema}"**

…I execute the **Standard Post Workflow** in section 4 below. I do NOT improvise the order or skip steps.

---

## 2. Project map

```
Visual_posts/
├── CLAUDE.md                          ← this file (autoloaded)
├── Skills/
│   ├── instagram-post-design.md       ← BASE visual system (read FIRST)
│   ├── instagram-cover-design.md      ← cover/thumbnail layouts
│   └── instagram-step-slide-design.md ← step slides + closing slide
├── Ejemplos/                          ← visual reference images (re-open every job)
│   ├── Ej_.png   → Type A cover (2 logos)
│   ├── Ej_1.png  → Type B cover (mockup)
│   ├── Ej_2.png  → Step slide with subtitle
│   ├── Ej_3.png  → Cover with phone screenshot
│   ├── Ej_4.png  → Step slide without subtitle
│   └── Ej_5.png  → Closing "follow for more" slide
├── Logos/                             ← real brand assets I can drop into slides
│   └── Claude_AI_symbol.svg
├── Assets/                            ← user-provided screenshots + AI-generated images
├── Outputs/                           ← rendered carousels (one folder per post)
│   └── {topic-slug}/
├── Errors/                            ← user marks visual bugs here for me to fix
├── .env                               ← GEMINI_API_KEY (never commit, never echo)
├── render.sh                          ← HTML→PNG batch renderer (use this, not raw chrome)
└── memory/                            ← persistent user/feedback memories (auto-loaded)
```

---

## 3. Non-negotiable rules (don't ask, don't deviate)

These are project-wide invariants. They live across every post, every slide, every iteration. They are also documented inside the skills, but they belong here too because they're load-bearing for *every* job.

### 3.1 Brand handle
- The handle on top of every slide is **`@lucianomusellaa`** (double "a")
- Never `@ramiro.cubria` — that's only the visual reference creator

### 3.2 Spanish dialect
- **Colombian Spanish, `tú` form** — never Argentinian voseo
- ✅ Crea, Define, Instala, Convierte, Delega, Desliza, Guarda, Usa, tú, tienes, quieres
- ❌ Creá, Definí, Instalá, Convertí, Delegá, Deslizá, Guardá, Usá, vos, tenés, querés
- Reflexive imperatives keep the accent: `instálalo`, `arráncalo`, `guárdalo`
- Full conversion table is in [Skills/instagram-post-design.md](Skills/instagram-post-design.md) section 3.5

### 3.3 Visual system (cream + coral + yellow + grid)
- Background: cream `#F5F2ED` (NOT pure white) with subtle grid `#E8E4DD`
- Primary text: `#0E0E0E`
- Accent coral: `#E85D3C`
- Highlight yellow: `#FFE45C`
- Canvas: 1080×1350 px (4:5 portrait)
- Font: Inter (500/600/700/800), JetBrains Mono for code

### 3.4 Highlight rules (this is what makes covers catchy)
- **Cover slides** → DOUBLE highlight by default: one keyword in coral, the other on yellow marker (user-confirmed preference, validated against 5 alternatives)
- **Step slides** → SINGLE highlight only: one keyword in coral OR on yellow, never both
- **Closing slide** → may use a single coral accent in the big text

### 3.5 Slide indicator
- Every slide in a carousel includes a **slide indicator** at the bottom: `N` small dots (one per slide), the current slide's dot bigger and coral, the rest small and grey `#D5D0C8`
- See [Skills/instagram-post-design.md](Skills/instagram-post-design.md) section 4.5 for the full spec
- Position: above `Desliza →` on slides 1..N-1; at the bottom of the closing slide (which has no `Desliza →`)

### 3.6 Output folder structure
- **Every post lives in its own folder** under `Outputs/{topic-slug}/`
- The slug is kebab-case, descriptive but short: `agentes-claude-code`, `claude-manychat-tutorial`, `flujos-meta-ads`
- Each folder contains the `.html` source files AND the rendered `.png` files side by side
- Naming inside the folder:
  - `cover_v{n}_{descriptor}.html` for cover variations (always generate 3+)
  - `paso_{n}_{descriptor}.html` for step slides
  - `cierre_cta.html` for the closing slide
- Never reuse a folder for a different topic. Never dump outputs into the root of `Outputs/`.

### 3.7 Render pipeline
- Use **`./render.sh {folder}`** to convert all HTMLs in a folder to PNGs
- Do NOT manually script Chrome headless commands — use `render.sh`
- The script handles all the flags (window size, virtual time budget, scale factor)

### 3.8 GitHub pushes require explicit approval
- I can `git init`, stage, commit locally, write READMEs, and configure remotes freely.
- I **must NOT** run `git push` (or any equivalent that publishes to a remote) until the user explicitly tells me to push in the current conversation ("haz el push", "súbelo", "publícalo", etc.).
- A prior approval to push does NOT carry over — every push needs its own green light.

---

## 4. Standard Post Workflow

When the user triggers a new post, follow this sequence **in order**. Do not skip steps. Do not render images before the user approves the breakdown.

### Step 1 — Re-anchor visually (silent, fast)
- Read [Skills/instagram-post-design.md](Skills/instagram-post-design.md) (base system)
- Read [Skills/instagram-cover-design.md](Skills/instagram-cover-design.md)
- Read [Skills/instagram-step-slide-design.md](Skills/instagram-step-slide-design.md)
- Open at least 2 reference images from `Ejemplos/` (the ones most relevant to the layout I'll use)
- Check `memory/MEMORY.md` for any user preferences I should know

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
mkdir -p "Outputs/{topic-slug}"
```
The slug must be kebab-case, ≤4 words.

### Step 6 — Write the HTML files
- Use the scaffolds from the skills as starting points
- Inline all CSS in each file (no external stylesheets — Chrome headless renders these standalone)
- Include the slide indicator footer on every slide (with the correct dot active)
- Use Inter via Google Fonts CDN, JetBrains Mono for any code

### Step 7 — Render with `./render.sh`
```bash
./render.sh Outputs/{topic-slug}
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

---

## 5. When the user reports a visual bug

If the user mentions something is wrong with a slide (or puts marked-up images in `Errors/`):
1. Read the marked images from `Errors/` to see what they circled
2. Identify the root cause in the HTML (don't guess — find the actual SVG/CSS line)
3. Fix it
4. Re-render only the affected slide
5. Verify the fix visually

---

## 6. When the user gives feedback that should outlive this session

If the user says something like *"siempre haz X"* or *"nunca uses Y"* or corrects me on a recurring pattern:
1. Save it as a `feedback` memory in `memory/` (see auto-memory instructions in the system prompt)
2. **Also** update the relevant skill file(s) so the rule lives in two places: memory (cross-session) AND skill (operational)
3. Add a one-line entry to `memory/MEMORY.md`

This is what we did with: Colombian Spanish, double highlight on covers, slide indicator, closing slide pattern.

---

## 7. The skills are the spec — don't improvise

The 3 skill files are the operational ground truth for design decisions. If a user request seems to conflict with a skill, **flag the conflict** before deviating. Example:

> *User: "haz el cover sin highlight"*
> *Me: "El skill dice que los covers usan double highlight por defecto (preferencia tuya validada). ¿Quieres que lo saltemos solo en este post o cambiamos la regla en el skill?"*

The skills are alive — they should evolve with the user's preferences, but only deliberately.
