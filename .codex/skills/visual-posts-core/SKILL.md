---
name: visual-posts-core
description: Core operating rules for this Visual_posts repository. Use when Codex is creating, migrating, rendering, QAing, or editing Instagram post assets in this project, regardless of post type.
---

# Visual Posts Core

Use this skill for all work in `c:/Trabajo_AI/Visual_posts`. It defines the
shared rules; post-type skills add the specific workflow.

## Load Order

1. Read `AGENTS.md`.
2. Read this skill.
3. Read the selected post-type skill in `.codex/skills/`.
4. Read the detailed original specs linked by that skill.

## Global Rules

- Do not create, read, print, or use local credential files for image generation.
- Never use local OpenAI scripts or project-level paid paths for generated images.
- Use Colombian Spanish with `tu`; never use voseo.
- Use 1080 x 1350 px output for final posts.
- Keep generated source and rendered PNGs in
  `PostTypes/{type}/Outputs/{topic-slug}/`.
- Review `Inspiracion/` and `Favoritos_Claude_Generated/` before every new post.
- Ask which rendered images are favorites at the end and copy selected PNGs to
  the post type's `Favoritos_Claude_Generated/`.

## Tool Translation For Codex

- Use `view_image` to inspect local reference PNG/JPG/WebP files.
- Use the web tool for news verification and official tweets.
- Use `apply_patch` for manual file edits.
- Use `rg` and `rg --files` for search.
- Use `render.sh`; do not hand-write Chrome commands.

## Render

Render all HTML in a folder:

```bash
./render.sh PostTypes/{type}/Outputs/{topic-slug}
```

Render one file:

```bash
./render.sh PostTypes/{type}/Outputs/{topic-slug}/slide.html
```

If running from PowerShell, invoke through Git Bash if needed:

```powershell
bash render.sh PostTypes/{type}/Outputs/{topic-slug}
```

## Visual QA

After every render, inspect every PNG before presenting it.

Check:

- final image is 1080 x 1350,
- no white/black strips at edges,
- logos/photos loaded,
- bottom elements are visible,
- text is readable and not clipped,
- handle/logo rules match the post type,
- slide indicators are correct where required,
- Spanish is Colombian.

Read `Skills/visual-qa.md` and `Skills/slide-spacing.md` when implementing or
debugging layout. These original global skills remain the detailed references.

## Assets

- `Logos/` is the first place to check for brand assets.
- `Assets/Personas/` stores person photos.
- `Assets/Fonts/` contains Inter fonts for PIL scripts.
- Prefer relative paths from the generated HTML/script location.
- Avoid stale absolute paths such as `C:/Visual_posts`; the current workspace is
  `C:/Trabajo_AI/Visual_posts`.

## Image Generation

Use Codex's integrated image generation tool for every generated raster image.
This includes news photos, informativo compositions, missing logos, persona
photos, avatars, and any other visual asset.

Operational rule:

1. Generate the asset with Codex's integrated image tool.
2. Save or copy the selected output into the project.
3. Reference the saved local image from HTML, PIL overlays, or future posts.

Do not use local credentials, removed image scripts, or any workflow that
charges project-level image generation.

## Original References

Use these for detailed constraints:

- `CLAUDE.md`
- `Skills/visual-qa.md`
- `Skills/slide-spacing.md`
- `render.sh`
