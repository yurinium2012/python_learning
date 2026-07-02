import cv2

# Using DirectShow backend (cv2.CAP_DSHOW) fixes the MSMF grab frame errors on Windows
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

print("Controls:")
print("  Press 's' to toggle between Stylized and Clean view.")
print("  Press 'q' to exit.")

# Toggle state: True for comic/grainy, False for normal
stylized_mode = True 

while True:
    ret, frame = cap.read()
    if not ret:
        # If a single frame drops, continue instead of crashing the program
        continue

    # Fix the inversion (1 flips horizontally, mirroring it correctly)
    frame = cv2.flip(frame, 1)

    if stylized_mode:
        # To make it less violently grainy, we apply a slight blur first
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Adaptive threshold on the blurred image for cleaner high-contrast lines
        display_frame = cv2.adaptiveThreshold(
            blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
        )
    else:
        # Standard, clean color feed
        display_frame = frame

    cv2.imshow('Camera Feed', display_frame)

    key = cv2.waitKey(1) & 0xFF
    
    # Toggle mode with 's'
    if key == ord('s'):
        stylized_mode = not stylized_mode
        print(f"Mode changed. Stylized: {stylized_mode}")
        
    # Exit with 'q'
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()