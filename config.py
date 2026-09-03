# config.py
# Quick tweaks for the demo

# How close they need to be to trigger panic (0.0 to 1.0)
# 0.40 = halfway up the frame, ~2-3 meters away with typical webcam
TRIGGER_PROXIMITY = 0.42

# Confidence threshold for YOLO person detection
CONF_THRESHOLD = 0.55

# Web camera index (0 is usually built-in, 1 or 2 if using external USB cam)
CAMERA_INDEX = 0

# Serial port for Arduino / ESP32 (set to None or "" if running without hardware)
SERIAL_PORT = "COM3"
BAUD_RATE = 9600

# What to open when boss is detected
TABS_TO_OPEN = [
    "https://www.youtube.com/watch?v=1-xGerv5FOk",  # Entry of the Gladiators (Circus theme)
    "https://www.google.com/search?q=how+to+steal+office+stationery+without+getting+caught",
    "https://www.google.com/search?q=fake+doctor+note+for+sick+leave+pdf+free",
    "https://krunker.io",
]
