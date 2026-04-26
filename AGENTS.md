# Visual_posts - Codex Operating Guide

This repository generates Instagram posts for `@lucianomusellaa`. It was originally
operated from Claude Code through `CLAUDE.md`; for Codex, this file is the root
entry point. `CLAUDE.md` remains as a compatibility reference, but new work should
follow this Codex-first guide and the local Codex skills in `.codex/skills/`.

## Required Startup

For every new post request:

1. Confirm the post type before doing production work:

   `Que tipo de post hacemos? (1) step-by-step, (2) news, o (3) informativo.`

2. Read the matching local Codex skill:

   - `.codex/skills/visual-posts-step-by-step/SKILL.md`
   - `.codex/skills/visual-posts-news/SKILL.md`
   - `.codex/skills/visual-posts-informativos/SKILL.md`

3. Read `.codex/skills/visual-posts-core/SKILL.md` for global visual QA,
   spacing, render, and asset rules.

4. Read the original detailed specs linked by the selected Codex skill before
   writing HTML, prompts, or overlay scripts.

5. Re-anchor visually before generating anything: inspect the selected post
   type's `Inspiracion/` and all current files in `Favoritos_Claude_Generated/`.

## Project Shape

- `CLAUDE.md`: original router and full operating contract.
- `Skills/`: global rules for visual QA and spacing.
- `PostTypes/{type}/Skills/`: per-type visual specs.
- `PostTypes/{type}/Inspiracion/`: external references to review before new work.
- `PostTypes/{type}/Favoritos_Claude_Generated/`: user-approved favorites to review before new work.
- `PostTypes/{type}/Outputs/{topic-slug}/`: generated HTML, PNGs, photos, and captions.
- `Logos/`: shared brand assets.
- `Assets/Personas/`: real/persona photos.
- Image generation: Codex integrated image tool only. Do not use local
  credentials, local OpenAI scripts, or project-level paid paths for image
  generation.
- `render.sh`: required HTML to PNG renderer.
- `.codex/skills/`: Codex-native skill wrappers for this project.

## Non-Negotiable Brand Rules

- Use Colombian Spanish with `tu`, never Argentinian voseo.
- Use `@lucianomusellaa` on step-by-step and informativo slides.
- Do not use `@lucianomusellaa` on news slides; news uses Alta Studio logo instead.
- Canvas is always 1080 x 1350 px unless generating intermediate assets with a documented ratio.
- Step-by-step visual identity: cream `#F5F2ED`, subtle grid `#E8E4DD`, black text, coral `#E85D3C`, yellow `#FFE45C`.
- News visual identity: dark editorial carousel, generated photos plus HTML overlays.
- Informativo visual identity: dense save-worthy infographic, usually generated composition plus text overlay.
- Do not create, read, print, or use local credential files for image generation.
- Before presenting output, visually inspect rendered PNGs. Do not describe a
  visual detail that has not been verified in the image.

## Codex Tool Translation

- Claude "Read image" means use `view_image` for local PNG/JPG/WebP references.
- Claude "WebSearch" means use the web tool. News facts, current announcements, and real tweets must be verified online.
- Claude "Bash" examples may need PowerShell or Git Bash adaptation in this Windows workspace.
- Prefer `rg` / `rg --files` for repo search.
- Use `apply_patch` for manual edits.
- Use `render.sh` for HTML renders; do not call Chrome manually unless explicitly debugging `render.sh`.

## Render And QA

Render with:

```bash
./render.sh PostTypes/{type}/Outputs/{topic-slug}
```

or single file:

```bash
./render.sh PostTypes/{type}/Outputs/{topic-slug}/slide.html
```

After every render, visually inspect every PNG before presenting it. Verify:

- exact 1080 x 1350 output,
- no clipped bottom elements,
- no broken images/logos,
- readable contrast,
- correct handle/logo rules,
- correct slide indicators where required,
- Colombian Spanish.

## Post-Type Routing

### Step-By-Step

Use `.codex/skills/visual-posts-step-by-step/SKILL.md`.

### News

Use `.codex/skills/visual-posts-news/SKILL.md`.

### Informativos

Use `.codex/skills/visual-posts-informativos/SKILL.md`.

## Known Migration Risks

- Some generated scripts still reference `C:/Visual_posts`; current workspace is
  `C:/Trabajo_AI/Visual_posts`. Prefer relative paths or derive paths from the file location.
- Some historical news outputs are from an older/deprecated news format and may violate the new
  news spec. Use them as archive/reference only, not as current rules.
- README/spec text may render with mojibake in PowerShell output. Do not "fix" accents blindly;
  preserve UTF-8 content when editing.
- `render.sh` assumes Git Bash style paths and Chrome at
  `/c/Program Files/Google/Chrome/Application/chrome.exe`.
- Legacy references to removed local image scripts or paid project-level image
  generation are deprecated. Replace them operationally with Codex integrated
  image generation, then save the generated asset into the project.

## Delivery Convention

At the end of a post run, ask:

`Cuales imagenes de este post son tus favoritas? Las guardo en Favoritos_Claude_Generated para usarlas como referencia en posts futuros.`

Copy selected PNGs into the correct `Favoritos_Claude_Generated/` folder. Use copy, never move.
