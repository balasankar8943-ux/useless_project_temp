# payload.py
import time
import webbrowser
import pyautogui
import serial
import config

class CareerDestructor:
    def __init__(self):
        self.arduino = None
        self.fired = False
        self._init_serial()

    def _init_serial(self):
        if not config.SERIAL_PORT:
            return
        try:
            self.arduino = serial.Serial(config.SERIAL_PORT, config.BAUD_RATE, timeout=0.5)
            time.sleep(1.5)  # wait for arduino bootloader
            print(f"[+] Connected to servo on {config.SERIAL_PORT}")
        except Exception as err:
            print(f"[-] Hardware unavailable ({err}). Running software-only mode.")
            self.arduino = None

    def crank_volume(self):
        # Spams Windows volume-up key to reach 100%
        for _ in range(50):
            pyautogui.press("volumeup")

    def drop_ide(self):
        # Win + D takes you straight to desktop, hiding all code
        pyautogui.hotkey("win", "d")
        time.sleep(0.15)

    def launch_distractions(self):
        for url in config.TABS_TO_OPEN:
            webbrowser.open_new_tab(url)
            time.sleep(0.2)

    def trigger_servo(self):
        if self.arduino and self.arduino.is_open:
            try:
                self.arduino.write(b"P\n")
            except Exception as e:
                print(f"[-] Serial write error: {e}")

    def execute(self):
        if self.fired:
            return
        self.fired = True
        print("\n>>> CRITICAL THREAT DETECTED. TERMINATING CAREER. <<<")

        self.crank_volume()
        self.drop_ide()
        self.launch_distractions()
        self.trigger_servo()

    def reset(self):
        self.fired = False
        print("\n[i] System re-armed and ready.")

    def cleanup(self):
        if self.arduino and self.arduino.is_open:
            self.arduino.close()
