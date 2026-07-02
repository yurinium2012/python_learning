import cv2
import numpy as np
import time
import mediapipe as mp
from PIL import Image, ImageDraw, ImageFont

# Initialize stable MediaPipe modules
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

mp_face = mp.solutions.face_detection
face_detection = mp_face.FaceDetection(
    min_detection_confidence=0.5
)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Load Fonts safely
font_dir = "C:\\Windows\\Fonts\\"
try:
    font_main = ImageFont.truetype(font_dir + "comic.ttf", 46)
    font_finger = ImageFont.truetype(font_dir + "cour.ttf", 20)  # Clean Courier style
    font_heavy = ImageFont.truetype(font_dir + "impact.ttf", 36)
    font_mono = ImageFont.truetype(font_dir + "cour.ttf", 26)
    font_serif = ImageFont.truetype(font_dir + "georgia.ttf", 26) 
except IOError:
    font_main = font_finger = font_heavy = font_mono = font_serif = ImageFont.load_default()

window_name = "Nashallery's Vibe Booth"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

# Color Space (RGB for PIL)
PINK = (255, 105, 180)
CYAN = (0, 240, 255)
LAVENDER = (210, 180, 255)
LIME = (170, 255, 120)
SHADOW = (40, 20, 40)
WHITE = (255, 255, 255)

FINGER_TIPS = {
    "THUMB": 4,
    "INDEX": 8,
    "MIDDLE": 12,
    "RING": 16,
    "PINKY": 20
}

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
    
    hand_results = hands.process(rgb_frame)
    face_results = face_detection.process(rgb_frame)
    
    pil_im = Image.fromarray(rgb_frame)
    draw = ImageDraw.Draw(pil_im)

    # --- 1. CORE BACKGROUND UI ELEMENTS ---
    draw.rectangle([25, 25, w - 25, h - 25], outline=PINK, width=2)
    draw.rectangle([32, 32, w - 32, h - 32], outline=CYAN, width=1)
    
    for x_grid in range(50, 220, 30):
        for y_grid in range(160, 280, 30):
            draw.text((x_grid, y_grid), ".", font=font_mono, fill=LAVENDER)

    # --- 2. MULTI-FINGER TRACKING ---
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            for idx, (name, lm_id) in enumerate(FINGER_TIPS.items()):
                landmark = hand_landmarks.landmark[lm_id]
                fx = int(landmark.x * w)
                fy = int(landmark.y * h)
                
                draw_retro_sparkle(draw, fx, fy, 12, WHITE, CYAN)
                
                text_color = PINK if idx % 2 == 0 else LIME
                
                # Removed stroke processing to eliminate the Pillow crash
                draw.text(
                    (fx + 18, fy - 15), 
                    f"// {name}", 
                    font=font_finger, 
                    fill=text_color
                )

    # --- 3. FOREHEAD SNIPER RETICLE ---
    if face_results.detections:
        for detection in face_results.detections:
            if detection.location_data.relative_keypoints:
                forehead_point = detection.location_data.relative_keypoints[2]
                th_x = int(forehead_point.x * w)
                th_y = int(forehead_point.y * h) - 25 
                
                r_target = 22
                draw.ellipse([th_x - r_target, th_y - r_target, th_x + r_target, th_y + r_target], outline=LIME, width=2)
                draw.ellipse([th_x - 4, th_y - 4, th_x + 4, th_y + 4], fill=PINK)
                
                draw.line([(th_x - 35, th_y), (th_x - 10, th_y)], fill=LIME, width=1)
                draw.line([(th_x + 10, th_y), (th_x + 35, th_y)], fill=LIME, width=1)
                draw.line([(th_x, th_y - 35), (th_x, th_y - 10)], fill=LIME, width=1)
                draw.line([(th_x, th_y + 10), (th_x, th_y + 35)], fill=LIME, width=1)
                
                # Removed stroke processing
                draw.text(
                    (th_x + 40, th_y - 16), 
                    "[ YURI ]", 
                    font=font_serif, 
                    fill=WHITE
                )

    # --- 4. DECORATIVE CELESTIAL ENVIRONMENT ---
    for i in range(1, 35):
        sx = (i * 37) % (w - 100) + 50
        sy = (i * 53) % (h - 150) + 60
        if not (sx < 500 and sy > h - 220):
            draw.text((sx, sy), "*", font=font_mono, fill=WHITE)

    # Text Overlays (Strokes dropped to prevent getmask2 errors)
    draw.text((60, h - 165), "You,re always my // REMINDER", font=font_mono, fill=(255, 255, 0))
    draw.text((63, h - 117), "yurinium ZURIII YUrI", font=font_main, fill=SHADOW)
    draw.text((60, h - 120), "yurinium ZURIII YUrI", font=font_main, fill=PINK)
    
    current_time = time.strftime("%H:%M:%S")
    draw.text((w - 280, 50), f"SYS_TIME: {current_time}", font=font_mono, fill=LIME)
    draw.text((w // 2 - 180, 45), "[ * + . V I B E . + * ]", font=font_mono, fill=LAVENDER)

    frame = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
    cv2.imshow(window_name, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()