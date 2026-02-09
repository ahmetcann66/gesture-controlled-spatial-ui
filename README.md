<div align="center">

# 🖐️ Gesture Controlled Spatial UI
### ⚡ "The Tony Stark Experience" ⚡

> **A Real-Time, Physics-Enabled Virtual Workspace** > *Create, Manipulate, and Interact with virtual objects using nothing but your hands.*

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand_Tracking-FFA800?style=for-the-badge&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

[Report Bug](https://github.com/ahmetcann66/gesture-controlled-spatial-ui/issues) · [Request Feature](https://github.com/ahmetcann66/gesture-controlled-spatial-ui/issues)

</div>

---

## 🌟 Project Highlights

* **Physics Engine:** Objects interact with gravity, bounce off the floor, and collide with each other realistically.
* **RGB Color Picker:** Dynamic UI to select Red, Green, or Blue for your virtual objects.
* **Zero Hardware:** No VR headsets or gloves required. Just a standard webcam.
* **Modular OOP Design:** Clean, scalable, and maintainable code architecture.

---

## 🧠 System Architecture

This diagram illustrates how data flows from the camera to the physics engine.

```mermaid
graph TD
    A[📷 Webcam Feed] -->|Frames| B(✋ HandTrackingModule)
    B -->|Landmarks| C{🧠 Main Controller}
    
    C -- Index Finger --> D[🖱️ Cursor / UI Select]
    C -- Victory Sign --> E[✨ Create Object]
    C -- Pinch --> F[✊ Grab & Drag]
    C -- Fist --> G[🗑️ Delete Logic]

    E & F --> H[🧩 ObjectManager]
    D --> I[🎨 Color Picker UI]
    
    subgraph Physics Engine
    H -->|Gravity & Velocity| J[Physics Update]
    J -->|Collision Check| K[Bounce & Repel]
    end

    K --> L[🖥️ Render Output]
    I --> L
gesture-controlled-spatial-ui/
├── 📄 main.py                # The Brain: Main loop, UI, and State Machine
├── 📄 HandTrackingModule.py  # The Eyes: MediaPipe wrapper for gesture detection
├── 📄 ObjectManager.py       # The World: Physics, Object properties, and Rendering
├── 📄 baslat.bat             # Quick Start Script
└── 📄 README.md              # Documentation
