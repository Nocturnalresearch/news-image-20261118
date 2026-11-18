#!/usr/bin/env python3
"""Draw the 18 November 2026 world-news front page (1024x1024 PNG).

One image summing up the day's news, drawn entirely with PIL so every
letter is crisp and legible (no AI-garbled text). Layout: masthead with
the date, then a 2x2 grid of stories, each with a small illustration,
a region tag, a bold headline and a one-line subhead.

Stories (researched from Reuters/AP/AFP/WSJ coverage of 18 Nov 2026):
  1. Gulf strikes — US hits Iran's Qeshm Island; Iran strikes Kuwait & Bahrain.
  2. Kerch Bridge — Ukraine attack partly collapses the Crimea bridge.
  3. Shenzhen summit — Xi hosts Putin; Trump joins Thursday.
  4. GTA VI eve — launches tomorrow; New Zealand plays first; reviews 99/100.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 247, 240)
NAVY = (15, 42, 74)
NAVY_DARK = (10, 26, 46)
GOLD = (232, 193, 90)
INK = (20, 28, 38)
GRAY = (68, 68, 68)
WHITE = (255, 255, 255)

F_SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
F_SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
F_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def vgrad(img, box, top, bottom):
    """Vertical gradient inside box (x0, y0, x1, y1)."""
    x0, y0, x1, y1 = box
    h = max(1, y1 - y0)
    for y in range(h):
        t = y / h
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        img.paste(c, (x0, y0 + y, x1, y0 + y + 1))


def wrap(draw, text, fnt, max_w):
    """Wrap text to fit max_w pixels; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def centered(draw, text, fnt, y, color, cx=W // 2):
    draw.text((cx, y), text, font=fnt, fill=color, anchor="mt")


def starburst(d, cx, cy, r_out, r_in, n=12, color=(255, 140, 0)):
    import math
    pts = []
    for i in range(n * 2):
        r = r_out if i % 2 == 0 else r_in
        a = math.pi * i / n
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.polygon(pts, fill=color)


def draw_gulf(d, box):
    x0, y0, x1, y1 = box
    vgrad(d._image, box, (10, 26, 46), (30, 70, 110))
    # sea
    d.rectangle([x0, y1 - 42, x1, y1], fill=(8, 20, 36))
    d.line([x0, y1 - 42, x1, y1 - 42], fill=(90, 140, 190), width=2)
    # missile trail: short diagonal streak from lower-left toward the burst
    d.line([x0 + 60, y1 - 46, x0 + 300, y0 + 88], fill=(255, 220, 120), width=5)
    d.line([x0 + 60, y1 - 46, x0 + 300, y0 + 88], fill=(255, 240, 180), width=2)
    # explosion burst
    starburst(d, x0 + 350, y0 + 62, 58, 30, color=(255, 140, 0))
    starburst(d, x0 + 350, y0 + 62, 34, 18, color=(255, 210, 60))
    d.ellipse([x0 + 332, y0 + 44, x0 + 368, y0 + 80], fill=(255, 240, 180))
    # radar / airbase silhouette on the left
    d.rectangle([x0 + 46, y0 + 118, x0 + 54, y1 - 42], fill=(5, 12, 24))
    d.ellipse([x0 + 30, y0 + 96, x0 + 70, y0 + 122], outline=(200, 220, 255), width=4)
    d.line([x0 + 50, y0 + 108, x0 + 50, y0 + 118], fill=(200, 220, 255), width=3)
    # ship silhouette on the sea
    d.rectangle([x0 + 380, y1 - 52, x0 + 450, y1 - 44], fill=(5, 12, 24))
    d.rectangle([x0 + 405, y1 - 66, x0 + 425, y1 - 52], fill=(5, 12, 24))


def draw_kerch(d, box):
    x0, y0, x1, y1 = box
    vgrad(d._image, box, (188, 214, 232), (220, 232, 240))
    # clouds
    for cx, cy, rx in [(90, 34, 46), (250, 22, 36), (400, 40, 42)]:
        d.ellipse([x0 + cx - rx, y0 + cy - 14, x0 + cx + rx, y0 + cy + 14], fill=(255, 255, 255))
    # water
    d.rectangle([x0, y1 - 52, x1, y1], fill=(46, 109, 164))
    for wx in (60, 200, 340):
        d.arc([x0 + wx, y1 - 40, x0 + wx + 60, y1 - 20], start=200, end=340, fill=(180, 220, 245), width=3)
    # bridge deck: two surviving spans, middle broken
    deck_y = y0 + 96
    d.rectangle([x0, deck_y, x0 + 205, deck_y + 12], fill=(70, 70, 78))
    d.rectangle([x0 + 283, deck_y, x1, deck_y + 12], fill=(70, 70, 78))
    # support piers
    d.rectangle([x0 + 90, deck_y + 12, x0 + 102, y1 - 52], fill=(90, 90, 98))
    d.rectangle([x0 + 380, deck_y + 12, x0 + 392, y1 - 52], fill=(90, 90, 98))
    # arch over the left span
    d.arc([x0 + 40, deck_y - 52, x0 + 200, deck_y + 12], start=180, end=360, fill=(70, 70, 78), width=7)
    # falling broken segment (tilted)
    d.polygon([(x0 + 215, deck_y + 2), (x0 + 278, deck_y + 2), (x0 + 262, deck_y + 46), (x0 + 228, deck_y + 58)], fill=(60, 60, 68))
    # smoke puffs at the break
    for sx, sy, sr in [(240, 66, 16), (258, 50, 20), (232, 44, 13)]:
        d.ellipse([x0 + sx - sr, y0 + sy - sr, x0 + sx + sr, y0 + sy + sr], fill=(120, 120, 125))
    # splash where the segment hits the water
    d.ellipse([x0 + 228, y1 - 62, x0 + 268, y1 - 38], outline=(255, 255, 255), width=3)


def draw_summit(d, box):
    x0, y0, x1, y1 = box
    vgrad(d._image, box, (240, 234, 222), (214, 204, 186))
    # skyline silhouettes
    base = y1
    heights = [58, 92, 70, 110, 78, 96, 62, 88]
    bw = (x1 - x0) // len(heights)
    for i, hh in enumerate(heights):
        d.rectangle([x0 + i * bw + 4, base - hh, x0 + (i + 1) * bw - 4, base], fill=(52, 58, 66))
    # three flags on poles above the skyline
    flag_w, flag_h = 96, 64
    fy = y0 + 14
    # China: red field, one gold star
    fx = x0 + 62
    d.rectangle([fx, fy, fx + flag_w, fy + flag_h], fill=(222, 41, 16))
    starburst(d, fx + 22, fy + 20, 12, 5, n=5, color=(255, 222, 0))
    # Russia: white / blue / red horizontal stripes
    fx = x0 + 196
    d.rectangle([fx, fy, fx + flag_w, fy + 22], fill=(255, 255, 255))
    d.rectangle([fx, fy + 22, fx + flag_w, fy + 43], fill=(0, 57, 166))
    d.rectangle([fx, fy + 43, fx + flag_w, fy + flag_h], fill=(213, 0, 50))
    d.rectangle([fx, fy, fx + flag_w, fy + flag_h], outline=(120, 120, 120), width=2)
    # USA: red/white stripes + blue canton
    fx = x0 + 330
    for s in range(7):
        d.rectangle([fx, fy + s * 9, fx + flag_w, fy + s * 9 + 9],
                    fill=(178, 34, 52) if s % 2 == 0 else (255, 255, 255))
    d.rectangle([fx, fy, fx + 40, fy + 34], fill=(60, 59, 110))
    d.rectangle([fx, fy, fx + flag_w, fy + flag_h], outline=(120, 120, 120), width=2)


def draw_gta(d, box):
    x0, y0, x1, y1 = box
    vgrad(d._image, box, (194, 24, 91), (255, 152, 0))
    # sun
    d.ellipse([x0 + 196, y0 + 26, x0 + 292, y0 + 122], fill=(255, 236, 160))
    # skyline silhouettes
    base = y1
    heights = [66, 104, 78, 122, 88, 108, 70, 96]
    bw = (x1 - x0) // len(heights)
    for i, hh in enumerate(heights):
        d.rectangle([x0 + i * bw + 3, base - hh, x0 + (i + 1) * bw - 3, base], fill=(30, 8, 40))
    # palm trees: simple silhouettes (curved trunk + straight fronds)
    import math
    for px, ph in [(70, 96), (428, 84)]:
        top_x, top_y = x0 + px + 10, base - ph
        d.line([x0 + px, base, top_x, top_y], fill=(20, 6, 28), width=7)
        for ang in (-75, -40, -5, 30, 65):
            r = math.radians(ang)
            ex = top_x + 36 * math.sin(r)
            ey = top_y - 10 + 26 * math.cos(r) * 0.4
            d.line([top_x, top_y, ex, ey], fill=(20, 6, 28), width=5)
    # big VI
    f_vi = font(F_SANS_B, 84)
    d.text((x0 + 244, y0 + 8), "VI", font=f_vi, fill=(255, 255, 255), anchor="mt",
           stroke_width=3, stroke_fill=(120, 10, 60))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.rectangle([0, 0, W, 128], fill=NAVY)
    d.rectangle([0, 128, W, 132], fill=GOLD)
    centered(d, "WORLD NEWS", font(F_SERIF_B, 62), 12, WHITE)
    centered(d, "WEDNESDAY, 18 NOVEMBER 2026", font(F_SANS_B, 30), 84, GOLD)

    # ---- tagline ----
    centered(d, "Four stories that defined the day", font(F_SANS, 21), 140, GRAY)

    # ---- panels ----
    stories = [
        ("MIDDLE EAST", (178, 34, 52), draw_gulf,
         "U.S. hits Iran island; Iran strikes Kuwait and Bahrain",
         "Qeshm missile site bombed; Tehran targets U.S. bases in the Gulf"),
        ("UKRAINE", (0, 90, 160), draw_kerch,
         "Kerch Bridge partly collapses under Ukrainian attack",
         "An arch falls into the strait on the second day of strikes"),
        ("CHINA", (176, 32, 32), draw_summit,
         "Xi hosts Putin in Shenzhen; Trump joins Thursday",
         "Three leaders to talk Ukraine, Iran and trade"),
        ("CULTURE", (123, 31, 162), draw_gta,
         "GTA VI launches tomorrow; New Zealand plays first",
         "Reviews hail 99/100 as the biggest game launch begins"),
    ]
    margin, gap = 16, 16
    pw = (W - margin * 2 - gap) // 2
    ph = (958 - 166 - gap) // 2
    f_tag = font(F_SANS_B, 16)
    f_head = font(F_SANS_B, 30)
    f_sub = font(F_SANS, 19)
    for i, (tag, color, artist, head, sub) in enumerate(stories):
        px = margin + (i % 2) * (pw + gap)
        py = 166 + (i // 2) * (ph + gap)
        # card background + border
        d.rectangle([px, py, px + pw, py + ph], fill=WHITE, outline=(200, 196, 188), width=2)
        # illustration
        artist(d, (px + 2, py + 2, px + pw - 2, py + 182))
        # tag strip
        d.rectangle([px + 2, py + 182, px + pw - 2, py + 212], fill=color)
        d.text((px + 14, py + 197), tag, font=f_tag, fill=WHITE, anchor="lm")
        # headline (2 lines)
        lines = wrap(d, head, f_head, pw - 28)
        y = py + 224
        for ln in lines[:2]:
            d.text((px + 14, y), ln, font=f_head, fill=INK)
            y += 36
        # subhead (2 lines)
        lines = wrap(d, sub, f_sub, pw - 28)
        y = py + 224 + 36 * min(2, len(wrap(d, head, f_head, pw - 28))) + 6
        for ln in lines[:2]:
            d.text((px + 14, y), ln, font=f_sub, fill=GRAY)
            y += 24

    # ---- footer ----
    d.rectangle([0, 966, W, H], fill=NAVY_DARK)
    centered(d, "Sources: Reuters  ·  AP  ·  AFP  ·  Wall Street Journal     —     18 November 2026",
             font(F_SANS, 16), 984, (200, 205, 215))

    img.save("entry.png", "PNG", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
