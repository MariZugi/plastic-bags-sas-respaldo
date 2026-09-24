from pathlib import Path
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(r"C:\Users\LENOVO\AppData\Local\Temp\browser-use\assets\ca37b821-9242-4a19-9ab0-1965ff4e431e")

FILES = {
    "3cfb4cfe49f6ceda": ROOT / "dist/assets/private-label/lets-be-fresh-vainilla-4-rollos.png",
    "587e33a97914a060": ROOT / "dist/assets/private-label/lets-be-fresh-vainilla-20-rollos.png",
    "c2732bd304833bae": ROOT / "dist/assets/private-label/lets-be-fresh-compostable-4-rollos.png",
    "f1418e5e5c51d4ad": ROOT / "dist/assets/private-label/lets-be-fresh-compostable-12-rollos.png",
    "ce863b0f61958849": ROOT / "dist/assets/brands/laika.png",
}


def main() -> None:
    for source_name, destination in FILES.items():
        destination.parent.mkdir(parents=True, exist_ok=True)
        with Image.open(SOURCE / source_name) as image:
            image.save(destination, format="PNG", optimize=True)
            print(destination.relative_to(ROOT), image.size, image.mode)


if __name__ == "__main__":
    main()
