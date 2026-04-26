# Visual_posts

Sistema para generar posts y carruseles de Instagram sobre inteligencia
artificial, automatizacion y herramientas de trabajo para `@lucianomusellaa`.

El proyecto empezo como un flujo para Claude Code. Ahora esta migrado para ser
operado por Codex: `AGENTS.md` es el router principal y `.codex/skills/`
contiene los skills Codex-first. `CLAUDE.md` se conserva como referencia
historica y compatibilidad.

## Tipos De Posts

| Tipo | Estado | Uso |
|---|---|---|
| `step-by-step` | Maduro | Tutoriales, how-tos y carruseles paso a paso. |
| `news` | Activo | Carruseles editoriales de noticias de IA, lanzamientos y anuncios. |
| `informativos` | Activo | Infografias, hacks, listas, cheatsheets y posts guardables. |

## Como Trabajar Con Codex

1. Pide un post en lenguaje natural.
2. Codex debe confirmar el tipo de post: step-by-step, news o informativo.
3. Codex lee `AGENTS.md`.
4. Codex carga el skill local correspondiente en `.codex/skills/`.
5. Codex revisa inspiracion y favoritos del tipo elegido.
6. Codex propone el desglose y espera aprobacion cuando el workflow lo exige.
7. Codex genera HTML, imagenes o overlays segun el tipo.
8. Codex renderiza y verifica visualmente cada PNG antes de presentarlo.

## Estructura

```text
Visual_posts/
|-- AGENTS.md
|-- CLAUDE.md
|-- README.md
|-- .codex/
|   `-- skills/
|       |-- visual-posts-core/
|       |-- visual-posts-step-by-step/
|       |-- visual-posts-news/
|       `-- visual-posts-informativos/
|-- Skills/
|   |-- visual-qa.md
|   |-- slide-spacing.md
|   `-- informativo-visual-iteration.md
|-- PostTypes/
|   |-- step-by-step/
|   |-- news/
|   `-- informativos/
|-- Assets/
|-- Logos/
|-- Errors/
`-- render.sh
```

## Reglas Globales

- Idioma: espanol colombiano con `tu`; nunca voseo argentino.
- Canvas final: 1080 x 1350 px.
- Tipografia: Inter; JetBrains Mono para codigo.
- Step-by-step e informativos usan `@lucianomusellaa`.
- News no usa `@lucianomusellaa`; usa logo de Alta Studio.
- No usar credenciales locales para generar imagenes.
- Todas las imagenes generativas las produce Codex con su herramienta integrada,
  sin depender de cobros del proyecto.
- Toda imagen renderizada debe pasar QA visual antes de presentarse.

## Render Manual

Renderizar una carpeta:

```bash
./render.sh PostTypes/step-by-step/Outputs/{topic-slug}
```

Renderizar un archivo:

```bash
./render.sh PostTypes/news/Outputs/{topic-slug}/slide1_cover.html
```

En PowerShell puede ser necesario:

```powershell
bash render.sh PostTypes/step-by-step/Outputs/{topic-slug}
```

## Imagenes Generativas

Las imagenes generativas se crean siempre con la herramienta integrada de Codex,
no con scripts locales ni credenciales del proyecto.

Flujo:

1. Codex genera la imagen en la herramienta integrada.
2. Codex la guarda dentro del proyecto en la carpeta correspondiente:
   `PostTypes/{type}/Outputs/{topic-slug}/`, `Logos/` o `Assets/`.
3. El post usa esa imagen local para el render final.

No debe existir ningun archivo local de credenciales para imagenes en este proyecto.

## Notas De Migracion

- La fuente de operacion para Codex es `AGENTS.md` + `.codex/skills/`.
- Los skills originales en `PostTypes/*/Skills/` siguen siendo la spec visual
  detallada.
- Algunos outputs antiguos de `news` pertenecen a un formato deprecated; no se
  deben usar como regla actual.
- Algunos scripts generados antiguos usan `C:/Visual_posts`; el workspace actual
  es `C:/Trabajo_AI/Visual_posts`. Usar rutas relativas cuando sea posible.
- Referencias antiguas a modelos o scripts locales de imagen deben interpretarse como
  "usar la herramienta integrada de imagen de Codex".
