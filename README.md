# 🕺 Pose Detection to Animation Data Export

A real-time pose tracking system that extracts full-body landmark coordinates from a video file and saves them into a text file for animation or game engine use.

This project:
- Reads a video file
- Detects full body pose landmarks
- Extracts landmark positions
- Converts coordinates to screen space
- Stores frame-by-frame data
- Exports animation data to a text file

---

## 👨‍💻 Author

Sheshehang Limbu (HunterVinic)

---

## 🚀 Features

- 🎥 Video-based pose detection
- 🧍 Full body landmark tracking
- 📦 Frame-by-frame data capture
- 📝 Export to animation text file
- 🎮 Ready for Unity / Blender / Game engines
- ⚡ Lightweight and simple pipeline

---

## 🛠 Tech Stack

- Python 3.x
- OpenCV
- CVZone
- MediaPipe Pose

---

## 📂 Project Structure

.
├── pose_export.py
├── Video.mp4
├── AnimationFile.txt
├── requirements.txt
└── README.md

---

## 📦 Installation

1️⃣ Create virtual environment:

python -m venv venv
source venv/bin/activate

2️⃣ Install dependencies:

pip install opencv-python
pip install cvzone
pip install mediapipe

Or use:

pip install -r requirements.txt

---

## ▶️ Run the Project

python pose_export.py

Controls:
- Press **s** → Save animation data to AnimationFile.txt
- Close window to exit

---

## 📡 How It Works

1. Load video file (Video.mp4)
2. Detect body pose using MediaPipe via CVZone
3. Extract landmark list
4. Convert coordinates:
   - X remains same
   - Y inverted (screen coordinate correction)
5. Store as string format per frame
6. Append to list
7. On pressing **s**, export all frames to:

AnimationFile.txt

---

## 📊 Data Format

Each line in AnimationFile.txt represents one frame.

Format:

x1,y1,z1,x2,y2,z2,x3,y3,z3,...x33,y33,z33,

MediaPipe Pose detects:
33 body landmarks per frame

So each frame contains:
99 values (33 × 3)

---

## 🎮 Use Cases

- Unity animation retargeting
- Blender motion replication
- Game character animation
- Motion capture prototype
- AI movement analysis
- Sports biomechanics research

---

## ⚠️ Notes

- Ensure Video.mp4 exists in project directory
- Works best with clear human subjects
- Good lighting improves detection
- Frame rate depends on video resolution
- Press 's' only after enough frames are captured

---

## 📈 Future Improvements

- Export as JSON instead of TXT
- Add CSV export option
- Normalize coordinates (0–1 range)
- Add smoothing filter
- Add real-time webcam version
- Add UDP streaming (like your hand tracking project)
- Convert to WebSocket streaming
- Build Unity receiver script

---

## 🔒 Technical Details

Landmark extraction:

for lm in lmList:
    lmString += f'{lm[1]},{img.shape[0] - lm[2]},{lm[3]},'

- lm[1] → X coordinate
- img.shape[0] - lm[2] → Y inverted
- lm[3] → Z depth

---

## 🏆 Project Type

Computer Vision + Motion Capture + Animation Data Export  

Suitable for:
- Game development
- AR/VR
- Motion capture systems
- AI research
- Portfolio demonstrations

---

## 📜 License

Copyright (c) 2026 Sheshehang Limbu

All rights reserved.

This project may not be copied, modified, or distributed
without explicit permission from the author.
