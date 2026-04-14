# Visual_posts

Sistema de generación de **posts de Instagram** con un lenguaje visual consistente, pensado para la cuenta **@lucianomusellaa**. Soporta tres tipos diferentes de posts, cada uno con sus propios skills, referencias visuales y workflow.

El proyecto está diseñado para operarse desde [Claude Code](https://claude.com/claude-code): tú escribes una intención en lenguaje natural ("hagamos un post sobre X") y el agente sigue un workflow definido para producir el post renderizado en PNG, listo para subir.

---

## Tres tipos de posts

| Tipo | Estado | Para qué sirve |
|---|---|---|
| **Step-by-step** ([`PostTypes/step-by-step/`](PostTypes/step-by-step/)) | ✅ Maduro — listo para usar | Tutoriales, how-tos, "X pasos para Y". Carruseles con cover → pasos → cierre. |
| **News** ([`PostTypes/news/`](PostTypes/news/)) | 🚧 Por construir | Posts de noticias de IA, lanzamientos, actualizaciones. Falta definir skills + referencias. |
| **Informativos** ([`PostTypes/informativos/`](PostTypes/informativos/)) | 🚧 Por construir | Hacks, tips, listas, "did you know". Falta definir skills + referencias. |

Cada tipo tiene su propio `README.md` con el workflow específico, sus skills (la "spec" de diseño visual), una carpeta de `Inspiracion/` con referencias, y `Outputs/` donde se guardan los posts renderizados.

---

## Estructura del proyecto

```
Visual_posts/
├── CLAUDE.md                          ← instrucciones del agente (autoload, router por tipo)
├── README.md                          ← este archivo
├── PostTypes/
│   ├── step-by-step/                  ← tutoriales / how-tos (maduro)
│   │   ├── README.md                  ← workflow + triggers + reglas para este tipo
│   │   ├── Skills/                    ← spec de diseño visual
│   │   ├── Inspiracion/               ← referencias visuales externas (drop nuevas aquí)
│   │   ├── Favoritos_Claude_Generated/ ← imágenes favoritas del usuario de runs pasados
│   │   └── Outputs/                   ← posts renderizados
│   ├── news/                          ← posts de noticias de IA (por construir)
│   └── informativos/                  ← hacks / tips / listas (por construir)
├── Logos/                             ← assets de marca compartidos
├── Assets/                            ← screenshots e imágenes del usuario
├── Errors/                            ← marcado de bugs visuales para iteraciones
├── render.sh                          ← batch renderer HTML → PNG (Chrome headless)
└── memory/                            ← memorias persistentes del usuario
```

---

## Reglas no negociables del sistema visual (todos los tipos)

- **Handle**: siempre `@lucianomusellaa` en la parte superior de cada slide.
- **Idioma**: español **colombiano** con `tú` (nunca voseo argentino: ✅ `crea`, `define`, `instala` / ❌ `creá`, `definí`, `instalá`).
- **Paleta**:
  - Fondo crema `#F5F2ED` con grid sutil `#E8E4DD`
  - Texto principal `#0E0E0E`
  - Acento coral `#E85D3C`
  - Highlight amarillo `#FFE45C`
- **Tipografía**: Inter (500/600/700/800) + JetBrains Mono para código.
- **Canvas**: 1080 × 1350 px (4:5 portrait).
- **Generación de imágenes**: 100% HTML + CSS + SVG inline, renderizado a PNG con Chrome headless. **Sin APIs externas de generación de imágenes** — todo se construye con código.

Detalle completo en [CLAUDE.md](CLAUDE.md) y en los skills de cada tipo (por ejemplo [PostTypes/step-by-step/Skills/](PostTypes/step-by-step/Skills/)).

---

## Cómo usarlo (con Claude Code)

### Requisitos previos

- [Claude Code](https://claude.com/claude-code) instalado
- [Google Chrome](https://www.google.com/chrome/) instalado (lo usa `render.sh` en modo headless)

### Disparar un post

Escribe alguna de estas frases en Claude Code (el agente identificará automáticamente el tipo de post según la frase):

**Step-by-step** (tutoriales):
- `nuevo post: {tema}`
- `hagamos un post sobre {tema}`
- `tutorial de {tema}`

**News** (cuando esté construido):
- `post de noticia: {titular}`
- `esto salió hoy: {url}`

**Informativos** (cuando esté construido):
- `post informativo de {tema}`
- `post de hacks de {tema}`
- `5 prompts para {tema}`

El agente te pedirá el contexto faltante, te propondrá el desglose en texto, y solo después de tu aprobación generará y renderizará los slides.

### Renderizar manualmente

```bash
./render.sh PostTypes/step-by-step/Outputs/{topic-slug}
```

Convierte todos los `.html` de la carpeta a PNGs del mismo nombre.

---

## Cómo añadir un nuevo tipo de post

1. Crea referencias visuales y déjalas en `PostTypes/{nuevo-tipo}/Inspiracion/`
2. Co-crea con Claude el skill que captura el patrón visual de esas referencias en `PostTypes/{nuevo-tipo}/Skills/`
3. Actualiza el `README.md` del tipo con el workflow específico
4. Añade el tipo y sus trigger phrases a la sección 1 del [CLAUDE.md](CLAUDE.md) raíz

---

## Créditos visuales

El lenguaje visual está inspirado en el estilo de creadores de contenido AI (referencia: @ramiro.cubria — solo estilo visual, no el handle). El proyecto está adaptado a la voz y audiencia de **@lucianomusellaa**.
