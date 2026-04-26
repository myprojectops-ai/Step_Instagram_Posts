from pathlib import Path
import textwrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[4]
OUT_DIR = Path(__file__).resolve().parent
W, H = 1080, 1350

COLORS = {
    "black": "#0E0E0E",
    "body": "#3A3A38",
    "muted": "#8A8780",
    "cream": "#F5F2ED",
    "coral": "#E85D3C",
    "orange": "#F49D37",
    "green": "#5B8C5A",
    "blue": "#4A90D9",
    "purple": "#8B6CC1",
    "teal": "#5A9E9E",
    "white": "#FFFFFF",
}


def font(name, size):
    return ImageFont.truetype(str(ROOT / "Assets" / "Fonts" / name), size)


FONT_HANDLE = font("Inter-Medium.ttf", 22)
FONT_TITLE = font("Inter-Black.ttf", 58)
FONT_TITLE_SMALL = font("Inter-Black.ttf", 54)
FONT_NUM = font("Inter-ExtraBold.ttf", 30)
FONT_ITEM = font("Inter-ExtraBold.ttf", 25)
FONT_DESC = font("Inter-Medium.ttf", 18)
FONT_FOOTER = font("Inter-Medium.ttf", 16)


def text_size(draw, text, fnt):
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def draw_centered(draw, text, y, fnt, fill, x_center=W // 2):
    tw, th = text_size(draw, text, fnt)
    draw.text((x_center - tw / 2, y), text, font=fnt, fill=fill)
    return y + th


def draw_centered_segments(draw, segments, y, fnt, gap=10):
    widths = [text_size(draw, text, fnt)[0] for text, _ in segments]
    total = sum(widths) + gap * (len(segments) - 1)
    x = (W - total) / 2
    for (text, fill), tw in zip(segments, widths):
        draw.text((x, y), text, font=fnt, fill=fill)
        x += tw + gap
    return y + text_size(draw, segments[0][0], fnt)[1]


def draw_wrapped(draw, text, box, fnt, fill, line_spacing=6):
    x1, y1, x2, y2 = box
    max_width = x2 - x1
    words = text.split()
    lines = []
    line = ""
    for word in words:
        test = f"{line} {word}".strip()
        if text_size(draw, test, fnt)[0] <= max_width:
            line = test
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)

    line_h = text_size(draw, "Ag", fnt)[1] + line_spacing
    total_h = line_h * len(lines) - line_spacing
    y = y1 + max(0, (y2 - y1 - total_h) / 2)
    for line in lines:
        draw.text((x1, y), line, font=fnt, fill=fill)
        y += line_h


def fit_title(draw, title, box):
    x1, y1, x2, y2 = box
    max_width = x2 - x1
    for size in range(25, 17, -1):
        fnt = font("Inter-ExtraBold.ttf", size)
        lines = textwrap.wrap(title, width=22)
        if all(text_size(draw, line, fnt)[0] <= max_width for line in lines):
            line_h = text_size(draw, "Ag", fnt)[1] + 4
            if len(lines) * line_h <= (y2 - y1):
                return fnt, lines, line_h
    fnt = font("Inter-Bold.ttf", 18)
    return fnt, textwrap.wrap(title, width=26)[:3], text_size(draw, "Ag", fnt)[1] + 4


def draw_card(draw, item):
    x1, y1, x2, y2 = item["box"]
    cx, cy = item["badge"]
    draw.text(
        (cx - text_size(draw, str(item["n"]), FONT_NUM)[0] / 2, cy - 19),
        str(item["n"]),
        font=FONT_NUM,
        fill=item["color"],
    )

    title_box = (x1 + 92, y1 + 46, x2 - 110, y1 + 116)
    title_font, title_lines, title_line_h = fit_title(draw, item["title"], title_box)
    title_y = title_box[1] + max(0, (title_box[3] - title_box[1] - len(title_lines) * title_line_h) / 2)
    for line in title_lines:
        draw.text((title_box[0], title_y), line, font=title_font, fill=COLORS["black"])
        title_y += title_line_h

    draw_wrapped(
        draw,
        item["desc"],
        (x1 + 92, y1 + 122, x2 - 58, y2 - 34),
        FONT_DESC,
        COLORS["body"],
        line_spacing=5,
    )


def main():
    comp = Image.open(OUT_DIR / "composition.png").convert("RGBA")
    if comp.size != (W, H):
        comp = comp.resize((W, H), Image.LANCZOS)
    canvas = comp.copy()
    draw = ImageDraw.Draw(canvas)

    draw_centered_segments(
        draw,
        [("6", COLORS["coral"]), ("formas en que", COLORS["black"])],
        92,
        FONT_TITLE,
        gap=14,
    )
    draw_centered(draw, "los agentes de Notion", 154, FONT_TITLE_SMALL, COLORS["black"])
    draw_centered(draw, "ahorran tiempo en empresas", 212, FONT_TITLE_SMALL, COLORS["black"])

    cards = [
        {
            "n": 1,
            "title": "Responden preguntas repetidas",
            "desc": "Usan el conocimiento del workspace y apps conectadas para evitar interrupciones.",
            "color": COLORS["coral"],
            "box": (70, 315, 522, 590),
            "badge": (116, 370),
        },
        {
            "n": 2,
            "title": "Enrutan tareas automáticamente",
            "desc": "Capturan solicitudes, priorizan y asignan trabajo al equipo correcto.",
            "color": COLORS["orange"],
            "box": (555, 315, 1008, 590),
            "badge": (603, 370),
        },
        {
            "n": 3,
            "title": "Preparan reportes recurrentes",
            "desc": "Reúnen avances y escriben estados diarios, semanales u OKR sin perseguir updates.",
            "color": COLORS["green"],
            "box": (70, 625, 522, 890),
            "badge": (116, 680),
        },
        {
            "n": 4,
            "title": "Actualizan docs y bases de datos",
            "desc": "Editan páginas, consultan bases y mantienen trackers con contexto fresco.",
            "color": COLORS["blue"],
            "box": (555, 625, 1008, 890),
            "badge": (603, 680),
        },
        {
            "n": 5,
            "title": "Conectan contexto entre apps",
            "desc": "Trabajan con Notion y conexiones como Slack, Mail, Calendar y más.",
            "color": COLORS["purple"],
            "box": (70, 925, 522, 1192),
            "badge": (116, 982),
        },
        {
            "n": 6,
            "title": "Reducen trabajo operativo",
            "desc": "Braintrust reporta 20+ min ahorrados por update y horas al día en flujos automatizados.",
            "color": COLORS["teal"],
            "box": (555, 925, 1008, 1192),
            "badge": (603, 982),
        },
    ]
    for card in cards:
        draw_card(draw, card)

    footer = "Fuente: Notion Agents + caso Braintrust"
    tw, _ = text_size(draw, footer, FONT_FOOTER)
    draw.text(((W - tw) / 2, 1264), footer, font=FONT_FOOTER, fill=COLORS["muted"])
    handle = "@lucianomusellaa"
    tw, _ = text_size(draw, handle, FONT_HANDLE)
    draw.text(((W - tw) / 2, 1290), handle, font=FONT_HANDLE, fill=COLORS["muted"])

    out = OUT_DIR / "info_v1_grid-cards.png"
    canvas.convert("RGB").save(out, quality=95)
    print(out)
    print(canvas.size)


if __name__ == "__main__":
    main()
