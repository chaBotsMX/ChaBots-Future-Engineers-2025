# Chabots - WRO Future Engineers 2024

![Banner](./other/readme-images/banner.png)

[![Website](https://img.shields.io/badge/Website-Visit-brightgreen?style=for-the-badge&logo=web&logoColor=white)](https://www.chabots.com.mx)
[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white)](https://www.facebook.com/chabotsMX/)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://www.instagram.com/chabotsmx/)
[![Youtube](https://img.shields.io/badge/Youtube-%23FF0000.svg?style=for-the-badge&logo=Youtube&logoColor=white)](https://www.youtube.com/@chabotsmx1956/videos)

This repository contains the documentation for **Chabots** participation in the **WRO Future Engineers 2024** category. Our robot was designed and built by a team of Mexican students passionate about robotics and education.

## Table of Contents

- [The Team](#the-team)
- [The Challenge](#the-challenge)
- [Robot Overview](#robot-overview)
- [Mobility Management](#mobility-management)
- [Power and Sense Management](#power-and-sense-management)
- [Code Overview](#code-overview)
- [Obstacle Management](#obstacle-management)
- [Construction Guide](#construction-guide)
- [Cost Report](#cost-report)
- [Resources](#resources)
- [License](#license)

---

## The Team <a name="the-team"></a>

### Roy Iván Barrón Martínez
**Age:** 19  
**Location:** San Luis Potosí, México  
**Role:** Team Lead, Electronics & Software Design  

I am  a self-taught robotics enthusiast with experience in embedded systems, software, and mechanical integration. my team ChaBots Ocelot win Mexico Robocup soccer Open second place  and achieved multiple national awards in programming and robotics.

> "I enjoy setting nearly impossible goals to push myself while learning. I believe that learning should always lead to building something real."


### [Add Teammate Name]
**Age:** [Age]  
**Location:** [City, State]  
**Role:** [Mechanical design / AI programming / Team logistics / etc.]  

[Short bio of the teammate – use placeholder text if teammate is unknown]

---

### Coach: [Coach Name]  
**Role:** Mentor / Support / Coordination  

[Insert coach description or leave placeholder if undecided]

---

## The Challenge <a name="the-challenge"></a>

The **WRO Future Engineers** challenge pushes students to create fully autonomous self-driving vehicles. Each robot must:

- Navigate a dynamically randomized track
- Detect and avoid colored obstacles (green/red blocks)
- Execute a parallel parking maneuver

Scoring is based on:  
✔ Performance on track  
✔ Obstacle handling  
✔ Documentation quality  
✔ Innovation and engineering rigor

Read more: [WRO Official Site](https://wro-association.org/)

---

## Robot Overview <a name="robot-overview"></a>

> **Name:** _[To be completed]_  
> **Meaning / Acronym:** _[Optional]_  

| Front | Back |
|-------|------|
| ![Front](./robot-photos/front.png) | ![Back](./robot-photos/back.png) |

| Left | Right |
|------|-------|
| ![Left](./robot-photos/left.png) | ![Right](./robot-photos/right.png) |

| Top | Bottom |
|------|--------|
| ![Top](./robot-photos/top.png) | ![Bottom](./robot-photos/bottom.png) |

---

## Mobility Management <a name="mobility-management"></a>


### Drivetrain

**Design Notes:**  
We opted for custom-built steel axles with a diameter of 4mm, connected to Pololu 25D 6V HP motors, which provided sufficient power and torque to meet our performancer requireeriments. The motors have a maximum RPM of, max spee 480, but theour torque output was initially too high for optimal speed. To address this, we implemented  ado we decide use an extra reductional to 2:1 gear reduction, effectively doubling the speed while maintainingto have double speed and approximately 1.8 kg·cm of/ torque—suitable for our application.

The drivetrain base and gear assemblys were manufactured in-hby ourse. We used PLA Carbon Fiber filameona QIDI Q1 proprinter for extra strength and durability. We designed and printed d, and PLA Couble Helical Gears tld  energy transmission efficiency and reduce mechanical wear.

The steel axeis wer to size manually and shapemade by our self using an steel rod, we cut it at the needed size, and usinged a Ddremel tool to create D-shaped shafts, which ensured a secure grip with the wheel hubs. Our wheels were also custom-built using 3D-printed make D Shaft to ensure grip from our wheels, our wheels were also made using , using the same qidi, the made the tire rims, and motor shaft couplers sourcedused some motor coupler shaft we bugth from AaliEexpress. For tires, we repurposed LEGO rubber tires after determining that fabricating our own rubber tires was not viable.

**Motor:** Pololu 25D 6V HP  
**Gear Ratio:** 20.4:1  
**Max RPM:** 480

**Planned Improvements for National Phase:**
- Upgrade to Maxon DCX19 motors for better power-to-weight ratio.
- Implement a differential gear system for smoother cornering.
- Replace LEGO tires with higher-grip, custom-molded polyurethane ones., we used lego wheels tires as we realize that was to dificult to make our selfs tires, d us a remel to rim and  rom liess

**Motor:** [Insert model]  
**Gear Ratio:** [Insert ratio]  
**Max RPM:** [Insert speed]  

**Potential Improvements:**
- Switch to brushless motors for better efficiency and thermal performance.
- Redesign wheel hubs to allowfor quicker swapping and maintenance.
- Manufacture custom
- Add diferential gear
- Make our self tires using cast polyiurethane for improved traction.

- Use Ma

### Steering

We build an ackermann stering systedm to ensure smooth and better turns, we used a mg 995 servo motor cause was dificult to get a better one justo for now, all the mechanism is mounted in our 3d printed chasis and we use PolyMax PC to ensure that our mehcanism have enough sttength,  

**Servo Model:** MG995 
**Rotation Range:** 0-180

**Future Upgrades:**
- Improve servo angle feedback
- Add software-based correction via IMU

---

## Power and Sense Management <a name="power-and-sense-management"></a>

### Battery
- 7.4V 2S LiPo, 450mAh
- Mounted with 3D-printed clip-in bracket

### Microcontroller
- Arduino Nano ESP32 (chosen for Bluetooth, WiFi, and compact footprint)

### IMU
- [BMI088 / MPU6050 / Insert model]  
- Used to calculate angular velocity and compensate drift for better trajectory

### Camera
- OpenMV Cam H7 R2 with custom color filters
- UART communication with Arduino

**Camera uses:**
- Line detection
- Color-based cube detection
- Parking wall identification

### Voltage Regulation
- L7805CV for 5V logic rail
- 3.3V internal regulator for camera

---

## Code Overview <a name="code-overview"></a>

Our codebase is structured in modular components:

| Component     | Language | Description                                |
|---------------|----------|--------------------------------------------|
| Arduino Logic | C++      | PID control, state machine, serial parsing |
| OpenMV Script | Python   | Vision processing and blob tracking        |

> Code snippets are available in the `/code` folder.

---

## Obstacle Management <a name="obstacle-management"></a>

The robot detects and reacts to obstacles in real-time:
- Cube detection via color blob recognition (green and red)
- Dynamic turning decision system (via UART commands)
- Follow-the-object mode with PID steering based on cube centroid

**States:**
- FOLLOW_CUBE
- AVOID_CUBE
- TURN_AROUND
- FIND_PARKING

---

## Construction Guide <a name="construction-guide"></a>

> _This section will describe the assembly process, including STL files and diagrams._

**STL Files Folder:** `3d-models/`

**Sections to complete:**
- Step 0: 3D printing
- Step 1: Steering system
- Step 2: Powertrain and motor mount
- Step 3: Electronic layout
- Step 4: Wiring
- Step 5: Upload firmware

---

## Cost Report <a name="cost-report"></a>

| Item                         | Qty | Unit Cost (MXN) | Total (MXN) |
|------------------------------|-----|------------------|-------------|
| Arduino Nano ESP32          | 1   | 250              | 250         |
| OpenMV Cam H7 R2            | 1   | 1500             | 1500        |
| 450mAh LiPo 7.4V Battery    | 1   | 180              | 180         |
| Gearmotor 50:1 Pololu       | 1   | 400              | 400         |
| MG90S Micro Servo           | 1   | 90               | 90          |
| BMI088 IMU Sensor           | 1   | 300              | 300         |
| TB6612FNG Motor Driver      | 1   | 150              | 150         |
| PLA Filament (prototypes)   | -   | 1kg = 350        | 350         |
| PLA-CF Filament (finals)    | -   | 200g = 150       | 150         |
| **Total**                   |     |                  | **3370 MXN**|

---

## Resources <a name="resources"></a>

- [Chabots Main Site](https://www.chabots.com.mx)
- [WRO Future Engineers Rules PDF](https://wro-association.org/wp-content/uploads/WRO-2024-Future-Engineers-Self-Driving-Cars-General-Rules.pdf)
- [GitHub Repos](https://github.com/chabotsmx) *(to be added)*

---

## License <a name="license"></a>

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software...
(Full license text here)
```

---

> *Document maintained by Chabots | Last updated: April 2025*

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM3NjUzNjAzOSwxMjQ4Mzg0MTM1LC0xMz
I3MTA1MjIzLC00ODE2MzMzODBdfQ==
-->