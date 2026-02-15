import cv2
import mediapipe as mp

# Load image
image = cv2.imread("captured_photo.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Initialize MediaPipe pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)

# Process image
results = pose.process(image_rgb)

# Draw landmarks and extract coordinates
if results.pose_landmarks:
    mp_drawing = mp.solutions.drawing_utils
    annotated_image = image.copy()
    mp_drawing.draw_landmarks(
        annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Save annotated image
    cv2.imwrite("annotated_pose.jpg", annotated_image)

    # Get landmarks
    landmarks = results.pose_landmarks.landmark

    # Helper function to get pixel coordinates
    def get_pixel_coords(landmark):
        h, w, _ = image.shape
        return int(landmark.x * w), int(landmark.y * h)

    # Print key body parts
    print("\n🧍 Body Landmark Coordinates:")
    body_parts = {
        "LEFT_SHOULDER": mp_pose.PoseLandmark.LEFT_SHOULDER,
        "RIGHT_SHOULDER": mp_pose.PoseLandmark.RIGHT_SHOULDER,
        "LEFT_HIP": mp_pose.PoseLandmark.LEFT_HIP,
        "RIGHT_HIP": mp_pose.PoseLandmark.RIGHT_HIP,
        "LEFT_KNEE": mp_pose.PoseLandmark.LEFT_KNEE,
        "RIGHT_KNEE": mp_pose.PoseLandmark.RIGHT_KNEE,
        "LEFT_ANKLE": mp_pose.PoseLandmark.LEFT_ANKLE,
        "RIGHT_ANKLE": mp_pose.PoseLandmark.RIGHT_ANKLE,
    }

    coords = {}
    for name, index in body_parts.items():
        coords[name] = get_pixel_coords(landmarks[index])
        print(f"{name}: {coords[name]}")

    # Example: Calculate shoulder width
    left_shoulder = coords["LEFT_SHOULDER"]
    right_shoulder = coords["RIGHT_SHOULDER"]
    shoulder_width = abs(left_shoulder[0] - right_shoulder[0])
    print(f"\n📏 Estimated Shoulder Width (in pixels): {shoulder_width}")

else:
    print("❌ No pose landmarks detected.")
