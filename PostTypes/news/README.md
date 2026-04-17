# News posts — AI noticias

## What this type is for

Posts about AI announcements, model releases, breaking news, industry events. **5-slide carousel** (4–7 allowed) with a dark editorial feel — Nano Banana photos + HTML text overlay. The hook is **timeliness + a bold headline + a real source tweet + digestible body slides** that replace the old long caption.

## Trigger phrases

- "post de noticia: {titular}"
- "carrusel de la noticia de {evento}"
- "hagamos un post sobre la noticia de {tema}"
- "esto salió hoy: {url}"

## Skills to load (in order)

1. **[Skills/news-post-design.md](Skills/news-post-design.md)** — the complete visual system for news carousels (5-slide taxonomy, cover layout, tweet/text/card templates, Nano Banana prompting, tweet ethics, Colombian Spanish rules, HTML scaffolds)

## The 5-slide default structure

| # | Slide type | Purpose |
|---|---|---|
| 1 | **Cover** | Nano Banana photo + bold headline with coral/yellow keyword highlights + SWIPE pill |
| 2 | **Tweet** | Real official tweet from the company/CEO (researched) OR quote card |
| 3 | **Text + photo** | What happened — short text block + Nano Banana supporting photo |
| 4 | **Text + photo** OR **white card** | Why it matters — explanation with photo, OR punchline stat on white card |
| 5 | **Closer** | Reaction tweet (invented commentator handle) OR stat card OR key takeaway |

Flexibility: 4 slides for simple news (skip slide 4), 6–7 for complex news. Never fewer than 4.

## Workflow when the user triggers a news post

1. **Read the skill:** load [`Skills/news-post-design.md`](Skills/news-post-design.md)
2. **Mandatory visual re-anchoring:** review [`Inspiracion/`](Inspiracion/) AND [`Favoritos_Claude_Generated/`](Favoritos_Claude_Generated/) (see root [CLAUDE.md](../../CLAUDE.md) §1.5). **Look at carousel patterns, not just covers.**
3. **Understand the news:** what happened, who's involved, what's the data.
4. **If only a title was given → WebSearch** for the full story. Extract: who, what, when, how, numbers, impact, source.
5. **Draft the 5-slide outline:** propose the breakdown (cover hook, tweet angle, body slide 1 angle, body slide 2 angle, closer angle). Wait for user approval of the structure.
6. **Propose 2–3 cover headline variations** in Colombian Spanish with keyword highlights marked. Wait for approval.
7. **Research real tweets** if slide 2 is an official announcement — use WebSearch, reproduce the real tweet text faithfully (see skill §11).
8. **Generate photos with Nano Banana** — ONE per slide that needs one (cover + 1–2 body slides + optional closer/avatar). Use `gemini-3-pro-image-preview` + `--aspect-ratio 4:5`. Resize to 1080×1350 after.
9. **Present photos to user for review.** Only regenerate if rejected.
10. **Build the HTML for all slides** — cover, tweet, text+photo, (optional) white card, closer. Save each as `slide{N}_{descriptor}.html` in the post's output folder.
11. **Render via `./render.sh PostTypes/news/Outputs/{topic-slug}`** — renders all slides at once.
12. **MANDATORY Visual QA** — open every PNG (see [`Skills/visual-qa.md`](../../Skills/visual-qa.md)). Verify: no artifacts, text readable, photos positioned correctly, dots correct per slide, Alta Studio visible, SWIPE pill only on cover.
13. **Draft the short caption** (1–3 lines only) → save as `caption.txt` in the output folder.
14. **Present the complete carousel** — all slide PNGs in order + caption.
15. **Ask which slides are favorites** → copy to [`Favoritos_Claude_Generated/`](Favoritos_Claude_Generated/).

## Brand-wide rules that apply

From the root [CLAUDE.md](../../CLAUDE.md):

- **Always ask the user to confirm the post type** before starting (§1)
- **Mandatory visual re-anchoring** before generating anything (§1.5)
- **After every post, ask which images are favorites** (§1.6)
- **Colombian Spanish, tú form** — never Argentinian voseo
- **NO `@lucianomusellaa` on news** — Alta Studio logo in ONE top corner replaces it
- **No bottom-right watermark** — just the single Alta Studio logo
- **Photos are 100% Nano Banana generative** (no `--reference`, no real person compositing)
- **Fabricated quotes attributed to real people are forbidden** — see skill §11 for tweet ethics

## What changed vs. the old system

The old news system was a **single image with a long caption**. That approach is deprecated. The new carousel format was adopted after reviewing inspiration from accounts like Bridgemind — they break the story into digestible slides that people actually read, which outperforms a long caption that gets skipped.

| | Old | New |
|---|---|---|
| Format | Single image + 6–10 paragraph caption | 5-slide carousel + 1–3 line caption |
| Text compositing | PIL (Python) | HTML + render.sh |
| Photos | Nano Banana (often with `--reference`) | Nano Banana only, no reference |
| Alta Studio | Fixed top-right every time | One corner per slide (composition-dependent) |

## Folder layout

```
PostTypes/news/
├── README.md                     ← this file
├── Skills/
│   └── news-post-design.md       ← visual system + HTML scaffolds + tweet ethics
├── Inspiracion/                  ← external visual references (carousel patterns)
├── Favoritos_Claude_Generated/   ← past slides the user marked as favorites
└── Outputs/                      ← rendered news carousels (one folder per news item)
    └── {topic-slug}/
        ├── composition.png              ← cover photo (Nano Banana)
        ├── slide3_photo.png             ← body slide photo
        ├── slide4_photo.png             ← (optional)
        ├── slide5_photo.png             ← (optional, if closer is Template A)
        ├── tweet_avatar.png             ← (optional, invented commentator avatar)
        ├── slide1_cover.html
        ├── slide1_cover.png
        ├── slide2_tweet.html
        ├── slide2_tweet.png
        ├── slide3_text.html
        ├── slide3_text.png
        ├── slide4_{text|card}.html
        ├── slide4_{text|card}.png
        ├── slide5_closer.html
        ├── slide5_closer.png
        └── caption.txt                  ← 1–3 lines for Instagram
```

## Naming convention for `{topic-slug}`

- kebab-case, descriptive, short: `anthropic-lideres-religiosos`, `altman-ataques-casa`, `perplexity-billion-build`, `claude-opus-4-7`
- Never reuse a folder for a different news item
