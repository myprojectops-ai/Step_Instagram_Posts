---
name: visual-posts-news
description: Create or edit dark editorial AI news Instagram carousels in Visual_posts. Use for news posts, current AI announcements, model releases, industry events, official tweets, source slides, and short news captions.
---

# News Posts

Use this skill for AI news carousels. Current format is a 5-slide dark editorial
carousel, not the older single-image news format.

## Required References

Read these before production work:

1. `.codex/skills/visual-posts-core/SKILL.md`
2. `PostTypes/news/README.md`
3. `PostTypes/news/Skills/news-post-design.md`

## Workflow

1. Confirm post type.
2. Review `PostTypes/news/Inspiracion/` and every file in
   `PostTypes/news/Favoritos_Claude_Generated/`.
3. Understand and verify the news. Browse when the user gives only a headline,
   a current event, a URL, or anything likely to have changed.
4. Draft the 5-slide outline and wait for approval.
5. Propose 2-3 cover headline variants and wait for approval.
6. Research official tweets when slide 2 uses a real announcement.
7. Generate one photo per needed slide with Codex's integrated image tool and
   save each approved asset into the post output folder.
8. Present generated photos before using them, unless the user explicitly asked
   for a fully autonomous run.
9. Build HTML overlays.
10. Render with `render.sh`.
11. Inspect every PNG.
12. Save a 1-3 line caption as `caption.txt`.
13. Present the carousel and ask for favorites.

## Slide Structure

Default:

- Slide 1: full-bleed cover photo, gradient, headline, Alta Studio logo, SWIPE pill.
- Slide 2: real official tweet or verified quote card.
- Slide 3: text + generated 16:9 photo.
- Slide 4: text + photo or white stat/quote card.
- Slide 5: reaction tweet with invented handle, stat card, or key takeaway.

Use 4-7 slides only when the story needs it.

## Visual Rules

- Dark editorial visual system.
- No `@lucianomusellaa` on news.
- Alta Studio logo appears in one top corner on every slide.
- No page dots on news slides.
- SWIPE pill appears only on the cover.
- HTML owns all typography, logos, tweet cards, stats, and labels.
- Generated images must contain no text, logos, words, or watermarks.

## Image Ratios

- Cover photo: 4:5 / 1080 x 1350 target.
- Body photo: 16:9 / 1080 x 608 target.
- Avatar: 1:1 square target.

## Tweet Ethics

- Never fabricate a quote attributed to a real person or company.
- Official announcements require web verification and faithful reproduction.
- Invented reaction tweets must use invented handles/personas.
- If a real tweet cannot be verified, use an editorial quote/source card instead.

## Historical Outputs

Some older `PostTypes/news/Outputs/` folders use deprecated single-image or
watermark patterns. Treat them as archive, not current spec.
