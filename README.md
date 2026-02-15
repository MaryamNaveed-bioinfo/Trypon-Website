Trypon-Website

[Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
[License](https://img.shields.io/badge/License-MIT-green)

 Table of Contents
1. project-overview
2. Features
3. Folder Structure
4. Installation
5. Usage
6. Sample Output
7. Libraries Used
8. License

 Project Overview
Trypon-Website is a Python project that captures a user's photo, detects body landmarks using MediaPipe, and calculates body measurements. This project demonstrates:

- Python coding skills  
- Working with OpenCV and MediaPipe libraries  
- Saving structured data as JSON  

It’s a great starter project for your portfolio or learning pose detection workflows.

Features
- Capture a photo from the camera (`capture_photo.py`)  
- Detect body landmarks (`detect_pose.py`)  
- Calculate user measurements and save to JSON (`measure_user.py`)  
- Sample output provided (`user_measurements.json`)  

Folder Structure

Trypon-Website

-capture_photo.py       # Captures photo from camera
-detect_pose.py         # Detects body landmarks using MediaPipe
-measure_user.py        # Calculates measurements & saves JSON
-user_measurements.json # Sample output
-README.md              # This file
-requirements.txt       # Python dependencies

Installation

1. Clone the repository:

bash
git clone https://github.com/MaryamNaveed-bioinfo/Trypon-Website.git
cd Trypon-Website

2. Install dependencies:

bash
pip install -r requirements.txt

 Usage

1. Run `capture_photo.py` to take a photo:

bash
python capture_photo.py

2. Run `detect_pose.py` to detect body landmarks:

bash
python detect_pose.py

3. Run `measure_user.py` to calculate measurements and save them to JSON:

bash
python measure_user.py

 Sample Output

The measurements will be saved in `user_measurements.json`. Example:

json
{
  "height": 170,
  "arm_length": 60,
  "leg_length": 80
}

 Libraries Used

[OpenCV](https://opencv.org/) – For capturing and handling images
[MediaPipe](https://mediapipe.dev/) – For pose detection
JSON – For storing measurement data

 License

This project is open-source and available under the MIT License.

What’s improved in this version:

- Badges for Python version & license  
- Table of contents with clickable links  
- Clear headers and sections  
- Markdown formatting that GitHub renders professionally  



