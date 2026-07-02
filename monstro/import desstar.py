import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Load your transparent graphic (Ensure it has an alpha channel / transparent background)
# If you don't have one yet, comment out lines 11-13 and the overlay logic inside the loop.
overlay_img = cv2.imread('butterfly.png', cv2.IMREAD_UNCHANGED)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # 1. ADD TEXT OVERLAYS (Y2K / Web Booth Style)
    # cv2.putText(image, text, position, font, scale, color(BGR), thickness)
    cv2.putText(frame, "yurinium ZURIII YUrI", (50, 80), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (180, 105, 255), 2, cv2.LINE_AA)
    
    cv2.putText(frame, "@GgHooouuuulss.mp3", (w - 220, 50), 
                cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.7, (255, 180, 200), 1, cv2.LINE_AA)

    # 2. OVERLAY TRANSPARENT PNG GRAPHIC
    if overlay_img is not None:
        # Resize overlay if it's too big
        overlay_res = cv2.resize(overlay_img, (100, 100))
        ol_h, ol_w, ol_c = overlay_res.shape

        # Set position coordinates (e.g., top right corner)
        y, x = 120, w - 150

        # Separate the color channels and the alpha (transparency) mask
        overlay_color = overlay_res[:, :, :3]
        alpha_mask = overlay_res[:, :, 3] / 255.0

        # Blend the graphic onto the camera frame
        for c in range(0, 3):
            frame[y:y+ol_h, x:x+ol_w, c] = (
                alpha_mask * overlay_color[:, :, c] + 
                (1.0 - alpha_mask) * frame[y:y+ol_h, x:x+ol_w, c]
            )

    # 3. DRAW A MINIMALIST UI BORDER/BOX
    cv2.rectangle(frame, (20, 20), (w - 20, h - 20), (255, 230, 240), 2)

    cv2.imshow("Nashallery's Vibe Booth", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()