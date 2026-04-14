# Visual_posts — Project Instructions

This project generates **catchy Instagram posts** for **@lucianomusellaa** using a defined visual system inspired by AI content creators (reference: @ramiro.cubria — visual style only, NOT his handle, NOT his Spanish dialect).

You are operating inside this project. Read this file first whenever a session starts here. Everything below is binding.

---

## 1. Three post types — pick the right one

This project supports **three different kinds of posts**, each with its own skills, references, and workflow. Every job belongs to exactly one of these types. Before doing anything else, identify which type the user is asking for, then read **that type's README** to load its workflow.

| Type | Folder | When to use |
|---|---|---|
| **Step-by-step** (paso a paso) | [PostTypes/step-by-step/](PostTypes/step-by-step/) | Tutorials, how-tos, "X pasos para Y", anything where the carousel walks the viewer through a sequence of actions. **This is the most mature type — its skills are complete.** |
| **News** (noticias de IA) | [PostTypes/news/](PostTypes/news/) | News posts about AI announcements, model releases, industry events, breaking AI updates. **Skills are ready** — single-image dark editorial style with real person photos. |
| **Informativos** (hacks / tips) | [PostTypes/informativos/](PostTypes/informativos/) | Standalone informative posts: AI hacks, prompts, tips, lists, infographics, tier lists, cheatsheets. **Skills are ready** — dense infographic style with 7 layout patterns (numbered list, grid cards, tier list, mind map, cheatsheet, hero card, comparison). |

### Trigger phrases — how the user kicks off a new post

The user signals their intent with phrases like these (or similar):

**Step-by-step:**
- "nuevo post: {tema}" / "hagamos un post sobre {tema}" / "generemos un carrusel de {tema}" / "quiero un post de {tema}"
- "post paso a paso de {tema}" / "tutorial de {tema}"

**News:**
- "post de noticia: {titular}" / "carrusel de la noticia de {evento}" / "hagamos un post sobre la noticia de {tema}" / "esto salió hoy: {url}"

**Informativos:**
- "post informativo de {tema}" / "post de hacks de {tema}" / "post de tips para {tema}" / "post tipo lista sobre {tema}"

### MANDATORY first move when the user asks for a post

> **ALWAYS ask the user to confirm the post type before starting any work**, even when the trigger phrase strongly suggests one type. Phrasings can be ambiguous and the wrong type wastes a whole job. This is non-negotiable.

The exact question I ask, in one short message:

> *"¿Qué tipo de post hacemos? **(1)** step-by-step (tutorial paso a paso), **(2)** news (noticia de IA), o **(3)** informativo (hack/tip/lista)."*

Only after the user confirms the type, I proceed with the workflow:
1. **Read that type's `README.md`** for the workflow and the list of skills to load.
2. **Read the skill files** that the README points to.
3. **MANDATORY visual re-anchoring** (see section 1.5 below) — review inspiration AND past favorites before generating anything.
4. **Follow the workflow** for that type — never improvise the order, never skip steps.

---

## 1.5 Visual re-anchoring — MANDATORY before EVERY post (all types)

> **Before generating any HTML for any post, regardless of type, I must always review BOTH of the following folders for the post type at hand:**
>
> - **`PostTypes/{type}/Inspiracion/`** — external references the user has dropped in (creators they admire, layouts they want me to learn from). **Always check for new images here vs. what I've seen before.**
> - **`PostTypes/{type}/Favoritos_Claude_Generated/`** — slides I generated in past sessions that the user explicitly marked as favorites. These are the strongest signal of "this works for me."

### Why this is mandatory

The whole point of having both folders is to keep posts feeling **fresh but on-brand**. Without re-anchoring, my outputs converge on the same patterns over and over and the feed feels repetitive. The user has been explicit: posts should follow the same aesthetic but should NOT all look the same. Variety is **essential**, not optional.

### What "review" means in practice

For every new post:
1. **Inspiracion** — list the folder (catch any newly added references), then read at least 2 images. Prefer images I haven't viewed in recent jobs to maximize the spread of patterns I'm pulling from.
2. **Favoritos_Claude_Generated** — list the folder, then read every image inside (it's the user's curated "best of" list). If empty, that's fine — just note it.
3. **Synthesize** — explicitly hold both inputs in mind while drafting the breakdown. Vary at least one structural element vs. the most recent post in the same type (different cover layout, different visual element, different hook structure, etc.) so the new post doesn't visually rhyme with the previous one.

### When I'm allowed to skip

Never. Even for tiny iterations on an existing post (re-rendering one slide), I don't need to re-review — but for any **new** post I do.

---

## 1.6 After every post — capture user favorites

> **At the end of every post run, I must ask the user which generated images are their favorites and save them to `Favoritos_Claude_Generated/` for that post type.**

### Exact question to ask

After presenting the rendered carousel (step 9 of the step-by-step workflow, or the equivalent in other types), I always ask:

> *"¿Cuáles imágenes de este post son tus favoritas? Las guardo en `Favoritos_Claude_Generated/` para usar como referencia en posts futuros."*

### What to do with the answer

- If the user names specific slides (e.g. "el cover v1 y el paso 3"), **copy** those PNGs from `PostTypes/{type}/Outputs/{topic-slug}/` to `PostTypes/{type}/Favoritos_Claude_Generated/`. Use a descriptive filename: `{topic-slug}_{original-name}.png` so it's clear what post it came from.
- If the user says "ninguna" or skips, that's fine — don't save anything, but still ask. Their answer is data either way.
- If the user says "todas", copy all the rendered PNGs of that post.
- **Use `cp` (copy), not `mv` (move)** — the original outputs stay in their folder; favorites are an additive curated library.

---

## 2. Project map

```
Visual_posts/
├── CLAUDE.md                          ← this file (autoloaded — the router)
├── README.md                          ← project intro
├── Skills/                            ← global skills (apply to ALL post types)
│   └── visual-qa.md                   ← MANDATORY post-render QA — verify every PNG before presenting
├── PostTypes/
│   ├── step-by-step/                  ← tutorial / how-to carousels (mature)
│   │   ├── README.md                  ← workflow + triggers + folder rules for this type
│   │   ├── Skills/
│   │   │   ├── instagram-post-design.md       ← BASE visual system (read FIRST)
│   │   │   ├── instagram-cover-design.md      ← cover/thumbnail layouts
│   │   │   └── instagram-step-slide-design.md ← step slides + closing slide
│   │   ├── Inspiracion/               ← external visual references (drop new ones here)
│   │   ├── Favoritos_Claude_Generated/ ← past slides the user marked as favorites
│   │   └── Outputs/                   ← rendered carousels (one folder per post)
│   ├── news/                          ← AI news posts (ready)
│   │   ├── README.md
│   │   ├── Skills/
│   │   │   └── news-post-design.md    ← visual system for dark editorial news posts
│   │   ├── Inspiracion/               ← (empty — drop reference images here)
│   │   ├── Favoritos_Claude_Generated/ ← (empty — populated as user marks favorites)
│   │   └── Outputs/
│   └── informativos/                  ← hacks / tips / infographics (ready)
│       ├── README.md                  ← workflow + triggers + layout patterns
│       ├── Skills/
│       │   └── informativo-post-design.md ← visual system (7 layouts, scaffolds, palette)
│       ├── Inspiracion/               ← 13 external visual references
│       ├── Favoritos_Claude_Generated/ ← past slides the user marked as favorites
│       └── Outputs/                   ← rendered informativo posts
├── Logos/                             ← shared brand assets across all post types
│   ├── Claude_AI_symbol.svg
│   ├── Alta_Studio_logo.png           ← Alta Studio logo (dark version)
│   └── Alta_Studio_Logo_fondoneutro.png ← Alta Studio logo (blue/glow version)
├── Assets/                            ← shared user-provided screenshots / images
│   └── Personas/                      ← real person photos (CEOs, founders) — global
├── Errors/                            ← user marks visual bugs here for me to fix
├── render.sh                          ← HTML→PNG batch renderer (use this, not raw chrome)
├── generate-image.py                  ← Nano Banana 2 (Gemini API) image generator
├── .env                               ← GEMINI_API_KEY lives here (git-ignored)
└── memory/                            ← persistent user/feedback memories (auto-loaded)
```

---

## 3. Brand-wide non-negotiable rules (apply to ALL post types)

These are project-wide invariants. They live across every post type, every slide, every iteration. Each post type's skills extend these rules with type-specific patterns — they never contradict them.

### 3.1 Brand handle
- The handle on top of every slide is **`@lucianomusellaa`** (double "a")
- Never `@ramiro.cubria` — that's only the visual reference creator

### 3.2 Spanish dialect
- **Colombian Spanish, `tú` form** — never Argentinian voseo
- ✅ Crea, Define, Instala, Convierte, Delega, Desliza, Guarda, Usa, tú, tienes, quieres
- ❌ Creá, Definí, Instalá, Convertí, Delegá, Deslizá, Guardá, Usá, vos, tenés, querés
- Reflexive imperatives keep the accent: `instálalo`, `arráncalo`, `guárdalo`
- Full conversion table is in [PostTypes/step-by-step/Skills/instagram-post-design.md](PostTypes/step-by-step/Skills/instagram-post-design.md) section 3.5

### 3.3 Visual system (cream + coral + yellow + grid)
- Background: cream `#F5F2ED` (NOT pure white) with subtle grid `#E8E4DD`
- Primary text: `#0E0E0E`
- Accent coral: `#E85D3C`
- Highlight yellow: `#FFE45C`
- Canvas: 1080×1350 px (4:5 portrait)
- Font: Inter (500/600/700/800), JetBrains Mono for code

### 3.4 Render pipeline
- Use **`./render.sh {folder}`** to convert all HTMLs in a folder to PNGs. The folder path is relative to the project root, e.g. `./render.sh PostTypes/step-by-step/Outputs/agentes-claude-v2`.
- Single-file mode also works: `./render.sh PostTypes/step-by-step/Outputs/agentes-claude-v2/cover_v1_delega.html`
- Do NOT manually script Chrome headless commands — use `render.sh`
- The script handles all the flags (window size, virtual time budget, scale factor) and Git Bash → Windows path conversion
- **After every render, run the [Visual QA skill](Skills/visual-qa.md)** — open and inspect every PNG before presenting it to the user. This is mandatory for ALL post types. Never describe a feature you can't visually confirm in the rendered output.

### 3.5 Image generation — hybrid approach (by post type)

This project uses **two image generation methods** depending on the post type:

| Post type | Method | Visual assets (logos, personas, backgrounds) |
|---|---|---|
| **Step-by-step** | HTML + CSS + inline SVG | Logos from `Logos/`; **Nano Banana 2 ONLY for missing logos** — nothing else |
| **News** | **Nano Banana 2 full composition** + PIL text overlay | Nano Banana generates the COMPLETE visual (person + logo + atmosphere) as one image; PIL only adds text (badge, headline, watermark) |
| **Informativos** | **Nano Banana 2 full composition** + HTML text overlay | Nano Banana generates the COMPLETE visual (background, layout structure, icons, logos, decorative elements — NO text); HTML overlay adds all text |

#### Step-by-step posts (Nano Banana ONLY for missing logos)
- All slides are **HTML + CSS + inline SVG**, rendered to PNG via `render.sh`.
- If a slide needs imagery beyond text, recreate it with elaborate inline SVG.
- Logos come from `Logos/` (real assets uploaded by the user).
- **If a needed logo is NOT in `Logos/`** → generate it with Nano Banana 2 via `generate-image.py`, save to `Logos/`, and present to the user for review before using it.
- **Nano Banana is strictly limited to logo generation in this post type.** Do NOT use it for backgrounds, illustrations, person photos, or any other asset — that would burn API budget for no gain. Everything else stays HTML + CSS + inline SVG.

#### News posts (Nano Banana FULL COMPOSITION + HTML text overlay)
- **Nano Banana 2 generates the complete visual composition** — person photo, brand logo, dark atmosphere, lighting — all as ONE cohesive image. This replaced the old approach of composing photos + logos in HTML/CSS, which produced "pasted-looking" results.
- **HTML is used ONLY for text** — the "AI NEWS" badge, headline, source attribution, and Alta Studio watermark. These are better handled by HTML for pixel-perfect typography.
- **Workflow for news compositions:**
  1. Check `Assets/Personas/` for existing reference photos (useful for `--reference` mode)
  2. Craft a detailed composition prompt (person + logo integration + dark atmosphere + dark bottom for text)
  3. Generate 2–3 composition variants with `generate-image.py --model gemini-3-pro-image-preview --aspect-ratio 4:5`
  4. Present compositions to user for review — they choose which to use
  5. Generate HTML text overlay on top of the approved composition
  6. Render via `render.sh`
- See `PostTypes/news/Skills/news-post-design.md` section 4 for detailed prompting guidelines.

#### Informativos posts (Nano Banana FULL COMPOSITION + HTML text overlay)
- **Nano Banana 2 generates the complete visual composition** — background, layout structure (cards, tiers, grids, mind-map nodes), decorative elements, icons, brand logos — all as ONE cohesive image. This replaced the old HTML+CSS+SVG approach, which couldn't achieve the editorial richness of the inspiration images.
- **HTML is used ONLY for text** — titles, item names, descriptions, numbers, handle, footer. HTML uses the composition as `background-image` and positions text to align with the visual structure.
- **Workflow for informativos compositions:**
  1. Choose layout pattern (A–G) and craft a detailed composition prompt (see skill file section 4)
  2. Check `Logos/` and `Assets/` for existing brand assets (use `--reference` if available)
  3. Generate ONE composition with `generate-image.py --model gemini-3-pro-image-preview --aspect-ratio 4:5`
  4. Present composition to user for review — only regenerate if rejected
  5. Generate HTML text overlay on top of the approved composition
  6. Render via `render.sh`
- See `PostTypes/informativos/Skills/informativo-post-design.md` section 4 for detailed prompting guidelines and layout templates.
- **The script:** `python generate-image.py --prompt "..." --output path/to/output.png`
  - Add `--model gemini-3-pro-image-preview` for maximum quality (compositions, logos, portraits)
  - Add `--aspect-ratio 4:5` for full-slide compositions
  - Add `--reference input.png` for style transfer / editing
  - See `generate-image.py --help` for all options
- **Default model:** `gemini-3.1-flash-image-preview` (Nano Banana 2) for all image generation
- **Requires:** `pip install google-genai` and a valid `GEMINI_API_KEY` in `.env`

#### Prompt guidelines for Nano Banana
- **Logos:** be specific about the brand, style, and background. E.g. "Official OpenAI logo, clean vector style, white background, high resolution"
- **Person photos:** describe the person and context. E.g. "Professional headshot of Sam Altman, CEO of OpenAI, wearing a grey t-shirt, neutral background, editorial photography style"
- **Backgrounds/textures:** describe the mood and palette. E.g. "Abstract dark background with subtle blue circuit patterns, futuristic AI aesthetic, 1080x1350"
- **Illustrations:** describe the concept clearly. E.g. "Minimalist illustration of a brain connected to a neural network, clean lines, coral and cream color palette"

### 3.5.1 Brand logos and person photos — sourcing hierarchy

For **step-by-step** posts, logos MUST come from the `Logos/` folder first. If a logo is missing → generate it with Nano Banana 2 (`generate-image.py`), save to `Logos/`, and present for user review. **Nano Banana is ONLY allowed for logos in step-by-step — never for backgrounds, illustrations, or any other asset.**

For **news and informativos** posts, follow this order:
1. **Check `Logos/` and `Assets/Personas/` first** — if the real asset exists, always prefer it
2. **If not available → generate with Nano Banana** via `generate-image.py`
3. **Save generated logos** to `Logos/` and **generated person photos** to `Assets/Personas/` so they're reusable across future posts
4. **Present to user for review** — they approve before it goes into the slide
5. **Never silently skip a visual asset** — either use an existing one or generate one. Every brand/person mentioned in the post should have its visual.

**SVG embedding tip (for existing assets):** for `.svg` files in `Logos/`, prefer inlining the `<svg>...</svg>` content directly into the HTML — this avoids path resolution issues with headless Chrome and gives full CSS control over fill/stroke colors.

### 3.6 Output folder structure
- **Every post lives in its own folder** under its type's `Outputs/`, e.g. `PostTypes/step-by-step/Outputs/{topic-slug}/`
- The slug is kebab-case, descriptive but short: `agentes-claude-code`, `claude-manychat-tutorial`, `flujos-meta-ads`
- Each folder contains the `.html` source files AND the rendered `.png` files side by side
- Never reuse a folder for a different topic. Never dump outputs into the root of `Outputs/`.
- Per-type naming conventions live in each type's `README.md`.

### 3.7 GitHub pushes require explicit approval
- I can `git init`, stage, commit locally, write READMEs, and configure remotes freely.
- I **must NOT** run `git push` (or any equivalent that publishes to a remote) until the user explicitly tells me to push in the current conversation ("haz el push", "súbelo", "publícalo", etc.).
- A prior approval to push does NOT carry over — every push needs its own green light.

---

## 4. When the user reports a visual bug

If the user mentions something is wrong with a slide (or puts marked-up images in `Errors/`):
1. Read the marked images from `Errors/` to see what they circled
2. Identify the root cause in the HTML (don't guess — find the actual SVG/CSS line)
3. Fix it
4. Re-render only the affected slide
5. Verify the fix visually

---

## 5. When the user gives feedback that should outlive this session

If the user says something like *"siempre haz X"* or *"nunca uses Y"* or corrects me on a recurring pattern:
1. Save it as a `feedback` memory in `memory/` (see auto-memory instructions in the system prompt)
2. **Also** update the relevant skill file(s) so the rule lives in two places: memory (cross-session) AND skill (operational)
3. Add a one-line entry to `memory/MEMORY.md`

This is what we did with: Colombian Spanish, double highlight on covers, slide indicator, closing slide pattern.

---

## 6. The skills are the spec — don't improvise

Each post type's skill files are the operational ground truth for that type's design decisions. If a user request seems to conflict with a skill, **flag the conflict** before deviating. Example:

> *User: "haz el cover sin highlight"*
> *Me: "El skill dice que los covers usan double highlight por defecto (preferencia tuya validada). ¿Quieres que lo saltemos solo en este post o cambiamos la regla en el skill?"*

The skills are alive — they should evolve with the user's preferences, but only deliberately.
