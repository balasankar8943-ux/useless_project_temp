# CareerDestructor 3000

Built for TinkerHub Useless Projects make-a-thon.

### The Premise
Traditional "Boss Key" utilities hide games and pop up fake spreadsheets when your manager walks in. 

CareerDestructor 3000 does the opposite: it uses edge computer vision behind your desk to detect someone approaching, and immediately guarantees you get fired on the spot.

### What it does upon detection
1. Cranks system master volume to 100%.
2. Minimizes all open IDEs and code windows (`Win + D`).
3. Launches fullscreen browser tabs with clown circus music, casual web games, and searches for *"how to steal office stationery without getting caught"*.
4. Sends serial signal to an Arduino/ESP32 servo to knock over a dummy coffee cup on your desk.

---

### Setup & Running

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Adjust settings (`config.py`)**:
   - `TRIGGER_PROXIMITY`: Defaults to `0.42` (triggers when the person occupies roughly 40%+ of camera frame height).
   - `SERIAL_PORT`: Set to `"COM3"` (or whatever port your Arduino is on). Leave as `None` if running purely software.
   - `CAMERA_INDEX`: `0` for default webcam, `1` if using a secondary external webcam pointed behind you.

3. **Run**:
   ```bash
   python detector.py
   ```
   *(or double click `run.bat` on Windows)*

---

### Demo Day Controls
- **`[SPACEBAR]`**: Emergency manual trigger. If venue stage lighting causes OpenCV / YOLO to struggle, hit spacebar to force the panic sequence.
- **`[R]`**: Reset / re-arm the trigger after it has fired.
- **`[Q]`**: Quit.

---

### Hardware Wiring (Optional)
- Micro Servo SG90:
  - Red -> 5V
  - Brown -> GND
  - Orange / Signal -> Pin 9 on Arduino Uno / Nano
- Flash `hardware/servo_panic.ino` using the Arduino IDE.
