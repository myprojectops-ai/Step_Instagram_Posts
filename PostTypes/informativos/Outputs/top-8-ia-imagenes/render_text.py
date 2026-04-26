from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter


ROOT = Path(__file__).resolve().parents[4]
OUT_DIR = Path(__file__).resolve().parent
FONT_DIR = ROOT / "Assets" / "Fonts"

W, H = 1080, 1350
CREAM = "#F5F2ED"
GRID = "#E8E4DD"
BLACK = "#0E0E0E"
BODY = "#3A3A38"
GREY = "#8A8780"
CORAL = "#E85D3C"
YELLOW = "#FFE45C"
COLORS = ["#E85D3C", "#F49D37", "#5B8C5A", "#4A90D9", "#8B6CC1", "#5A9E9E", "#C7727D", "#E85D3C"]


TOOLS = [
    ("ChatGPT Images", "GENERALISTA", "La más versátil para crear, editar e iterar conversando."),
    ("Nano Banana Pro", "TEXTO + INFOGRAFÍAS", "Ideal para piezas con texto, diagramas y control visual."),
    ("Midjourney V7", "ESTÉTICA", "La reina de textura, mood y dirección artística premium."),
    ("Ideogram 3.0", "POSTERS + LOGOS", "Fuerte para lettering, afiches y diseño con palabras."),
    ("FLUX.2", "OPEN / API", "Potente para flujos pro, referencias y producción técnica."),
    ("Adobe Firefly", "MARCAS", "Opción segura para equipos, marcas y ecosistema Adobe."),
    ("Recraft V3", "DISEÑO GRÁFICO", "Muy buena para estilos consistentes y texto ubicado."),
    ("Freepik Mystic", "MARKETING", "Rápida para renders, piezas comerciales y contenido diario."),
]


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_DIR / name), size)


FONT_HANDLE = font("Inter-Medium.ttf", 24)
FONT_TITLE = font("Inter-Black.ttf", 58)
FONT_TITLE_SMALL = font("Inter-Black.ttf", 52)
FONT_CARD = font("Inter-ExtraBold.ttf", 27)
FONT_BADGE = font("Inter-Bold.ttf", 13)
FONT_DESC = font("Inter-Medium.ttf", 19)
FONT_NUM = font("Inter-ExtraBold.ttf", 25)
FONT_FOOTER = font("Inter-Medium.ttf", 18)


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def draw_center(draw: ImageDraw.ImageDraw, text: str, y: int, fnt: ImageFont.FreeTypeFont, fill: str) -> None:
    tw, _ = text_size(draw, text, fnt)
    draw.text(((W - tw) / 2, y), text, font=fnt, fill=fill)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_w: int) -> list[str]:
    words = text.split()
    lines = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if text_size(draw, candidate, fnt)[0] <= max_w:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def rounded_shadow(base: Image.Image, box: tuple[int, int, int, int], radius: int = 28) -> None:
    x1, y1, x2, y2 = box
    shadow = Image.new("RGBA", base.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((x1 + 6, y1 + 10, x2 + 6, y2 + 10), radius=radius, fill=(14, 14, 14, 20))
    shadow = shadow.filter(ImageFilter.GaussianBlur(14))
    base.alpha_composite(shadow)


def draw_icon(draw: ImageDraw.ImageDraw, kind: int, x: int, y: int, color: str) -> None:
    if kind % 4 == 0:
        draw.ellipse((x, y, x + 34, y + 34), outline=color, width=4)
        draw.ellipse((x + 11, y + 11, x + 23, y + 23), outline=color, width=3)
    elif kind % 4 == 1:
        draw.line((x + 2, y + 30, x + 30, y + 2), fill=color, width=4)
        draw.line((x + 20, y + 2, x + 34, y + 16), fill=color, width=4)
    elif kind % 4 == 2:
        draw.polygon([(x + 18, y), (x + 23, y + 13), (x + 36, y + 18), (x + 23, y + 23), (x + 18, y + 36), (x + 13, y + 23), (x, y + 18), (x + 13, y + 13)], outline=color)
        draw.line((x + 18, y, x + 18, y + 36), fill=color, width=2)
    else:
        draw.rounded_rectangle((x, y + 4, x + 38, y + 32), radius=5, outline=color, width=3)
        draw.line((x + 6, y + 24, x + 16, y + 15, x + 25, y + 22, x + 33, y + 12), fill=color, width=3)


def draw_title(draw: ImageDraw.ImageDraw) -> None:
    draw_center(draw, "@lucianomusellaa", 48, FONT_HANDLE, GREY)
    y = 102
    line1 = "Las "
    number = "8"
    line1b = " mejores IA"
    total = (
        text_size(draw, line1, FONT_TITLE)[0]
        + text_size(draw, number, FONT_TITLE)[0]
        + text_size(draw, line1b, FONT_TITLE)[0]
    )
    x = (W - total) / 2
    draw.text((x, y), line1, font=FONT_TITLE, fill=BLACK)
    x += text_size(draw, line1, FONT_TITLE)[0]
    draw.text((x, y), number, font=FONT_TITLE, fill=CORAL)
    x += text_size(draw, number, FONT_TITLE)[0]
    draw.text((x, y), line1b, font=FONT_TITLE, fill=BLACK)

    line2a = "para generar "
    line2b = "imágenes"
    w2a = text_size(draw, line2a, FONT_TITLE_SMALL)[0]
    w2b = text_size(draw, line2b, FONT_TITLE_SMALL)[0]
    pad_x, pad_y = 13, 5
    total2 = w2a + w2b + pad_x * 2
    x2 = (W - total2) / 2
    y2 = 170
    draw.text((x2, y2), line2a, font=FONT_TITLE_SMALL, fill=BLACK)
    box_x = x2 + w2a
    bbox = draw.textbbox((box_x + pad_x, y2), line2b, font=FONT_TITLE_SMALL)
    draw.rounded_rectangle((box_x, bbox[1] - pad_y, box_x + w2b + pad_x * 2, bbox[3] + pad_y), radius=9, fill=YELLOW)
    draw.text((box_x + pad_x, y2), line2b, font=FONT_TITLE_SMALL, fill=BLACK)


def main() -> None:
    canvas = Image.new("RGBA", (W, H), CREAM)
    draw = ImageDraw.Draw(canvas)

    for x in range(0, W, 40):
        draw.line((x, 0, x, H), fill=GRID, width=1)
    for y in range(0, H, 40):
        draw.line((0, y, W, y), fill=GRID, width=1)

    # Subtle editorial dots.
    for i in range(7):
        for j in range(3):
            draw.ellipse((44 + i * 22, 286 + j * 22, 51 + i * 22, 293 + j * 22), fill="#D5D0C8")
    for i in range(5):
        draw.line((930 + i * 16, 130, 1060 + i * 16, 0), fill="#CFC8BD", width=2)

    draw_title(draw)

    card_w, card_h = 462, 192
    x_positions = [58, 560]
    y_positions = [284, 514, 744, 974]

    for idx, (name, badge, desc) in enumerate(TOOLS):
        col = idx % 2
        row = idx // 2
        x = x_positions[col]
        y = y_positions[row]
        color = COLORS[idx]
        rounded_shadow(canvas, (x, y, x + card_w, y + card_h))
        draw.rounded_rectangle((x, y, x + card_w, y + card_h), radius=30, fill="#FFFFFF")
        draw.ellipse((x + 28, y + 28, x + 76, y + 76), fill=color)
        num = str(idx + 1)
        nw, nh = text_size(draw, num, FONT_NUM)
        draw.text((x + 52 - nw / 2, y + 50 - nh / 2 - 2), num, font=FONT_NUM, fill="#FFFFFF")
        text_x = x + 94
        draw.text((text_x, y + 29), name, font=FONT_CARD, fill=BLACK)
        bw, bh = text_size(draw, badge, FONT_BADGE)
        draw.rounded_rectangle((text_x, y + 67, text_x + bw + 18, y + 67 + bh + 9), radius=12, fill=color)
        draw.text((text_x + 9, y + 70), badge, font=FONT_BADGE, fill="#FFFFFF")
        lines = wrap(draw, desc, FONT_DESC, 315)
        for line_i, line in enumerate(lines[:2]):
            draw.text((text_x, y + 103 + line_i * 25), line, font=FONT_DESC, fill=BODY)
        draw_icon(draw, idx, x + card_w - 74, y + card_h - 62, color)

    footer = "Guarda este mapa para elegir la IA correcta según tu objetivo visual."
    draw_center(draw, footer, 1246, FONT_FOOTER, GREY)

    out = OUT_DIR / "info_v1_top8-ia-imagenes.png"
    canvas.convert("RGB").save(out, quality=95)
    print(out)


if __name__ == "__main__":
    main()
