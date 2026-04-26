# Visual_posts â€” Project Instructions

This project generates **catchy Instagram posts** for **@lucianomusellaa** using a defined visual system inspired by AI content creators (reference: @ramiro.cubria â€” visual style only, NOT his handle, NOT his Spanish dialect).

You are operating inside this project. Read this file first whenever a session starts here. Everything below is binding.

---

## 1. Three post types â€” pick the right one

This project supports **three different kinds of posts**, each with its own skills, references, and workflow. Every job belongs to exactly one of these types. Before doing anything else, identify which type the user is asking for, then read **that type's README** to load its workflow.

| Type | Folder | When to use |
|---|---|---|
| **Step-by-step** (paso a paso) | [PostTypes/step-by-step/](PostTypes/step-by-step/) | Tutorials, how-tos, "X pasos para Y", anything where the carousel walks the viewer through a sequence of actions. **This is the most mature type â€” its skills are complete.** |
| **News** (noticias de IA) | [PostTypes/news/](PostTypes/news/) | News posts about AI announcements, model releases, industry events, breaking AI updates. **Skills are ready** â€” single-image dark editorial style with real person photos. |
| **Informativos** (hacks / tips) | [PostTypes/informativos/](PostTypes/informativos/) | Standalone informative posts: AI hacks, prompts, tips, lists, infographics, tier lists, cheatsheets. **Skills are ready** â€” dense infographic style with 7 layout patterns (numbered list, grid cards, tier list, mind map, cheatsheet, hero card, comparison). |

### Trigger phrases â€” how the user kicks off a new post

The user signals their intent with phrases like these (or similar):

**Step-by-step:**
- "nuevo post: {tema}" / "hagamos un post sobre {tema}" / "generemos un carrusel de {tema}" / "quiero un post de {tema}"
- "post paso a paso de {tema}" / "tutorial de {tema}"

**News:**
- "post de noticia: {titular}" / "carrusel de la noticia de {evento}" / "hagamos un post sobre la noticia de {tema}" / "esto saliÃ³ hoy: {url}"

**Informativos:**
- "post informativo de {tema}" / "post de hacks de {tema}" / "post de tips para {tema}" / "post tipo lista sobre {tema}"

### MANDATORY first move when the user asks for a post

> **ALWAYS ask the user to confirm the post type before starting any work**, even when the trigger phrase strongly suggests one type. Phrasings can be ambiguous and the wrong type wastes a whole job. This is non-negotiable.

The exact question I ask, in one short message:

> *"Â¿QuÃ© tipo de post hacemos? **(1)** step-by-step (tutorial paso a paso), **(2)** news (noticia de IA), o **(3)** informativo (hack/tip/lista)."*

Only after the user confirms the type, I proceed with the workflow:
1. **Read that type's `README.md`** for the workflow and the list of skills to load.
2. **Read the skill files** that the README points to.
3. **MANDATORY visual re-anchoring** (see section 1.5 below) â€” review inspiration AND past favorites before generating anything.
4. **Follow the workflow** for that type â€” never improvise the order, never skip steps.

---

## 1.5 Visual re-anchoring â€” MANDATORY before EVERY post (all types)

> **Before generating any HTML for any post, regardless of type, I must always review BOTH of the following folders for the post type at hand:**
>
> - **`PostTypes/{type}/Inspiracion/`** â€” external references the user has dropped in (creators they admire, layouts they want me to learn from). **Always check for new images here vs. what I've seen before.**
> - **`PostTypes/{type}/Favoritos_Claude_Generated/`** â€” slides I generated in past sessions that the user explicitly marked as favorites. These are the strongest signal of "this works for me."

### Why this is mandatory

The whole point of having both folders is to keep posts feeling **fresh but on-brand**. Without re-anchoring, my outputs converge on the same patterns over and over and the feed feels repetitive. The user has been explicit: posts should follow the same aesthetic but should NOT all look the same. Variety is **essential**, not optional.

### What "review" means in practice

For every new post:
1. **Inspiracion** â€” list the folder (catch any newly added references), then read at least 2 images. Prefer images I haven't viewed in recent jobs to maximize the spread of patterns I'm pulling from.
2. **Favoritos_Claude_Generated** â€” list the folder, then read every image inside (it's the user's curated "best of" list). If empty, that's fine â€” just note it.
3. **Synthesize** â€” explicitly hold both inputs in mind while drafting the breakdown. Vary at least one structural element vs. the most recent post in the same type (different cover layout, different visual element, different hook structure, etc.) so the new post doesn't visually rhyme with the previous one.

### When I'm allowed to skip

Never. Even for tiny iterations on an existing post (re-rendering one slide), I don't need to re-review â€” but for any **new** post I do.

---

## 1.6 After every post â€” capture user favorites

> **At the end of every post run, I must ask the user which generated images are their favorites and save them to `Favoritos_Claude_Generated/` for that post type.**

### Exact question to ask

After presenting the rendered carousel (step 9 of the step-by-step workflow, or the equivalent in other types), I always ask:

> *"Â¿CuÃ¡les imÃ¡genes de este post son tus favoritas? Las guardo en `Favoritos_Claude_Generated/` para usar como referencia en posts futuros."*

### What to do with the answer

- If the user names specific slides (e.g. "el cover v1 y el paso 3"), **copy** those PNGs from `PostTypes/{type}/Outputs/{topic-slug}/` to `PostTypes/{type}/Favoritos_Claude_Generated/`. Use a descriptive filename: `{topic-slug}_{original-name}.png` so it's clear what post it came from.
- If the user says "ninguna" or skips, that's fine â€” don't save anything, but still ask. Their answer is data either way.
- If the user says "todas", copy all the rendered PNGs of that post.
- **Use `cp` (copy), not `mv` (move)** â€” the original outputs stay in their folder; favorites are an additive curated library.

---

## 2. Project map

```
Visual_posts/
â”œâ”€â”€ CLAUDE.md                          â† this file (autoloaded â€” the router)
â”œâ”€â”€ README.md                          â† project intro
â”œâ”€â”€ Skills/                            â† global skills (apply to ALL post types)
â”‚   â”œâ”€â”€ visual-qa.md                   â† MANDATORY post-render QA â€” verify every PNG before presenting
â”‚   â””â”€â”€ slide-spacing.md               â† MANDATORY spacing/layout rules â€” content must fill ~70-85% of canvas, never leave large empty zones
â”œâ”€â”€ PostTypes/
â”‚   â”œâ”€â”€ step-by-step/                  â† tutorial / how-to carousels (mature)
â”‚   â”‚   â”œâ”€â”€ README.md                  â† workflow + triggers + folder rules for this type
â”‚   â”‚   â”œâ”€â”€ Skills/
â”‚   â”‚   â”‚   â”œâ”€â”€ instagram-post-design.md       â† BASE visual system (read FIRST)
â”‚   â”‚   â”‚   â”œâ”€â”€ instagram-cover-design.md      â† cover/thumbnail layouts
â”‚   â”‚   â”‚   â””â”€â”€ instagram-step-slide-design.md â† step slides + closing slide
â”‚   â”‚   â”œâ”€â”€ Inspiracion/               â† external visual references (drop new ones here)
â”‚   â”‚   â”œâ”€â”€ Favoritos_Claude_Generated/ â† past slides the user marked as favorites
â”‚   â”‚   â””â”€â”€ Outputs/                   â† rendered carousels (one folder per post)
â”‚   â”œâ”€â”€ news/                          â† AI news posts (ready)
â”‚   â”‚   â”œâ”€â”€ README.md
â”‚   â”‚   â”œâ”€â”€ Skills/
â”‚   â”‚   â”‚   â””â”€â”€ news-post-design.md    â† visual system for dark editorial news posts
â”‚   â”‚   â”œâ”€â”€ Inspiracion/               â† (empty â€” drop reference images here)
â”‚   â”‚   â”œâ”€â”€ Favoritos_Claude_Generated/ â† (empty â€” populated as user marks favorites)
â”‚   â”‚   â””â”€â”€ Outputs/
â”‚   â””â”€â”€ informativos/                  â† hacks / tips / infographics (ready)
â”‚       â”œâ”€â”€ README.md                  â† workflow + triggers + layout patterns
â”‚       â”œâ”€â”€ Skills/
â”‚       â”‚   â””â”€â”€ informativo-post-design.md â† visual system (7 layouts, scaffolds, palette)
â”‚       â”œâ”€â”€ Inspiracion/               â† 13 external visual references
â”‚       â”œâ”€â”€ Favoritos_Claude_Generated/ â† past slides the user marked as favorites
â”‚       â””â”€â”€ Outputs/                   â† rendered informativo posts
â”œâ”€â”€ Logos/                             â† shared brand assets across all post types
â”‚   â”œâ”€â”€ Claude_AI_symbol.svg
â”‚   â”œâ”€â”€ Alta_Studio_logo.png           â† Alta Studio logo (dark version)
â”‚   â””â”€â”€ Alta_Studio_Logo_fondoneutro.png â† Alta Studio logo (blue/glow version)
â”œâ”€â”€ Assets/                            â† shared user-provided screenshots / images
â”‚   â””â”€â”€ Personas/                      â† real person photos (CEOs, founders) â€” global
â”œâ”€â”€ Errors/                            â† user marks visual bugs here for me to fix
â”œâ”€â”€ render.sh                          â† HTMLâ†’PNG batch renderer (use this, not raw chrome)
â””â”€â”€ memory/                            â† persistent user/feedback memories (auto-loaded)
```

---

## 3. Brand-wide non-negotiable rules (apply to ALL post types)

These are project-wide invariants. They live across every post type, every slide, every iteration. Each post type's skills extend these rules with type-specific patterns â€” they never contradict them.

### 3.1 Brand handle
- The handle on top of every slide is **`@lucianomusellaa`** (double "a")
- Never `@ramiro.cubria` â€” that's only the visual reference creator

### 3.2 Spanish dialect
- **Colombian Spanish, `tÃº` form** â€” never Argentinian voseo
- âœ… Crea, Define, Instala, Convierte, Delega, Desliza, Guarda, Usa, tÃº, tienes, quieres
- âŒ CreÃ¡, DefinÃ­, InstalÃ¡, ConvertÃ­, DelegÃ¡, DeslizÃ¡, GuardÃ¡, UsÃ¡, vos, tenÃ©s, querÃ©s
- Reflexive imperatives keep the accent: `instÃ¡lalo`, `arrÃ¡ncalo`, `guÃ¡rdalo`
- Full conversion table is in [PostTypes/step-by-step/Skills/instagram-post-design.md](PostTypes/step-by-step/Skills/instagram-post-design.md) section 3.5

### 3.3 Visual system (cream + coral + yellow + grid)
- Background: cream `#F5F2ED` (NOT pure white) with subtle grid `#E8E4DD`
- Primary text: `#0E0E0E`
- Accent coral: `#E85D3C`
- Highlight yellow: `#FFE45C`
- Canvas: 1080Ã—1350 px (4:5 portrait)
- Font: Inter (500/600/700/800), JetBrains Mono for code

### 3.4 Render pipeline
- Use **`./render.sh {folder}`** to convert all HTMLs in a folder to PNGs. The folder path is relative to the project root, e.g. `./render.sh PostTypes/step-by-step/Outputs/agentes-claude-v2`.
- Single-file mode also works: `./render.sh PostTypes/step-by-step/Outputs/agentes-claude-v2/cover_v1_delega.html`
- Do NOT manually script Chrome headless commands â€” use `render.sh`
- The script handles all the flags (window size, virtual time budget, scale factor) and Git Bash â†’ Windows path conversion
- **Viewport bug fix (2026-04-16):** Chrome headless on Windows subtracts ~96px from `--window-size` height for window chrome decorations. `render.sh` uses `--window-size=1098,1550` (200px extra headroom) and then crops to exact 1080Ã—1350 via PIL. This ensures content near the bottom of the canvas (dots, pills, taglines at y>1272) renders correctly. If bottom elements appear cut off in renders, verify `render.sh` has the correct window size.
- **After every render, run the [Visual QA skill](Skills/visual-qa.md)** â€” open and inspect every PNG before presenting it to the user. This is mandatory for ALL post types. Never describe a feature you can't visually confirm in the rendered output.
- **Before writing any slide's HTML AND during QA, apply the [Slide Spacing skill](Skills/slide-spacing.md)** â€” content must fill ~70â€“85% of the usable canvas. Never leave >150px empty in the middle of a slide or >120px at the bottom outside the safe zone. Scale fonts up for short content; use flex `justify-content: space-between` for multi-element slides. This applies to ALL post types.

### 3.5 Image generation â€” hybrid approach (by post type)

This project uses **two image generation methods** depending on the post type:

| Post type | Method | Visual assets (logos, personas, backgrounds) |
|---|---|---|
| **Step-by-step** | HTML + CSS + inline SVG | Logos from `Logos/`; **Codex image tool ONLY for missing logos** â€” nothing else |
| **News** | **Codex image tool photos per slide** + HTML overlay | 5-slide carousel. Codex image tool generates ONE photo per slide that needs one (cover + body slides); HTML adds all text, tweet cards, stat cards, dots, Alta Studio. **No PIL anywhere.** |
| **Informativos** | **Codex image tool full composition** + HTML text overlay | Codex image tool generates the COMPLETE visual (background, layout structure, icons, logos, decorative elements â€” NO text); HTML overlay adds all text |

#### Step-by-step posts (Codex image tool ONLY for missing logos)
- All slides are **HTML + CSS + inline SVG**, rendered to PNG via `render.sh`.
- If a slide needs imagery beyond text, recreate it with elaborate inline SVG.
- Logos come from `Logos/` (real assets uploaded by the user).
- **If a needed logo is NOT in `Logos/`** â†’ generate it with Codex image tool with Codex's integrated image tool, save to `Logos/`, and present to the user for review before using it.
- **Codex image tool is strictly limited to logo generation in this post type.** Do NOT use it for backgrounds, illustrations, person photos, or any other asset â€” that would violate the no-local-paid-image rule. Everything else stays HTML + CSS + inline SVG.

#### News posts (5-slide carousel, Codex image tool photos + HTML overlay)
- **News is a carousel**, not a single image. 5 slides default (4â€“7 allowed). The old single-image + long-caption format is **deprecated**.
- **Slide structure:** (1) cover with photo + headline, (2) tweet/official announcement, (3) text+photo, (4) text+photo OR white-card stat, (5) closer (reaction tweet, stat card, or takeaway).
- **Codex image tool generates one photo per slide that needs one** â€” cover photo, body-slide supporting photos, optional tweet avatars. No text or logos inside the images.
- **HTML + render.sh handles everything else** â€” headlines with coral/yellow keyword highlights, tweet cards, white stat cards, page dots, Alta Studio logo, SWIPE pill. **PIL is no longer used for news.**
- **Tweet ethics (mandatory):** real official tweets are researched and reproduced faithfully; reaction/commentary tweets use invented handles with generated avatars; **never fabricate a quote attributed to a real person.** See `PostTypes/news/Skills/news-post-design.md` Â§11.
- **Photos are 100% generative** â€” no `--reference` with real person photos per user preference.
- **Alta Studio logo** appears in ONE top corner per slide (not both). **No `@lucianomusellaa`** on news. **No bottom-right watermark.**
- **Workflow for news carousels:**
  1. Visual re-anchor (`Inspiracion/` + `Favoritos_Claude_Generated/`)
  2. Draft the 5-slide outline â†’ user approves structure
  3. Propose 2â€“3 cover headline variations (Colombian Spanish, keyword highlights) â†’ user approves
  4. Research real tweets for slide 2 via WebSearch (if official announcement)
  5. Generate photos with Codex's integrated image tool, save the approved assets locally, and use the required ratios (4:5 cover, 16:9 body photos, 1:1 avatars).
  6. Present photos to user â€” only regenerate if rejected
  7. Build HTML for all slides â†’ `./render.sh PostTypes/news/Outputs/{topic-slug}`
  8. Visual QA on every PNG
  9. Short caption (1â€“3 lines) saved as `caption.txt`
  10. Present full carousel + caption, ask which slides are favorites
- See `PostTypes/news/Skills/news-post-design.md` for the complete visual system, HTML scaffolds, prompt guidelines, and tweet ethics.

#### Informativos posts (Codex image tool FULL COMPOSITION + HTML text overlay)
- **Codex image tool generates the complete visual composition** â€” background, layout structure (cards, tiers, grids, mind-map nodes), decorative elements, icons, brand logos â€” all as ONE cohesive image. This replaced the old HTML+CSS+SVG approach, which couldn't achieve the editorial richness of the inspiration images.
- **HTML is used ONLY for text** â€” titles, item names, descriptions, numbers, handle, footer. HTML uses the composition as `background-image` and positions text to align with the visual structure.
- **Workflow for informativos compositions:**
  1. Choose layout pattern (Aâ€“G) and craft a detailed composition prompt (see skill file section 4)
  2. Check `Logos/` and `Assets/` for existing brand assets (use `--reference` if available)
  3. Generate ONE composition with Codex's integrated image tool and save it as `composition.png`
  4. Present composition to user for review â€” only regenerate if rejected
  5. Generate HTML text overlay on top of the approved composition
  6. Render via `render.sh`
- See `PostTypes/informativos/Skills/informativo-post-design.md` section 4 for detailed prompting guidelines and layout templates.
- **Generation tool:** Codex's integrated image tool. Do not use local scripts, local credentials, or project-level paid image paths. Save generated assets locally at the intended ratio: 1080x1080 (1:1), 1080x1350 (4:5), or 1080x608 (16:9).`r`n- **âš ï¸ Content policy:** OpenAI's image policy rejects named real public figures (CEOs, politicians, researchers) more aggressively than Gemini did. If the script fails with `content_policy_violation`, rephrase the prompt as "a person who looks like X", describe the role/setting without the name, or use a user-provided reference photo in `Assets/Personas/`.

#### Prompt guidelines for Codex image tool
- **Logos:** be specific about the brand, style, and background. E.g. "Official OpenAI logo, clean vector style, white background, high resolution"
- **Person photos:** describe the person and context. E.g. "Professional headshot of Sam Altman, CEO of OpenAI, wearing a grey t-shirt, neutral background, editorial photography style"
- **Backgrounds/textures:** describe the mood and palette. E.g. "Abstract dark background with subtle blue circuit patterns, futuristic AI aesthetic, 1080x1350"
- **Illustrations:** describe the concept clearly. E.g. "Minimalist illustration of a brain connected to a neural network, clean lines, coral and cream color palette"

### 3.5.1 Brand logos and person photos â€” sourcing hierarchy

For **step-by-step** posts, logos MUST come from the `Logos/` folder first. If a logo is missing â†’ generate it with Codex image tool with Codex's integrated image tool, save to `Logos/`, and present for user review. **Codex image tool is ONLY allowed for logos in step-by-step â€” never for backgrounds, illustrations, or any other asset.**

For **news and informativos** posts, follow this order:
1. **Check `Logos/` and `Assets/Personas/` first** â€” if the real asset exists, always prefer it
2. **If not available â†’ generate with Codex image tool** with Codex's integrated image tool
3. **Save generated logos** to `Logos/` and **generated person photos** to `Assets/Personas/` so they're reusable across future posts
4. **Present to user for review** â€” they approve before it goes into the slide
5. **Never silently skip a visual asset** â€” either use an existing one or generate one. Every brand/person mentioned in the post should have its visual.

**SVG embedding tip (for existing assets):** for `.svg` files in `Logos/`, prefer inlining the `<svg>...</svg>` content directly into the HTML â€” this avoids path resolution issues with headless Chrome and gives full CSS control over fill/stroke colors.

### 3.6 Output folder structure
- **Every post lives in its own folder** under its type's `Outputs/`, e.g. `PostTypes/step-by-step/Outputs/{topic-slug}/`
- The slug is kebab-case, descriptive but short: `agentes-claude-code`, `claude-manychat-tutorial`, `flujos-meta-ads`
- Each folder contains the `.html` source files AND the rendered `.png` files side by side
- Never reuse a folder for a different topic. Never dump outputs into the root of `Outputs/`.
- Per-type naming conventions live in each type's `README.md`.

### 3.7 GitHub pushes require explicit approval
- I can `git init`, stage, commit locally, write READMEs, and configure remotes freely.
- I **must NOT** run `git push` (or any equivalent that publishes to a remote) until the user explicitly tells me to push in the current conversation ("haz el push", "sÃºbelo", "publÃ­calo", etc.).
- A prior approval to push does NOT carry over â€” every push needs its own green light.

---

## 4. When the user reports a visual bug

If the user mentions something is wrong with a slide (or puts marked-up images in `Errors/`):
1. Read the marked images from `Errors/` to see what they circled
2. Identify the root cause in the HTML (don't guess â€” find the actual SVG/CSS line)
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

## 6. The skills are the spec â€” don't improvise

Each post type's skill files are the operational ground truth for that type's design decisions. If a user request seems to conflict with a skill, **flag the conflict** before deviating. Example:

> *User: "haz el cover sin highlight"*
> *Me: "El skill dice que los covers usan double highlight por defecto (preferencia tuya validada). Â¿Quieres que lo saltemos solo en este post o cambiamos la regla en el skill?"*

The skills are alive â€” they should evolve with the user's preferences, but only deliberately.


