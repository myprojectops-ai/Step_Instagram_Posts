---
name: visual-posts-informativos
description: Create or edit dense informative Instagram posts in Visual_posts. Use for AI tips, hacks, lists, cheatsheets, rankings, mind maps, tool lists, prompt lists, infographics, or save-worthy reference posts.
---

# Informativos Posts

Use this skill for dense, save-worthy AI infographics and short informative
carousels.

## Required References

Read these before production work:

1. `.codex/skills/visual-posts-core/SKILL.md`
2. `PostTypes/informativos/README.md`
3. `PostTypes/informativos/Skills/informativo-post-design.md`
4. `Skills/informativo-visual-iteration.md` for PIL/connected-component alignment.

## Migration Decision

The repository contains older wording that says informativo text overlays are
HTML + `render.sh`. The current detailed informativo skill and the working
example in `PostTypes/informativos/Outputs/ahorro-4h-claude-code/render_text.py`
prefer PIL text compositing after a Codex-generated composition because browser
background-image rendering can create artifacts.

Use this rule until the user changes it:

- Single-image informativos: Codex-generated composition + PIL text overlay.
- Multi-slide informativos: use the hybrid workflow from the detailed skill:
  generated/PIL cover when needed, HTML/CSS content slides when precision matters.

## Workflow

1. Confirm post type.
2. Review `PostTypes/informativos/Inspiracion/` and every file in
   `PostTypes/informativos/Favoritos_Claude_Generated/`.
3. Choose one layout pattern A-G.
4. Check `Logos/` and `Assets/` for required assets.
5. Propose title, layout, items/sections, and caption. Wait for approval before
   generating the composition image.
6. Generate one composition only with Codex's integrated image tool and save it
   as `composition.png` in the post output folder.
7. Present the composition for approval.
8. Overlay text with PIL or the approved hybrid approach.
9. Inspect every final PNG.
10. Save caption as `caption.txt`.
11. Present output and ask for favorites.

## Layout Patterns

- A: numbered list.
- B: grid cards.
- C: tier list or pyramid.
- D: mind map or radial diagram.
- E: sectioned cheatsheet.
- F: single feature or hero card.
- G: comparison or before/after.

## Composition Rules

- Composition must be cream-based and editorial.
- Composition must contain empty zones for text.
- Composition must contain no text, letters, numbers, typography, or watermarks.
- Generate one composition only unless the user rejects it.
- Category colors are allowed, but max five per post.

## Text Overlay Rules

- Use Inter fonts from `Assets/Fonts/`.
- Prefer relative paths or derive paths from the script location.
- Do not use stale `C:/Visual_posts` paths.
- For organic blobs/cards, find exact text zones with connected-component
  analysis rather than guessing coordinates.
- Verify all text is readable at reduced size and stays inside its visual zone.

## Content Rules

- Make the post specific and useful; avoid generic filler.
- Use a number in the title when natural.
- Minimum body text size is 16 px.
- No Alta Studio watermark on informativos.
- Use `@lucianomusellaa` unless the detailed workflow says a specific cover
  layout needs different placement.
