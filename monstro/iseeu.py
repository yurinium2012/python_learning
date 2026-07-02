import cv2
import numpy as np
import time
import mediapipe as mp
from PIL import Image, ImageDraw, ImageFont

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Load Fonts safely
font_dir = "C:\\Windows\\Fonts\\"
try:
    font_main = ImageFont.truetype(font_dir + "comic.ttf", 46)
    font_heavy = ImageFont.truetype(font_dir + "impact.ttf", 36)
    font_mono = ImageFont.truetype(font_dir + "cour.ttf", 28)
    font_serif = ImageFont.truetype(font_dir + "georgia.ttf", 24)
except IOError:
    font_main = font_heavy = font_mono = font_serif = ImageFont.load_default()

window_name = "Nashallery's Interactive Booth"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

PINK = (255, 105, 180)
CYAN = (0, 240, 255)
LAVENDER = (210, 180, 255)
LIME = (170, 255, 120)
SHADOW = (40, 20, 40)
WHITE = (255, 255, 255)

# Interactive asset state
obj_x, obj_y = 640, 360
obj_radius = 50
is_dragging = False

def draw_retro_sparkle(d, cx, cy, size, core_color, accent_color):
    d.line([(cx - size, cy), (cx + size, cy)], fill=accent_color, width=2)
    d.line([(cx, cy - size), (cx, cy + size)], fill=accent_color, width=2)
    d.polygon([(cx, cy - 3), (cx + 3, cy), (cx, cy + 3), (cx - 3, cy)], fill=core_color)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    finger_x, finger_y = None, None
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            index_tip = hand_landmarks.landmark[8]
            finger_x = int(index_tip.x * w)
            finger_y = int(index_tip.y * h)

            # Bounding check for dragging mechanics
            distance = np.sqrt((finger_x - obj_x)**2 + (finger_y - obj_y)**2)
            if distance < obj_radius:
                is_dragging = True
            
            if is_dragging:
                obj_x, obj_y = finger_x, finger_y
    else:
        is_dragging = False

    pil_im = Image.fromarray(rgb_frame)
    draw = ImageDraw.Draw(pil_im)

    # Outer Frames
    draw.rectangle([25, 25, w - 25, h - 25], outline=PINK, width=2)
    draw.rectangle([32, 32, w - 32, h - 32], outline=CYAN, width=1)
    
    # Upper left dot grid matrix (Enlarged)
    for x_grid in range(50, 220, 30):
        for y_grid in range(160, 280, 30):
            draw.text((x_grid, y_grid), ".", font=font_mono, fill=LAVENDER)

    # Interactive Drag Target
    object_color = LIME if is_dragging else CYAN
    draw.ellipse([obj_x - 20, obj_y - 20, obj_x + 20, obj_y + 20], outline=object_color, width=2)
    draw_retro_sparkle(draw, obj_x, obj_y, 35, WHITE, object_color)
    draw.text((obj_x + 45, obj_y - 15), "<= DRAG ME", font=font_mono, fill=object_color)

    # Procedural Celestial Starfield
    for i in range(1, 45):
        sx = (i * 37) % (w - 100) + 50
        sy = (i * 53) % (h - 150) + 60
        # Protect readability zones from star overlap
        if not (sx < 500 and sy > h - 220) and np.sqrt((sx - obj_x)**2 + (sy - obj_y)**2) > 70:
            char = "+" if i % 3 == 0 else "*"
            draw.text((sx, sy), char, font=font_mono, fill=WHITE)

    # Static Sparkle Clusters
    draw_retro_sparkle(draw, 90, 130, 18, WHITE, PINK)
    draw_retro_sparkle(draw, w - 140, 160, 16, LIME, LAVENDER)
    draw_retro_sparkle(draw, w - 90, h - 160, 22, WHITE, PINK)

    # Yellow Typewriter line with precise black stroke parameters
    draw.text(
        (60, h - 165), 
        "You,re always my // REMINDER", 
        font=font_mono, 
        fill=(255, 255, 0), 
        stroke_width=2, 
        stroke_fill=(0, 0, 0)
    )

    # Text Overlays
    draw.text((63, h - 117), "yurinium ZURIII YUrI", font=font_main, fill=SHADOW)
    draw.text((60, h - 120), "yurinium ZURIII YUrI", font=font_main, fill=PINK)
    
    current_time = time.strftime("%H:%M:%S")
    draw.text((w - 280, 50), f"SYS_TIME: {current_time}", font=font_mono, fill=LIME)
    draw.text((w // 2 - 180, 45), "[ * + . V I B E . + * ]", font=font_mono, fill=LAVENDER)

    # Render back to OpenCV window context
    frame = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
    cv2.imshow(window_name, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()