import cv2
import mediapipe as mp
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# ... (Keep your existing MediaPipe, font, and particle initialization code here) ...
cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    
    # 1. MediaPipe hand detection (uses RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # --- PARTICLE LOGIC ---
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            cx = int((hand_landmarks.landmark[0].x + hand_landmarks.landmark[9].x) / 2 * w)
            cy = int((hand_landmarks.landmark[0].y + hand_landmarks.landmark[9].y) / 2 * h)
            for _ in range(2):
                spawn_particle(cx, cy)

    # --- THE PIL CONVERSION FIX ---
    # 2. Convert the current OpenCV frame to a PIL Image so 'draw.text' works
    pil_img = Image.fromarray(rgb_frame) 
    draw = ImageDraw.Draw(pil_img)

    # 3. Draw your static text (Line 139 from your error)
    draw.text((60, h - 120), "yurinium ZURIII YUrI", font=font_main, fill=PINK)

    # 4. Draw your moving particles using PIL
    active_particles = []
    for p in particles:
        p["x"] += p["vx"]
        p["y"] += p["vy"]
        p["life"] -= 1
        p["vx"] += random.uniform(-0.2, 0.2)

        if p["life"] > 0:
            # Using PIL's draw.text instead of cv2.putText
            draw.text((int(p["x"]), int(p["y"])), p["text"], font=font_particles, fill=p["color"])
            active_particles.append(p)
            
    particles = active_particles

    # 5. Convert back to OpenCV format (BGR) so it can actually display
    frame = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

    # 6. Display the converted frame
    cv2.imshow("Worm Song Filter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()