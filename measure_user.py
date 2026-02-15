import cv2
import mediapipe as mp
import json
import math

# Load the captured image
image_path = "captured_photo.jpg"
image = cv2.imread(image_path)
if image is None:
    print(" Image not found. Make sure 'captured_photo.jpg' exists.")
    exit()
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Initialize MediaPipe pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, model_complexity=2)
results = pose.process(image_rgb)

# Check if landmarks were detected
if not results.pose_landmarks:
    print(" No pose landmarks detected.")
    exit()

# Get landmark coordinates
landmarks = results.pose_landmarks.landmark
h, w, _ = image.shape


def get_landmark_coords(part_name):
    part = mp_pose.PoseLandmark[part_name]
    lm = landmarks[part]
    return int(lm.x * w), int(lm.y * h)


def calculate_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


# 1. Shoulder width
left_shoulder = get_landmark_coords("LEFT_SHOULDER")
right_shoulder = get_landmark_coords("RIGHT_SHOULDER")
shoulder_width_px = calculate_distance(left_shoulder, right_shoulder)

# 2. Hip width (optional)
left_hip = get_landmark_coords("LEFT_HIP")
right_hip = get_landmark_coords("RIGHT_HIP")
hip_width_px = calculate_distance(left_hip, right_hip)

# Set scale (Pixels per cm) — assuming A4 paper (29.7 cm tall = 300px approx)
pixels_per_cm = 300 / 29.7

# Convert to centimeters
shoulder_width_cm = shoulder_width_px / pixels_per_cm
hip_width_cm = hip_width_px / pixels_per_cm

# Save to JSON file
measurements = {
    "shoulder_width_cm": round(shoulder_width_cm, 2),
    "hip_width_cm": round(hip_width_cm, 2),
    "pixel_scale": round(pixels_per_cm, 2)
}

with open("user_measurements.json", "w") as f:
    json.dump(measurements, f, indent=2)

print("Measurements saved to 'user_measurements.json':")
print(json.dumps(measurements, indent=2))
