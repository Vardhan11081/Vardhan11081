#!/usr/bin/env python3
"""Generate title and end cards."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
OUT = Path(__file__).parent / "storyboards"


def font(size, bold=True):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    if not bold:
        paths.reverse()
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            pass
    return ImageFont.load_default()


def card(title, subtitle=None, dark=True):
    img = Image.new("RGB", (W, H), (8, 20, 40) if dark else (240, 248, 255))
    d = ImageDraw.Draw(img)
    if dark:
        for y in range(H):
            t = y / H
            c = int(8 + 40 * t)
            d.line([(0, y), (W, y)], fill=(c, c + 20, c + 50))
    d.text((W // 2, H // 2 - 80), title, fill=(240, 248, 255) if dark else (8, 24, 48), font=font(96), anchor="mm")
    if subtitle:
        d.text((W // 2, H // 2 + 40), subtitle, fill=(56, 189, 248), font=font(42), anchor="mm")
    return img


def main():
    card("CloudInvoke", "AI Evidence Enhancement").save(OUT / "title_cloudinvoke.png")
    card(
        "CloudInvoke",
        "Turning Blurred Evidence into Clear Answers",
    ).save(OUT / "end_card.png")
    print("Title cards saved.")


if __name__ == "__main__":
    main()
