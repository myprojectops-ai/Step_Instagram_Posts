---
name: visual-posts-step-by-step
description: Create or edit step-by-step Instagram tutorial carousels in Visual_posts. Use for tutorial, how-to, paso a paso, carousel walkthrough, cover, step slide, closing CTA, or dark-mode variants.
---

# Step-By-Step Posts

Use this skill for tutorial/how-to carousels: cover -> PASO slides -> closing CTA.

## Required References

Read these before creating or editing slides:

1. `.codex/skills/visual-posts-core/SKILL.md`
2. `PostTypes/step-by-step/README.md`
3. `PostTypes/step-by-step/Skills/instagram-post-design.md`
4. `PostTypes/step-by-step/Skills/instagram-cover-design.md`
5. `PostTypes/step-by-step/Skills/instagram-step-slide-design.md`
6. `PostTypes/step-by-step/Skills/instagram-dark-mode.md` only if the user asks for dark mode.

## Workflow

1. Confirm post type.
2. Review at least 2 images in `PostTypes/step-by-step/Inspiracion/`.
3. Review all PNGs in `PostTypes/step-by-step/Favoritos_Claude_Generated/`.
4. List `Logos/` and check whether required brands already exist.
5. Gather missing context only if necessary.
6. Propose the full carousel breakdown in text and wait for approval.
7. Create `PostTypes/step-by-step/Outputs/{topic-slug}/`.
8. Write HTML files.
9. Render with `render.sh`.
10. Inspect every PNG.
11. Present the carousel and offer precise iterations.
12. Ask which images are favorites and copy selected PNGs.

Do not write production HTML before the user approves the breakdown.

## Visual Rules

- Use cream background `#F5F2ED` with subtle grid `#E8E4DD`.
- Put `@lucianomusellaa` at top on every slide.
- Use Inter; JetBrains Mono for code/terminal mockups.
- Covers default to double highlight: one coral keyword and one yellow marker.
- Step slides use exactly one highlighted keyword.
- Every step slide has `PASO {N}`.
- Every carousel slide has indicator dots; active dot matches the slide index.
- Closing slide has no `Desliza ->`, but it still has indicator dots.
- Use HTML/CSS/inline SVG for visuals.
- Use Codex's integrated image tool only for missing logos after checking
  `Logos/`; never use local credentials or project-level paid paths.

## Naming

- Cover variations: `cover_v{n}_{descriptor}.html`
- Step slides: `paso_{n}_{descriptor}.html`
- Closing slide: `cierre_cta.html`
- Rendered PNGs sit beside their HTML.

## Dark Mode

Use only when explicitly requested. Create a sibling folder ending in `-dark`.
Change colors only; preserve layout, copy, and structure.
