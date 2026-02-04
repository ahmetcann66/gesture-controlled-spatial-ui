# 🚁 UAV Fleet Command System (CLI)

![Language](https://img.shields.io/badge/Language-C-blue) ![Platform](https://img.shields.io/badge/Platform-Windows%2FLinux-lightgrey) ![License](https://img.shields.io/badge/License-MIT-green) ![Version](https://img.shields.io/badge/Version-V3.3-orange)

## 🎯 Project Purpose
**UAV Fleet Command System** is a C-based simulation designed to demonstrate the logic behind a **Ground Control Station (GCS)**. The primary goal is to simulate the tactical management of a mixed UAV swarm (**TB2, AKINCI, AKSUNGUR**) in a terminal environment.

It simulates critical aerospace software functions:
* **Black Box (Flight Recorder):** Persistent logging of mission data to text files.
* **ISR & Radar Logic:** Stochastic target acquisition and locking mechanisms.
* **Collision Avoidance:** Active altitude scanning to prevent mid-air crashes.
* **Fire Control (FCS):** Weapon release protocols based on safety locks.

### 📐 System Logic & Architecture
The following diagram illustrates the core decision-making loop of the software, including the **Safety Interlocks** and **Data Logging** layer.

```mermaid
graph TD
    Start((Start)) --> Menu{Main Menu}
    
    %% Radar & ISR Logic
    Menu -- 8. Radar Scan --> Radar[Stochastic Sensor Scan]
    Radar -- Target Found --> Lock[State: TARGET LOCKED]
    Radar -- Scan Empty --> Unlock[State: NO TARGET]
    
    %% Fire Control Logic
    Menu -- 5. Fire Mission --> CheckLock{Target Locked?}
    CheckLock -- YES --> Fire[Fire Missile & Update Ammo]
    CheckLock -- NO --> Deny[⛔ Safety Lock Engaged]
    
    %% Navigation & Collision Logic
    Menu -- 3/4. Altitude --> ColCheck{Collision Check}
    ColCheck -- Safe --> Move[Update Altitude & Fuel]
    ColCheck -- Risk --> Block[⛔ Collision Warning]
    
    %% Logging Layer
    Fire -.-> Log[💾 Write to ucus_kayitlari.txt]
    Move -.-> Log
    Lock -.-> Log
    
    Menu -- 0. Exit --> Stop((Terminate))
⚙️ Installation
Prerequisites
You need a C compiler (GCC) installed on your system.

1. Clone the Repository
Open your terminal and clone the project files:

Bash
git clone [https://github.com/ahmetcann66/UAV-Fleet-Command-CLI.git](https://github.com/ahmetcann66/UAV-Fleet-Command-CLI.git)
cd UAV-Fleet-Command-CLI
2. Compile the Code
Compile the source code using GCC:

Bash
gcc main.c -o uav_system
🎮 Usage
Running the Application
For Windows:

Bash
uav_system.exe
For Linux / macOS:

Bash
./uav_system
Controls
The system uses a numeric menu interface. Enter the number corresponding to the action:

1 Switch UAV: Cycle control between TB2, AKINCI, and AKSUNGUR.

3 Ascend: Increase altitude by 1000m (Consumes Fuel).

5 FIRE MISSION: Launch ammunition (Requires Radar Lock).

8 RADAR SCAN: Scan the sector for targets (Required before firing).

0 Exit: Close the simulation and save the Black Box logs.

🖥️ Example Output / Screenshot
When you run the system, the CLI provides visual feedback (ASCII Art) and real-time telemetry.

Plaintext
=== UAV FLEET COMMAND SYSTEM (V3.3 - BLACK BOX) ===

       | 
   ---=|=---
    \_|^|_/    
    AKINCI-TIHA

Selected UAV: AKINCI (Altitude: 5000m | Ammo: 8) [KILITLI]
---------------------------------------
1. IHA Degistir
2. Durum Raporu
3. Yuksel (+1000m, -5 yakit)
...
8. RADAR TARAMASI (ISR Scan)

Seciminiz: 8

[RADAR] Bolge taraniyor... Sinyal araniyor...
!!! TESPIT: Dusman zirhli araci tespit edildi! Kordinatlar kilitlendi. !!!
[SYSTEM] ATIS SISTEMI AKTIF.

Seciminiz: 5

*** HEDEF KILITLENDI... FUSELAGE RELEASED ***
>>> AKINCI, 1 adet MAM-C fuzesi atisladi! HEDEF IMHA EDILDI. <<<
[BILGI] Hedef imha edildi. Radar sifirlandi.
Black Box Log Output (ucus_kayitlari.txt):

Plaintext
[03-02-2026 14:30:10] [SISTEM] UAV Fleet Command System V3.3 Baslatildi.
[03-02-2026 14:31:05] [RADAR] AKINCI RADAR HEDEF TESPIT ETTI.
[03-02-2026 14:31:12] [ATIS] AKINCI MAM-C ATISLADI. Hedef Vuruldu.