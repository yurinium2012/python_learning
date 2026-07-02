import cv2
import numpy as np
import time
from PIL import Image, ImageDraw, ImageFont

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Explicit hardware widescreen resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# --- LOAD A VARIETY OF WINDOWS SYSTEM FONTS ---
font_dir = "C:\\Windows\\Fonts\\"
try:
    font_main = ImageFont.truetype(font_dir + "comic.ttf", 46)
    font_heavy = ImageFont.truetype(font_dir + "impact.ttf", 36)
    font_mono = ImageFont.truetype(font_dir + "cour.ttf", 20)
    font_serif = ImageFont.truetype(font_dir + "georgia.ttf", 24)
except IOError:
    # Safe structural fallbacks if your Windows paths differ
    font_main = font_heavy = font_mono = font_serif = ImageFont.load_default()

window_name = "Nashallery's Vibe Booth"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

# Color Palette Variables (RGB for PIL)
PINK = (255, 105, 180)
CYAN = (0, 240, 255)
LAVENDER = (210, 180, 255)
LIME = (170, 255, 120)
SHADOW = (40, 20, 40)
WHITE = (255, 255, 255)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    
    # Process matrix conversions
    cv2_im_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im_rgb)
    draw = ImageDraw.Draw(pil_im)

    w, h = pil_im.size

    # --- 1. DETAILED INTERFACE ART & CORNER GRAPHICS ---
    # Double Outer Neon Frame
    draw.rectangle([25, 25, w - 25, h - 25], outline=PINK, width=2)
    draw.rectangle([32, 32, w - 32, h - 32], outline=CYAN, width=1)

    # Tech Crosshairs in Corners
    def draw_bracket(d, x, y, size_x, size_y, color):
        d.line([(x, y), (x + size_x, y)], fill=color, width=2)
        d.line([(x, y), (x, y + size_y)], fill=color, width=2)

    # Top-Left tech bracket
    draw_bracket(draw, 45, 45, 30, 30, LIME)
    # Bottom-Right tech bracket
    draw_bracket(draw, w - 45, h - 45, -30, -30, LIME)

    # Decorative Dotted Grid on the Side
    for x_grid in range(50, 180, 20):
        for y_grid in range(160, 240, 20):
            draw.rectangle([x_grid, y_grid, x_grid+2, y_grid+2], fill=LAVENDER)

    # --- 2. LAYERED TEXT WITH MIXED STYLES AND COLORS ---
    # Headline text using main font (Bottom Left)
    draw.text((63, h - 117), "yurinium ZURIII YUrI", font=font_main, fill=SHADOW)
    draw.text((60, h - 120), "yurinium ZURIII YUrI", font=font_main, fill=PINK)

    # Subtext subtitle using Impact serif combo (Just above main heading)
    draw.text((90, h - 165), "You,re always my // REMINDER", font=font_mono, font_mono = ImageFont.truetype(font_dir + "cour.ttf", 32), fill=(255, 255, 0),stroke_width=1, stroke_fill=(0, 0, 0))

    # Top Right Handle / Credits using clean monospace text
    current_time = time.strftime("%H:%M:%S")
    draw.text((w - 280, 50), f"SYS_TIME: {current_time}", font=font_mono, fill=LIME)
    draw.text((w - 280, 80), "@Ghouls and Gals", font=font_serif, fill=LAVENDER)

    # Center-left status label using Georgia serif
    draw.text((60, 70), "Mode: Widescreen Vibe", font=font_serif, fill=WHITE)

    # --- 3. ADVANCED Y2K PROCEDURAL SPARKLE DRAWINGS ---
    def draw_retro_sparkle(d, cx, cy, size, core_color, accent_color):
        # Vertical / Horizontal spikes
        d.line([(cx - size, cy), (cx + size, cy)], fill=accent_color, width=2)
        d.line([(cx, cy - size), (cx, cy + size)], fill=accent_color, width=2)
        # Inner diamond/circle center
        d.polygon([(cx, cy - 3), (cx + 3, cy), (cx, cy + 3), (cx - 3, cy)], fill=core_color)

    # Scattering distinct sparkle designs across the frames
    draw_retro_sparkle(draw, 90, 130, 15, WHITE, PINK)
    draw_retro_sparkle(draw, 220, 85, 10, WHITE, CYAN)
    draw_retro_sparkle(draw, w - 120, 140, 12, LIME, LAVENDER)
    draw_retro_sparkle(draw, w - 80, h - 140, 18, WHITE, PINK)

# Additional Web-Deco Ornaments & ASCII Clusters
    # 1. Monospace ASCII cluster near the top center
    draw.text((w // 2 - 50, 50), "[ *++ . WHEN YOURE ALONE . ++* ]", font=font_mono, fill=(210, 180, 255), font_mono = ImageFont.truetype(font_dir + "cour.ttf", 28))
    
    # 2. Scattered micro-stars (Tiny 2x2 pixels) for digital noise

    star_positions = [(150, 100), (300, 600), (w - 200, h - 200), (w - 400, 80), (120, h - 300)]
    for pos in star_positions:
        draw.rectangle([pos[0], pos[1], pos[0] + 3, pos[1] + 3], fill=(255, 255, 255))
        
        
    # 3. Extra mini neon sparkles
    draw_retro_sparkle(draw, 450, h - 130, 8, (255, 255, 255), (170, 255, 120))
    draw_retro_sparkle(draw, w - 180, 250, 7, (255, 255, 255), (255, 105, 180))
    draw_retro_sparkle(draw, 450, h - 130, 8, (255, 255, 255), (170, 255, 120))
    draw_retro_sparkle(draw, w - 180, 250, 7, (255, 255, 255), (255, 105, 180))
    draw_retro_sparkle(draw, 450, h - 130, 8, (255, 255, 255), (170, 255, 120))
    draw_retro_sparkle(draw, w - 180, 250, 7, (255, 255, 255), (255, 105, 180))
    draw_retro_sparkle(draw, 450, h - 130, 8, (255, 255, 255), (170, 255, 120))
    draw_retro_sparkle(draw, w - 180, 250, 7, (255, 255, 255), (255, 105, 180))
# --- EXPANDED STARS & SPARKLES ---
    # Massive field of micro-stars (3x3 pixels) for a dense digital sky effect
    dense_stars = [
        (120, 100), (160, 220), (280, 85), (340, 190), 
        (90, 450), (150, 600), (240, 520), (1150, 110), 
        (1020, 200), (1110, 280), (1200, 400), (1050, 550), 
        (1180, 620), (950, 650), (450, 80), (750, 60)
    ]
    for pos in dense_stars:
        draw.rectangle([pos[0], pos[1], pos[0] + 3, pos[1] + 3], fill=(255, 255, 255))

    # Additional large procedural sparkles scattered around the margins
    draw_retro_sparkle(draw, 140, 290, 10, WHITE, CYAN)
    draw_retro_sparkle(draw, 200, 420, 12, WHITE, LAVENDER)
    draw_retro_sparkle(draw, w - 250, 180, 14, LIME, PINK)
    draw_retro_sparkle(draw, w - 160, 480, 9, WHITE, CYAN)
    draw_retro_sparkle(draw, w // 2 + 150, h - 120, 11, WHITE, LIME)
    draw_retro_sparkle(draw, 90, 130, 18, WHITE, PINK)
    draw_retro_sparkle(draw, 250, 95, 14, WHITE, CYAN)
    draw_retro_sparkle(draw, 400, 150, 12, LIME, WHITE)
    draw_retro_sparkle(draw, w - 140, 160, 16, LIME, LAVENDER)
    draw_retro_sparkle(draw, w - 220, 300, 12, WHITE, PINK)
    draw_retro_sparkle(draw, w - 90, h - 160, 22, WHITE, PINK)
    draw_retro_sparkle(draw, w // 2 + 200, h - 130, 15, CYAN, LIME)


    # Convert back to native OpenCV display format
    frame = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
    cv2.imshow(window_name, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()