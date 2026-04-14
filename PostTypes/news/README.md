# News posts — AI noticias

## What this type is for

Posts about AI announcements, model releases, breaking news, industry events. **Single image** (not a carousel) — the hook is **timeliness and a bold headline** over a real person photo, with a dark editorial feel.

## Trigger phrases

- "post de noticia: {titular}"
- "carrusel de la noticia de {evento}"
- "hagamos un post sobre la noticia de {tema}"
- "esto salió hoy: {url}"

## Skills to load (in order)

1. **[Skills/news-post-design.md](Skills/news-post-design.md)** — the complete visual system for news posts (layout, colors, typography, photo handling, headline rules, HTML scaffold)

## Workflow when the user triggers a news post

1. **Read the skill:** load `Skills/news-post-design.md`
2. **Mandatory visual re-anchoring:** review [`Inspiracion/`](Inspiracion/) AND [`Favoritos_Claude_Generated/`](Favoritos_Claude_Generated/) (see root CLAUDE.md section 1.5)
3. **Get the news details:** what happened, who's involved, source
4. **Check `Assets/Personas/`** for existing reference photos (useful for `--reference` in Nano Banana)
5. **Propose 2–3 headline variations** in Colombian Spanish. Wait for approval.
6. **Research the full story** (if user only gave a title, search the internet for the complete article).
7. **Draft the caption** — short paragraphs, factual, Colombian Spanish. Generate directly (no approval needed).
8. **Generate ONE visual composition with Nano Banana 2** — full image with person + brand logo + dark atmosphere. Use `--model gemini-3-pro-image-preview --aspect-ratio 4:5`. Present to user — only regenerate if rejected.
9. **Composite text with Python/PIL** (NOT HTML/Chrome — Chrome creates border artifacts). Draw: badge, headline, source, Alta Studio logo. No bottom-right watermark.
10. **Verify** the final PNG visually — image must fill 1080×1350 edge-to-edge with zero borders.
11. **Save the caption** as `caption.txt` in the output folder.
12. **Present the complete deliverable:** image + caption together. Offer iterations.
13. **Ask which images are favorites** → copy to `Favoritos_Claude_Generated/`

## Brand-wide rules that apply

From the root [CLAUDE.md](../../CLAUDE.md):

- **Always ask the user to confirm the post type** before starting (section 1)
- **Mandatory visual re-anchoring** before generating anything (section 1.5)
- **After every post, ask which images are favorites** (section 1.6)
- **Colombian Spanish, tú form** — never Argentinian voseo
- **NO `@lucianomusellaa` on news** — use Alta Studio logo in top-right instead (editorial feel)
- **Alta Studio watermark** on every image (subtle, bottom-right)
- **Brand logos** from `Logos/` (existing) or generated with **Nano Banana 2** if missing
- **Person photos** from `Assets/Personas/` (existing) or generated with **Nano Banana 2** if missing — always user-reviewed

## Folder layout

```
PostTypes/news/
├── README.md                     ← this file
├── Skills/
│   └── news-post-design.md      ← visual system + HTML scaffold
├── Inspiracion/                  ← external visual references
├── Favoritos_Claude_Generated/   ← past images the user marked as favorites
└── Outputs/                      ← rendered news posts (one folder per news item)
    └── {topic-slug}/
        ├── news_v1_{descriptor}.html
        ├── news_v1_{descriptor}.png
        ├── caption.txt              ← caption listo para copiar a Instagram
        └── ...
```
