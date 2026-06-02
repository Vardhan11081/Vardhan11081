#!/usr/bin/env python3
"""Generate CloudInvoke UI processing animation frames (1920x1080)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

W, H = 1920, 1080
OUT = Path(__file__).parent / "frames" / "ui"
OUT.mkdir(parents=True, exist_ok=True)

# Palette
BG_TOP = (8, 24, 48)
BG_BOT = (16, 52, 96)
ACCENT = (56, 189, 248)
WHITE = (240, 248, 255)
GRID = (30, 90, 140)


def lerp(a, b, t):
    return int(a + (b - a) * t)


def gradient_bg(draw, t=0.0):
    for y in range(H):
        p = y / H
        r = lerp(BG_TOP[0], BG_BOT[0], p)
        g = lerp(BG_TOP[1], BG_BOT[1], p)
        b = lerp(BG_TOP[2], BG_BOT[2], p)
        draw.line([(0, y), (W, y)], fill=(r, g, b))


def try_font(size):
    for name in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_frame(i: int, total: int):
    img = Image.new("RGB", (W, H), BG_TOP)
    draw = ImageDraw.Draw(img)
    gradient_bg(draw)
    t = i / max(total - 1, 1)

    title_f = try_font(72)
    small_f = try_font(28)
    draw.text((80, 60), "CloudInvoke", fill=WHITE, font=title_f)
    draw.text((80, 140), "AI Evidence Enhancement", fill=ACCENT, font=small_f)

    # Panel
    px, py, pw, ph = 120, 220, 1680, 720
    draw.rounded_rectangle([px, py, px + pw, py + ph], radius=24, outline=ACCENT, width=3, fill=(12, 36, 68))

    # Upload zone
    uz = [px + 60, py + 50, px + 520, py + ph - 50]
    draw.rounded_rectangle(uz, radius=16, outline=GRID, width=2, fill=(10, 30, 55))
    draw.text((uz[0] + 40, uz[1] + 30), "Evidence Upload", fill=WHITE, font=small_f)

    # Progress bar
    bar_y = uz[3] - 80
    bar_x1, bar_x2 = uz[0] + 40, uz[2] - 40
    draw.rectangle([bar_x1, bar_y, bar_x2, bar_y + 18], fill=(20, 50, 80))
    prog = min(1.0, t * 1.4)
    draw.rectangle([bar_x1, bar_y, bar_x1 + int((bar_x2 - bar_x1) * prog), bar_y + 18], fill=ACCENT)
    draw.text((bar_x1, bar_y - 36), f"Processing… {int(prog * 100)}%", fill=WHITE, font=small_f)

    # Neural grid (right side)
    gx0 = px + 580
    for row in range(12):
        for col in range(20):
            x = gx0 + col * 52
            y = py + 80 + row * 48
            pulse = (math.sin(t * 12 + col * 0.4 + row * 0.3) + 1) / 2
            if x > px + pw - 80:
                continue
            c = lerp(20, 180, pulse * prog)
            draw.rectangle([x, y, x + 40, y + 36], fill=(c // 3, c // 2 + 40, c + 60))

    # Scan line
    scan_y = py + 60 + int((ph - 120) * ((t * 2) % 1.0))
    draw.line([(gx0, scan_y), (px + pw - 40, scan_y)], fill=ACCENT, width=2)

    # Plate preview area
    plate_box = [px + pw - 520, py + ph - 280, px + pw - 60, py + ph - 60]
    draw.rounded_rectangle(plate_box, radius=12, outline=WHITE, width=2, fill=(6, 20, 40))

    # Simulated plate: blur -> sharp
    plate_text = "BX47 KLM"
    blur_amt = max(0, int(8 * (1 - min(1.0, t * 1.2))))
    plate_f = try_font(64)
    plate_img = Image.new("RGBA", (400, 120), (0, 0, 0, 0))
    pd = ImageDraw.Draw(plate_img)
    pd.text((20, 20), plate_text, fill=(255, 255, 255, 255), font=plate_f)
    if blur_amt:
        plate_img = plate_img.filter(ImageFilter.GaussianBlur(blur_amt))
    img.paste(plate_img, (plate_box[0] + 40, plate_box[1] + 60), plate_img)

    draw.text((plate_box[0], plate_box[1] - 40), "Plate reconstruction", fill=ACCENT, font=small_f)

    # plate_number.txt file icon when near end
    if t > 0.75:
        fx, fy = px + 60, py + ph - 200
        draw.rounded_rectangle([fx, fy, fx + 360, fy + 120], radius=10, fill=(20, 60, 100), outline=ACCENT, width=2)
        draw.text((fx + 24, fy + 20), "plate_number.txt", fill=WHITE, font=small_f)
        draw.text((fx + 24, fy + 62), "BX47 KLM", fill=ACCENT, font=try_font(36))

    # Data flow particles
    for p in range(30):
        pxp = gx0 + int((p * 97 + i * 15) % (pw - 600))
        pyp = py + 100 + int((p * 53 + i * 11) % (ph - 200))
        draw.ellipse([pxp, pyp, pxp + 6, pyp + 6], fill=ACCENT)

    path = OUT / f"ui_{i:04d}.png"
    img.save(path, quality=95)
    return path


def main():
    total = 72  # 3 sec @ 24fps
    for i in range(total):
        draw_frame(i, total)
    print(f"Wrote {total} UI frames to {OUT}")


if __name__ == "__main__":
    main()
