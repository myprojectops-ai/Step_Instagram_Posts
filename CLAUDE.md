# Visual_posts -- Project Instructions

This project generates **catchy Instagram posts** for **@lucianomusellaa** using the brand visual system documented in [Brand/brand-spec.md](Brand/brand-spec.md). The reference creator @ramiro.cubria is the *visual style inspiration only* -- NOT his handle, NOT his Spanish dialect.

You are operating inside this project. Read this file first whenever a session starts here. Everything below is binding.

> **Brand v2 migration completed 2026-05-22.** The previous cream + coral + Inter visual system was retired. The new brand system (Roboto + Playfair Display Italic, dual-mode palette with three color schemes) lives in [Brand/brand-spec.md](Brand/brand-spec.md). **All `PostTypes/*/Outputs/` from before that date are historical and immutable -- do not re-render them.**

---

## 1. Three post types -- pick the right one

This project supports **three different kinds of posts**, each with its own skills, references, and workflow. Every job belongs to exactly one of these types. Before doing anything else, identify which type the user is asking for, then read **that type's README** to load its workflow.

| Type | Folder | When to use |
|---|---|---|
| **Step-by-step** (paso a paso) | [PostTypes/step-by-step/](PostTypes/step-by-step/) | Tutorials, how-tos, "X pasos para Y", anything where the carousel walks the viewer through a sequence of actions. **This is the most mature type.** |
| **News** (noticias de IA) | [PostTypes/news/](PostTypes/news/) | News posts about AI announcements, model releases, industry events, breaking AI updates. **4-slide carousel** with dark or light editorial photo + headline aesthetic. |
| **Informativos** (hacks / tips) | [PostTypes/informativos/](PostTypes/informativos/) | Standalone informative posts: AI hacks, prompts, tips, lists, infographics, tier lists, cheatsheets. **7 layout patterns** (numbered list, grid cards, tier list, mind map, cheatsheet, hero card, comparison) -- composition + HTML text overlay. |

### Trigger phrases -- how the user kicks off a new post

The user signals their intent with phrases like these (or similar):

**Step-by-step:**
- "nuevo post: {tema}" / "hagamos un post sobre {tema}" / "generemos un carrusel de {tema}" / "quiero un post de {tema}"
- "post paso a paso de {tema}" / "tutorial de {tema}"

**News:**
- "post de noticia: {titular}" / "carrusel de la noticia de {evento}" / "hagamos un post sobre la noticia de {tema}" / "esto salió hoy: {url}"

**Informativos:**
- "post informativo de {tema}" / "post de hacks de {tema}" / "post de tips para {tema}" / "post tipo lista sobre {tema}"

### MANDATORY first move when the user asks for a post

> **ALWAYS ask the user to confirm three things before starting any work: post type, color scheme, and mode.** Phrasings can be ambiguous and the wrong combination wastes a whole job. This is non-negotiable.

The exact question I ask, in one short message:

> *"Para arrancar necesito tres cosas:*
> *(a) Tipo de post: **(1)** step-by-step (tutorial), **(2)** news (noticia de IA), o **(3)** informativo (hack/tip/lista).*
> *(b) Esquema de color: **AMARILLO** (highlights naranjas), **ROJO** (highlights rojos), o **AZUL** (highlights azules).*
> *(c) Modo: **LIGHT** (fondos crema/blanco) o **DARK** (fondos negro/navy)."*

The brand visual system lives in [Brand/brand-spec.md](Brand/brand-spec.md) -- color tokens for each scheme/mode and typography rules are documented there. **Read brand-spec.md once at the start of every session.**

Only after the user confirms type + color + mode, I proceed with the workflow:
1. **Read [Brand/brand-spec.md](Brand/brand-spec.md)** -- canonical palette, fonts, slide patterns.
2. **Read that type's `README.md`** for the workflow and the list of skills to load.
3. **Read the skill files** that the README points to.
4. **MANDATORY visual re-anchoring** (see section 1.5 below) -- review templates in `Brand/Templates/{Tutorial|Noticias}/`, plus inspiration AND past favorites before generating anything.
5. **Follow the workflow** for that type -- never improvise the order, never skip steps.

---

## 1.5 Visual re-anchoring -- MANDATORY before EVERY post (all types)

> **Before generating any HTML for any post, regardless of type, I must always review THREE sources:**
>
> - **`Brand/Templates/{Tutorial|Noticias}/{COLOR}/{MODE}/`** -- canonical brand templates that match the user's chosen color + mode. **These are the visual ground truth** -- read at least 2 PNGs that match the exact color+mode combo.
> - **`PostTypes/{type}/Inspiracion/`** -- external references the user has dropped in. **Always check for new images here vs. what I've seen before.**
> - **`PostTypes/{type}/Favoritos_Claude_Generated/`** -- slides I generated in past sessions that the user explicitly marked as favorites. Strongest signal of "this works for me."

### Why this is mandatory

The whole point of having three sources is to keep posts feeling **fresh but on-brand**. Without re-anchoring, my outputs converge on the same patterns over and over and the feed feels repetitive. The user has been explicit: posts should follow the same aesthetic but should NOT all look the same. Variety is **essential**, not optional.

### What "review" means in practice

For every new post:
1. **Brand/Templates/** -- always start here. Open the subfolder matching the user's choice and read at least 2 PNGs. These define spacing, font sizing, layout proportions for the chosen variant.
2. **Inspiracion** -- list the folder (catch any newly added references), then read at least 2 images. Prefer images I haven't viewed in recent jobs to maximize the spread of patterns I'm pulling from.
3. **Favoritos_Claude_Generated** -- list the folder, then read every image inside. If empty, that's fine -- just note it.
4. **Synthesize** -- explicitly hold all three inputs in mind while drafting the breakdown. Vary at least one structural element vs. the most recent post in the same type so the new post doesn't visually rhyme with the previous one.

### When I'm allowed to skip

Never. Even for tiny iterations on an existing post (re-rendering one slide), I don't need to re-review -- but for any **new** post I do.

---

## 1.6 After every post -- capture user favorites

> **At the end of every post run, I must ask the user which generated images are their favorites and save them to `Favoritos_Claude_Generated/` for that post type.**

### Exact question to ask

After presenting the rendered carousel, I always ask:

> *"¿Cuáles imágenes de este post son tus favoritas? Las guardo en `Favoritos_Claude_Generated/` para usar como referencia en posts futuros."*

### What to do with the answer

- If the user names specific slides (e.g. "el cover v1 y el paso 3"), **copy** those PNGs from `PostTypes/{type}/Outputs/{topic-slug}/` to `PostTypes/{type}/Favoritos_Claude_Generated/`. Filename pattern: `{topic-slug}_{original-name}.png`.
- If the user says "ninguna" or skips, that's fine -- don't save anything, but still ask.
- If the user says "todas", copy all the rendered PNGs of that post.
- **Use `cp` (copy), not `mv` (move)** -- originals stay in their folder; favorites are an additive curated library.

---

## 2. Project map

```
Visual_posts/
|-- CLAUDE.md                          <- this file (autoloaded, the router)
|-- README.md                          <- project intro
|-- Brand/                             <- CANONICAL brand system (v2)
|   |-- brand-spec.md                  <- single source of truth: palette, fonts, slide patterns
|   |-- Colores/COLORES.pdf            <- visual palette reference (PDF)
|   |-- Fonts/
|   |   |-- Roboto/                    <- primary font (TTFs, loaded via @font-face)
|   |   `-- PlayfairDisplay/           <- emphasis font (Italic only)
|   `-- Templates/
|       |-- Tutorial/                  <- 45 reference PNGs by color x style x mode
|       `-- Noticias/                  <- 24 reference PNGs by color x mode
|-- Skills/                            <- global skills (apply to ALL post types)
|   |-- visual-qa.md                   <- MANDATORY post-render QA
|   |-- slide-spacing.md               <- MANDATORY spacing/layout rules
|   `-- informativo-visual-iteration.md <- self-iteration loop for informativo compositions
|-- PostTypes/
|   |-- step-by-step/                  <- tutorial / how-to carousels
|   |   |-- README.md                  <- workflow + triggers + folder rules
|   |   |-- Skills/
|   |   |   |-- instagram-post-design.md       <- BASE visual system (read FIRST)
|   |   |   |-- instagram-cover-design.md      <- cover/thumbnail layouts
|   |   |   |-- instagram-step-slide-design.md <- step slides + closing slide
|   |   |   `-- instagram-dark-mode.md         <- dark mode palette overrides
|   |   |-- Inspiracion/               <- external visual references
|   |   |-- Favoritos_Claude_Generated/ <- past slides the user marked as favorites
|   |   `-- Outputs/                   <- rendered carousels (one folder per post)
|   |-- news/                          <- AI news posts (4-slide carousel)
|   |   |-- README.md
|   |   |-- Skills/
|   |   |   `-- news-post-design.md    <- 4-slide news carousel visual system
|   |   |-- Inspiracion/
|   |   |-- Favoritos_Claude_Generated/
|   |   `-- Outputs/
|   `-- informativos/                  <- hacks / tips / infographics
|       |-- README.md                  <- workflow + triggers + layout patterns
|       |-- Skills/
|       |   `-- informativo-post-design.md <- 7-layout visual system
|       |-- Inspiracion/
|       |-- Favoritos_Claude_Generated/
|       `-- Outputs/
|-- Logos/                             <- shared brand assets
|   |-- Claude_AI_symbol.svg
|   |-- Alta_Studio_logo.png           <- Alta Studio logo (use on LIGHT mode)
|   |-- Alta_Studio_logo_white.png     <- white variant (use on DARK mode)
|   `-- (OpenAI, Perplexity, SAP, Amazon, etc. third-party logos)
|-- Assets/
|   |-- Fonts/                         <- LEGACY (Inter family) -- not used by v2 brand
|   `-- Personas/                      <- real person photos (CEOs, founders)
|-- Errors/                            <- user marks visual bugs here for me to fix
|-- render.sh                          <- HTML->PNG batch renderer (use this, not raw chrome)
`-- (persistent memories at ~/.claude/projects/c--Trabajo-AI-Visual-posts/memory/)
```

---

## 3. Brand-wide non-negotiable rules (apply to ALL post types)

These are project-wide invariants. Each post type's skills extend these rules with type-specific patterns -- they never contradict them.

### 3.1 Brand handle
- The handle on top of every slide (when applicable -- e.g. tutorial covers and informativos bottom) is **`@lucianomusellaa`** (double "a")
- Never `@ramiro.cubria` -- that's only the visual reference creator
- **News posts do NOT use the handle AND do NOT use any logo.** The top-left corner is intentionally empty -- editorial magazine look. The brand identity comes through typography (Roboto + Playfair Italic) and color scheme.

### 3.2 Spanish dialect
- **Colombian Spanish, `tú` form** -- never Argentinian voseo
- Yes: Crea, Define, Instala, Convierte, Delega, Desliza, Guarda, Usa, tú, tienes, quieres
- No: Creá, Definí, Instalá, Convertí, Delegá, Deslizá, Guardá, Usá, vos, tenés, querés
- Reflexive imperatives keep the accent: `instálalo`, `arráncalo`, `guárdalo`
- Full conversion table is in [PostTypes/step-by-step/Skills/instagram-post-design.md](PostTypes/step-by-step/Skills/instagram-post-design.md)

### 3.3 Visual system

**All color, typography, and slide-pattern decisions live in [Brand/brand-spec.md](Brand/brand-spec.md).** Read that file at the start of every session. The TL;DR:

- **Canvas:** 1080 × 1350 px (4:5 portrait, Instagram feed optimal)
- **Color schemes:** AMARILLO (orange highlights), ROJO (red), AZUL (blue) -- ask user per post.
- **Modes:** LIGHT (cream/white bg) or DARK (black/navy bg) -- ask user per post.
- **Fonts:** Roboto (400/500/700/900) for body+headings; Playfair Display **Italic only** for 1-2 emphasis words per headline.
- **No page dots** -- Instagram adds them natively for carousels. Do not add dot indicators to slides.

If a skill contradicts brand-spec.md, brand-spec.md wins -- update the skill.

### 3.4 Render pipeline
- Use **`./render.sh {folder}`** to convert all HTMLs in a folder to PNGs. The folder path is relative to the project root, e.g. `./render.sh PostTypes/step-by-step/Outputs/agentes-claude-v2`.
- Single-file mode also works: `./render.sh PostTypes/step-by-step/Outputs/agentes-claude-v2/cover_v1_delega.html`
- Do NOT manually script Chrome headless commands -- use `render.sh`.
- The script handles all the flags (window size, virtual time budget, scale factor) and Git Bash -> Windows path conversion.
- **Viewport bug fix:** Chrome headless on Windows subtracts ~96px from `--window-size` height. `render.sh` uses `--window-size=1098,1550` and crops to exact 1080×1350 via PIL. Content at y>1272 (footer pills, taglines) will be cut off if the viewport is too small. Always verify bottom elements render.
- **After every render, run the [Visual QA skill](Skills/visual-qa.md)** -- open and inspect every PNG before presenting it to the user. Mandatory for ALL post types. Never describe a feature you can't visually confirm in the rendered output.
- **Before writing any slide's HTML AND during QA, apply the [Slide Spacing skill](Skills/slide-spacing.md)** -- content fills ~70-85% of usable canvas, never leave >150px empty in the middle or >120px at the bottom outside safe zone.

### 3.5 Image generation -- Higgsfield MCP (sole image generator)

> **As of brand v2 migration (2026-05-22), all AI image generation goes through the Higgsfield MCP.** The previous Codex/gpt-image-1 path is deprecated. Do not reference, call, or attempt to use any other image generator.

**Setup (one-time per machine):**
```
claude mcp add --transport http --scope user higgsfield https://mcp.higgsfield.ai/mcp
```
First tool invocation opens browser-based OAuth -- log in with the existing paid Higgsfield account.

**Tools exposed (typical MCP naming):**
- `mcp__higgsfield__generate_image` -- single image generation (Soul 2.0 / Nano Banana Pro / Flux 2 / etc.)
- `mcp__higgsfield__generate_video` -- video generation (not used in this project today)
- `mcp__higgsfield__balance` -- check remaining credits
- (verify exact names after authentication; the prefix `mcp__higgsfield__` is conventional)

**When to use it (by post type):**

| Post type | Image generation use |
|---|---|
| **Step-by-step** | Only for missing logos. All other slide content is HTML+CSS+inline SVG (Tutorial templates require precise layout, terminal mockups, code, etc.). |
| **News** | **Single-step generation per slide, 100% Higgsfield.** Prompt `nano_banana_pro` at `resolution: "2k"` with ALL text, stats, headlines, eyebrows, bullet dots, comparison cards, layout structure baked into the prompt. **News slides have NO Alta Studio logo and NO `@lucianomusellaa` handle.** Each prompt explicitly instructs "the top-left corner MUST be completely empty -- no logo, no symbol, no mark". After generation: download + resize to 1080×1350 (PIL LANCZOS) and that's the final deliverable. No HTML overlay, no PIL paste, no post-processing of any kind. Verify spelling on every slide; regenerate if typos appear. ~8 credits per 4-slide carousel. |
| **Informativos** | **Single-step generation, 100% Higgsfield.** nano_banana_pro at 2k with ALL text baked into the prompt (title, item names, descriptions, `@lucianomusellaa` handle at bottom). No HTML overlay, no PIL paste. ~2 credits per post. |

**Prompt anatomy (Higgsfield Soul 2.0 favors descriptive long-form prompts):**
```
[SUBJECT — specific noun + adjectives]
[STYLE — editorial / cinematic / minimalist / photoreal etc.]
[COMPOSITION — framing, depth, angle]
[LIGHTING — natural, studio, dramatic, golden hour, etc.]
[PALETTE — limit to brand-friendly tones; avoid colors that clash with the chosen mode]
[NEGATIVE — "no text", "no logos", "no watermarks"]
[ASPECT RATIO — explicit, e.g. --ar 4:5, --ar 16:9, --ar 1:1]
[SEED — same seed across slides of one carousel for stylistic consistency]
```

Full prompt templates and per-slot recipes live in [Brand/brand-spec.md §4](Brand/brand-spec.md).

**Anti-patterns:**
- Do NOT ask Higgsfield to render text inside an image (typography is HTML's job).
- Do NOT ask for a logo of a real brand if it's already in `Logos/` -- use the existing file.
- Do NOT use prompts under 15 words -- Soul produces generic results.
- Do NOT fall back to any other image API silently. If Higgsfield is unreachable, ask the user.

### 3.5.1 Brand logos and person photos -- sourcing hierarchy

For **step-by-step** posts, logos MUST come from the `Logos/` folder first. If a logo is missing, generate it with Higgsfield, save to `Logos/`, and present for user review before using.

For **news and informativos** posts, follow this order:
1. **Check `Logos/` and `Assets/Personas/` first** -- if the real asset exists, always prefer it.
2. **If not available -> generate with Higgsfield MCP.**
3. **Save generated logos** to `Logos/` and **generated person photos** to `Assets/Personas/` so they're reusable across future posts.
4. **Present to user for review** -- they approve before it goes into the slide.
5. **Never silently skip a visual asset** -- either use an existing one or generate one.

**SVG embedding tip:** for `.svg` files in `Logos/`, prefer inlining the `<svg>...</svg>` content directly into the HTML -- this avoids path resolution issues with headless Chrome and gives full CSS control over fill/stroke colors.

**Content policy note:** Higgsfield's Soul 2.0 handles named real people more permissively than gpt-image-1 did, but the same legal/ethics rules apply. For news photos of public figures, generate generic-looking imagery and lean on context, OR use a real photo from `Assets/Personas/` when available.

### 3.6 Output folder structure (dated + auto-pruned to last 5 per type)

- **Every post lives in its own folder** under its type's `Outputs/`, named **`YYYY-MM-DD_{topic-slug}/`**. The date prefix is mandatory.
- Example: `PostTypes/news/Outputs/2026-05-24_opus-4-7/`, `PostTypes/step-by-step/Outputs/2026-05-24_agentes-claude-code/`.
- Slug part: kebab-case, descriptive but short (≤4 words).
- Each folder contains the rendered `.png` files (and any source files like `.html` for step-by-step, `caption.txt`, etc.) side by side.
- Never reuse a folder for a different topic. Never dump outputs into the root of `Outputs/`.

**Auto-prune to last 5 posts per type:**
- After creating a new post folder (and after the user has confirmed favorites), run:
  ```
  python Brand/prune_outputs.py {step-by-step|news|informativos}
  ```
- The script keeps the 5 most-recent dated folders and **deletes the rest** (`rm -rf`). This prevents `Outputs/` from accumulating indefinitely.
- The script uses lexicographic sort on the `YYYY-MM-DD_` prefix → newest first → keep top 5 → delete tail.
- **Folders WITHOUT a date prefix are NEVER touched** by the prune. This protects historical pre-migration outputs (e.g. `agentes-claude-code/`, `allbirds-pivote-ia/`) and the `Favoritos_Claude_Generated/` folder.
- If the user marks a post as favorite (CLAUDE.md §1.6), the favorites are copied to `Favoritos_Claude_Generated/` BEFORE the prune runs. So a favorited slide is preserved even when its source `Outputs/` folder gets pruned later.
- To change the keep limit for a one-off: `python Brand/prune_outputs.py news 10` keeps the last 10 instead of 5. Default stays at 5.

### 3.7 GitHub pushes require explicit approval
- I can `git init`, stage, commit locally, write READMEs, and configure remotes freely.
- I **must NOT** run `git push` (or any equivalent that publishes to a remote) until the user explicitly tells me to push in the current conversation ("haz el push", "súbelo", "publícalo", etc.).
- A prior approval to push does NOT carry over -- every push needs its own green light.

### 3.8 Outputs lifecycle (dated naming + last-5 rolling window)

- All historical pre-migration outputs were cleaned on 2026-05-24. The Outputs/ tree now contains only posts created under brand v2.
- **New convention:** every post lives in `PostTypes/{type}/Outputs/YYYY-MM-DD_{topic-slug}/`. See §3.6 for the dated-folder rule.
- **Auto-prune** keeps only the 5 most-recent dated folders per type. Favorites are saved separately in `Favoritos_Claude_Generated/` BEFORE the prune runs, so they survive deletion of their source folder.
- If a user wants to revisit an older post and it's been pruned, recovery options: (a) check `Favoritos_Claude_Generated/` if any slide was favorited, (b) check `git log` to find the commit when it was generated and restore from there, (c) re-generate from scratch using the original brief if available.

---

## 4. When the user reports a visual bug

If the user mentions something is wrong with a slide (or puts marked-up images in `Errors/`):
1. Read the marked images from `Errors/` to see what they circled
2. Identify the root cause in the HTML (don't guess -- find the actual SVG/CSS line)
3. Fix it
4. Re-render only the affected slide
5. Verify the fix visually

---

## 5. When the user gives feedback that should outlive this session

If the user says something like *"siempre haz X"* or *"nunca uses Y"* or corrects me on a recurring pattern:
1. Save it as a `feedback` memory in `~/.claude/projects/c--Trabajo-AI-Visual-posts/memory/`
2. **Also** update the relevant skill file(s) -- and if it's a brand-level rule, update `Brand/brand-spec.md`
3. Add a one-line entry to `~/.claude/projects/c--Trabajo-AI-Visual-posts/memory/MEMORY.md`

Examples of feedback already captured: Colombian Spanish, no page dots, color+mode per post, Higgsfield as sole image generator, Outputs/ immutable.

---

## 6. The skills are the spec -- don't improvise

Skill files and `Brand/brand-spec.md` are the operational ground truth. If a user request seems to conflict with a skill or the brand spec, **flag the conflict** before deviating. Example:

> *User: "haz el cover sin highlight"*
> *Me: "El brand-spec dice que los covers llevan 1-2 palabras en Playfair Italic accent. ¿Lo saltamos solo en este post o cambiamos la regla en el spec?"*

The skills are alive -- they should evolve with the user's preferences, but only deliberately.
