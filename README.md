# ✋ Hand Gesture Recognition System (SkillCraft Internship – Task 4)

This project implements a **real-time Hand Gesture Recognition System** using Python, OpenCV, and Machine Learning.  
It was developed as **Task 4** during my internship at **SkillCraft Technology**.

The system captures hand gestures through a webcam, creates a manual dataset, trains a Machine Learning model, and predicts gestures live.

---

## 🚀 Features

- Real-time gesture detection using webcam
- Manual dataset creation
- Machine Learning model training (SVM)
- Live gesture prediction
- Beginner-friendly implementation
- No deep learning (simple ML approach)

---

## 🛠 Technologies Used

- Python  
- OpenCV  
- NumPy  
- Scikit-learn  
- Joblib  

---

hand_gesture_recognition/
│
├── dataset/
│ ├── palm/
│ ├── fist/
│ └── thumbs/
│
├── model/
│ └── gesture_model.pkl
│
├── collect_data.py
├── train_model.py
├── predict.py
└── README.md

---

## ⚙️ Installation

### 1. Clone the repository

git clone <your-github-repo-link>
cd hand_gesture_recognition

---

### 2. Install dependencies

pip install opencv-python numpy scikit-learn joblib

---

## ▶️ How to Run

### Step 1 – Collect Dataset

Run:

python collect_data.py

Enter gesture names when prompted:
palm
fist
thumbs

(Each gesture is captured using webcam.)

---

### Step 2 – Train Model

python train_model.py

Output:

Model trained successfully

---

### Step 3 – Predict Gestures Live

python predict.py

Webcam opens and predicted gesture is displayed on screen.

Press **ESC** to exit.

---

## 🧠 Working Principle

1. Webcam captures hand image.
2. OpenCV extracts contour features (area & count).
3. Features are saved as dataset.
4. SVM classifier is trained on collected data.
5. Model predicts gestures in real-time.

---

## 🎓 Internship Description

This project demonstrates practical implementation of Machine Learning for real-time computer vision applications.  
Manual dataset creation and ML logic were developed as part of SkillCraft Technology Internship Task 4.

---

## 👩‍💻 Author

**Manvitha**

SkillCraft Technology Intern  
Computer Science Student  

---

## ⭐ Acknowledgment

Thanks to **SkillCraft Technology** for providing this learning opportunity.

---

## 📌 Note

This project is built for educational and internship purposes.

---

⭐ If you like this project, feel free to star the repository!

## 📁 Project Structure

