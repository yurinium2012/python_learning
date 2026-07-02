import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# --- SET HIGH RESOLUTION HERE ---
# 1280x720 is ideal for most webcams. If yours supports Full HD, you can try 1920 and 1080.
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# --------------------------------

# Load fonts
try:
    font_path = "C:\\Windows\\Fonts\\comic.ttf" 
    font_large = ImageFont.truetype(font_path, 42)  # Slightly bigger for high res
    font_small = ImageFont.truetype(font_path, 22)
except IOError:
    font_large = ImageFont.load_default()
    font_small = ImageFont.load_default()

# Define window parameters cleanly
window_name = "Nashallery's Vibe Booth"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    
    # Convert OpenCV BGR frame to PIL Image
    cv2_im_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im_rgb)
    draw = ImageDraw.Draw(pil_im)

    w, h = pil_im.size

    # DRAW TEXT WITH RESPECT TO TARGET HIGH-RES DIMENSIONS
    # Drop shadow
    draw.text((62, h - 108), "yurinium ZURIII YUrI", font=font_large, fill=(50, 0, 50))
    # Main text (Pink/Magenta moved elegantly to bottom-left corner like the reference)
    draw.text((60, h - 110), "yurinium ZURIII YUrI", font=font_large, fill=(255, 105, 180))
    
    # Top right handle relative to current width
    draw.text((w - 260, 50), "@zaza lover", font=font_small, fill=(200, 200, 255))

    # Y2K Sparkle Crosses
    def draw_sparkle(d, cx, cy, size, color):
        d.line([(cx - size, cy), (cx + size, cy)], fill=color, width=2)
        d.line([(cx, cy - size), (cx, cy + size)], fill=color, width=2)
        d.ellipse([cx - 2, cy - 2, cx + 2, cy + 2], fill=(255, 255, 255))

    # Scattered cleanly around the dynamic frame limits
    draw_sparkle(draw, 80, 140, 12, (255, 180, 230))
    draw_sparkle(draw, w - 120, 140, 10, (180, 220, 255))
    draw_sparkle(draw, w - 80, h - 140, 14, (255, 255, 150))
    
    # SYSTEM BORDERS
    draw.rectangle([30, 30, w - 30, h - 30], outline=(255, 230, 240), width=2)
    draw.rectangle([36, 36, w - 36, h - 36], outline=(255, 105, 180), width=1)

    # Convert back to OpenCV format to display
    frame = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

    cv2.imshow(window_name, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()