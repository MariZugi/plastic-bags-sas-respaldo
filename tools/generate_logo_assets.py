from __future__ import annotations

import base64
import math
from io import BytesIO
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(
    "C:/Users/LENOVO/AppData/Local/Temp/"
    "codex-clipboard-74fd7765-8922-4ece-bb7d-951013b757e4.png"
)
OUT = ROOT / "dist" / "assets" / "logos"
OUT.mkdir(parents=True, exist_ok=True)


def remove_white_background(image: Image.Image) -> Image.Image:
    image = image.convert("RGBA")
    pixels = []
    for y in range(image.height):
        for x in range(image.width):
            red, green, blue, _ = image.getpixel((x, y))
            distance = math.sqrt((255 - red) ** 2 + (255 - green) ** 2 + (255 - blue) ** 2)
            alpha = max(0, min(255, round((distance - 55) * 2.6)))
            leaf_zone = x < 57 or x > 203
            brightness = (red + green + blue) / 3
            color = (156, 191, 108) if leaf_zone and brightness > 115 else (72, 100, 82)
            pixels.append((*color, alpha))
    image.putdata(pixels)
    return image


def main() -> None:
    source = Image.open(SOURCE)
    transparent = remove_white_background(source)
    png = transparent.resize(
        (transparent.width * 4, transparent.height * 4),
        Image.Resampling.LANCZOS,
    )

    png_path = OUT / "plastic-bags-logo.png"
    png.save(png_path, optimize=True)

    buffer = BytesIO()
    png.save(buffer, format="PNG", optimize=True)
    encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{png.width}" height="{png.height}" viewBox="0 0 {png.width} {png.height}" role="img" aria-labelledby="title desc">
  <title id="title">Plastic Bags SAS</title>
  <desc id="desc">Logotipo horizontal verde de Plastic Bags SAS con hojas a ambos lados.</desc>
  <image width="{png.width}" height="{png.height}" href="data:image/png;base64,{encoded}" />
</svg>
'''
    svg_path = OUT / "plastic-bags-logo.svg"
    svg_path.write_text(svg, encoding="utf-8")

    print(svg_path)
    print(png_path)


if __name__ == "__main__":
    main()
