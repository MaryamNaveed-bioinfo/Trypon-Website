import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Cannot open camera")
    exit()

print("📸 Press 's' to capture the photo and save it")
while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    cv2.imshow('Camera Feed - Press s to Save', frame)

    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite('captured_photo.jpg', frame)
        print("✅ Image saved as captured_photo.jpg")
        break
    elif key == ord('q'):
        print("❌ Quit without saving")
        break

cap.release()
cv2.destroyAllWindows()
s
