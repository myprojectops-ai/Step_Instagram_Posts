# News posts â€” AI noticias

## What this type is for

Posts about AI announcements, model releases, breaking news, industry events. **5-slide carousel** (4â€“7 allowed) with a dark editorial feel â€” Codex image tool photos + HTML text overlay. The hook is **timeliness + a bold headline + a real source tweet + digestible body slides** that replace the old long caption.

## Trigger phrases

- "post de noticia: {titular}"
- "carrusel de la noticia de {evento}"
- "hagamos un post sobre la noticia de {tema}"
- "esto saliÃ³ hoy: {url}"

## Skills to load (in order)

1. **[Skills/news-post-design.md](Skills/news-post-design.md)** â€” the complete visual system for news carousels (5-slide taxonomy, cover layout, tweet/text/card templates, Codex image tool prompting, tweet ethics, Colombian Spanish rules, HTML scaffolds)

## The 5-slide default structure

| # | Slide type | Purpose |
|---|---|---|
| 1 | **Cover** | Codex image tool photo + bold headline with coral/yellow keyword highlights + SWIPE pill |
| 2 | **Tweet** | Real official tweet from the company/CEO (researched) OR quote card |
| 3 | **Text + photo** | What happened â€” short text block + Codex image tool supporting photo |
| 4 | **Text + photo** OR **white card** | Why it matters â€” explanation with photo, OR punchline stat on white card |
| 5 | **Closer** | Reaction tweet (invented commentator handle) OR stat card OR key takeaway |

Flexibility: 4 slides for simple news (skip slide 4), 6â€“7 for complex news. Never fewer than 4.

## Workflow when the user triggers a news post

1. **Read the skill:** load [`Skills/news-post-design.md`](Skills/news-post-design.md)
2. **Mandatory visual re-anchoring:** review [`Inspiracion/`](Inspiracion/) AND [`Favoritos_Claude_Generated/`](Favoritos_Claude_Generated/) (see root [CLAUDE.md](../../CLAUDE.md) Â§1.5). **Look at carousel patterns, not just covers.**
3. **Understand the news:** what happened, who's involved, what's the data.
4. **If only a title was given â†’ WebSearch** for the full story. Extract: who, what, when, how, numbers, impact, source.
5. **Draft the 5-slide outline:** propose the breakdown (cover hook, tweet angle, body slide 1 angle, body slide 2 angle, closer angle). Wait for user approval of the structure.
6. **Propose 2â€“3 cover headline variations** in Colombian Spanish with keyword highlights marked. Wait for approval.
7. **Research real tweets** if slide 2 is an official announcement â€” use WebSearch, reproduce the real tweet text faithfully (see skill Â§11).
8. **Generate photos with Codex image tool** â€” ONE per slide that needs one (cover + 1â€“2 body slides + optional closer/avatar). Cover at `--aspect-ratio 4:5`, body slides at `16:9`. The script crops + resizes internally to exact dimensions â€” no separate resize step needed.
9. **Present photos to user for review.** Only regenerate if rejected.
10. **Build the HTML for all slides** â€” cover, tweet, text+photo, (optional) white card, closer. Save each as `slide{N}_{descriptor}.html` in the post's output folder.
11. **Render via `./render.sh PostTypes/news/Outputs/{topic-slug}`** â€” renders all slides at once.
12. **MANDATORY Visual QA** â€” open every PNG (see [`Skills/visual-qa.md`](../../Skills/visual-qa.md)). Verify: no artifacts, text readable, photos positioned correctly, dots correct per slide, Alta Studio visible, SWIPE pill only on cover.
13. **Draft the short caption** (1â€“3 lines only) â†’ save as `caption.txt` in the output folder.
14. **Present the complete carousel** â€” all slide PNGs in order + caption.
15. **Ask which slides are favorites** â†’ copy to [`Favoritos_Claude_Generated/`](Favoritos_Claude_Generated/).

## Brand-wide rules that apply

From the root [CLAUDE.md](../../CLAUDE.md):

- **Always ask the user to confirm the post type** before starting (Â§1)
- **Mandatory visual re-anchoring** before generating anything (Â§1.5)
- **After every post, ask which images are favorites** (Â§1.6)
- **Colombian Spanish, tÃº form** â€” never Argentinian voseo
- **NO `@lucianomusellaa` on news** â€” Alta Studio logo in ONE top corner replaces it
- **No bottom-right watermark** â€” just the single Alta Studio logo
- **Photos are 100% generative** (no `--reference`, no real person compositing)
- **Fabricated quotes attributed to real people are forbidden** â€” see skill Â§11 for tweet ethics

## What changed vs. the old system

The old news system was a **single image with a long caption**. That approach is deprecated. The new carousel format was adopted after reviewing inspiration from accounts like Bridgemind â€” they break the story into digestible slides that people actually read, which outperforms a long caption that gets skipped.

| | Old | New |
|---|---|---|
| Format | Single image + 6â€“10 paragraph caption | 5-slide carousel + 1â€“3 line caption |
| Text compositing | PIL (Python) | HTML + render.sh |
| Photos | Generated (often with `--reference`) | Codex image tool only, no reference |
| Alta Studio | Fixed top-right every time | One corner per slide (composition-dependent) |

## Folder layout

```
PostTypes/news/
â”œâ”€â”€ README.md                     â† this file
â”œâ”€â”€ Skills/
â”‚   â””â”€â”€ news-post-design.md       â† visual system + HTML scaffolds + tweet ethics
â”œâ”€â”€ Inspiracion/                  â† external visual references (carousel patterns)
â”œâ”€â”€ Favoritos_Claude_Generated/   â† past slides the user marked as favorites
â””â”€â”€ Outputs/                      â† rendered news carousels (one folder per news item)
    â””â”€â”€ {topic-slug}/
        â”œâ”€â”€ composition.png              â† cover photo (Codex image tool)
        â”œâ”€â”€ slide3_photo.png             â† body slide photo
        â”œâ”€â”€ slide4_photo.png             â† (optional)
        â”œâ”€â”€ slide5_photo.png             â† (optional, if closer is Template A)
        â”œâ”€â”€ tweet_avatar.png             â† (optional, invented commentator avatar)
        â”œâ”€â”€ slide1_cover.html
        â”œâ”€â”€ slide1_cover.png
        â”œâ”€â”€ slide2_tweet.html
        â”œâ”€â”€ slide2_tweet.png
        â”œâ”€â”€ slide3_text.html
        â”œâ”€â”€ slide3_text.png
        â”œâ”€â”€ slide4_{text|card}.html
        â”œâ”€â”€ slide4_{text|card}.png
        â”œâ”€â”€ slide5_closer.html
        â”œâ”€â”€ slide5_closer.png
        â””â”€â”€ caption.txt                  â† 1â€“3 lines for Instagram
```

## Naming convention for `{topic-slug}`

- kebab-case, descriptive, short: `anthropic-lideres-religiosos`, `altman-ataques-casa`, `perplexity-billion-build`, `claude-opus-4-7`
- Never reuse a folder for a different news item

