from pathlib import Path
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "dist" / "assets" / "documents" / "brochure-plastic-bags-sas.pdf"
OUTPUT = ROOT / "dist" / "assets" / "brands"

# Image objects containing the client marks on brochure pages 6 and 7.
BRANDS = {
    (6, "X21.png"): "d1.png",
    (6, "X23.png"): "euro-supermercado.png",
    (6, "X27.png"): "isimo.png",
    (7, "X14.png"): "ara.png",
    (7, "X20.jpg"): "alkosto.jpg",
    (7, "X9.png"): "gabrica.png",
}


def main() -> None:
    reader = PdfReader(PDF)
    OUTPUT.mkdir(parents=True, exist_ok=True)

    for (page_number, image_name), output_name in BRANDS.items():
        page_images = {image.name: image for image in reader.pages[page_number - 1].images}
        image = page_images[image_name]
        (OUTPUT / output_name).write_bytes(image.data)


if __name__ == "__main__":
    main()
