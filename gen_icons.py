from PIL import Image, ImageDraw, ImageFont
import os

for size in [192, 512]:
    img = Image.new('RGB', (size, size), '#0f1117')
    draw = ImageDraw.Draw(img)
    # Circle background
    margin = size // 8
    draw.ellipse([margin, margin, size-margin, size-margin], fill='#2563eb')
    # Simple dumbbell shape
    cx, cy = size//2, size//2
    r = size // 6
    bar_w = int(size * 0.35)
    bar_h = size // 14
    draw.ellipse([cx - bar_w - r, cy - r, cx - bar_w + r, cy + r], fill='white')
    draw.ellipse([cx + bar_w - r, cy - r, cx + bar_w + r, cy + r], fill='white')
    draw.rectangle([cx - bar_w, cy - bar_h, cx + bar_w, cy + bar_h], fill='white')
    img.save(f'icon-{size}.png')
    print(f'icon-{size}.png created')
