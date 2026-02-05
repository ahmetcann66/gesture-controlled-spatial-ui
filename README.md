# 🖐️ Gesture Controlled Spatial UI (Tony Stark Style)

> **Project Description:** This project is a real-time **Spatial User Interface** developed using Python, OpenCV, and MediaPipe. It allows users to create, manipulate, and delete virtual objects using hand gestures. **The system features a built-in Physics Engine, allowing objects to react to gravity, bounce off the floor, and interact with user inputs dynamically.**

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=flat&logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange?style=flat&logo=google)

## 🛠️ Tech Stack

| Technology | Version | Description |
| :--- | :--- | :--- |
| **Python** | 3.11.x | Core programming language (Selected for MediaPipe compatibility). |
| **OpenCV** | 4.x | Image processing, camera feed management, and rendering. |
| **MediaPipe** | 0.10.9 | ML pipeline for real-time 21-point hand landmark detection. |
| **NumPy** | 1.x | Vector math operations. |

---

## 🎮 Gestures & Controls

| Gesture | Visual Guide | Function |
| :--- | :--- | :--- |
| **👆 Index Finger** | Index finger up. | **Cursor / Hover:** Selects menu items or targets objects. |
| **👌 Pinch** | Thumb & Index finger touching. | **Grab & Drag:** Moves the selected object and **pauses physics** for that object. |
| **✌️ Victory (V-Sign)** | Index & Middle fingers up. | **Create:** Spawns the selected shape (Square/Circle) which immediately **reacts to gravity**. |
| **✊ Fist** | All fingers closed. | **Delete (Undo):** Triggers a "Hold-to-Confirm" bar. Deletes the last object when filled. |

---

## 📂 Project Architecture

The project follows a modular **Object-Oriented Programming (OOP)** structure:

* `main.py` - **Controller:** Manages the main loop, camera feed, and state machine.
* `HandTrackingModule.py` - **Sensor:** Wraps MediaPipe functionality to detect hands and gestures.
* `ObjectManager.py` - **Model:** Manages the state, **physics calculations (gravity, velocity, collision)**, and rendering.

---

## 🚀 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/ahmetcann66/gesture-controlled-spatial-ui.git](https://github.com/ahmetcann66/gesture-controlled-spatial-ui.git)
    cd gesture-controlled-spatial-ui
    ```

2.  **Install Dependencies**
    Ensure you are using Python 3.11.
    ```bash
    pip install opencv-python mediapipe numpy
    ```

3.  **Run the Project**
    Double-click `baslat.bat` or run via terminal:
    ```bash
    python main.py
    ```

---

## 🔮 Future Improvements
* [x] Physics Engine (Gravity & Bounce) ✅
* [ ] Color Picker Menu (RGB Selection)
* [ ] Save/Load Scene functionality
* [ ] 3D Object Rendering

---

> **Developer:** Ahmet
> **License:** MIT