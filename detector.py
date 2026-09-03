# detector.py
import cv2
import time
from ultralytics import YOLO
import config
from payload import CareerDestructor

def main():
    print("[*] Initializing CareerDestructor 3000...")
    print("[*] Loading YOLOv8 nano weights (downloads automatically on first run)...")
    model = YOLO("yolov8n.pt")

    engine = CareerDestructor()

    cap = cv2.VideoCapture(config.CAMERA_INDEX)
    if not cap.isOpened():
        print(f"[!] Could not open webcam at index {config.CAMERA_INDEX}. Check config.py.")
        return

    print("\n[+] Guard armed.")
    print("    [SPACEBAR] -> Manual trigger (stage fallback)")
    print("    [R]        -> Re-arm after trigger")
    print("    [Q]        -> Exit\n")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_h, frame_w = frame.shape[:2]

        # Run detection specifically for persons (class 0)
        results = model(frame, classes=[0], conf=config.CONF_THRESHOLD, verbose=False)

        closest_ratio = 0.0
        closest_box = None

        for r in results:
            for box in r.boxes:
                coords = box.xyxy[0].cpu().numpy().astype(int)
                x1, y1, x2, y2 = coords
                box_h = y2 - y1
                ratio = box_h / float(frame_h)

                if ratio > closest_ratio:
                    closest_ratio = ratio
                    closest_box = (x1, y1, x2, y2)

        # Draw closest person & calculate trigger
        if closest_box:
            x1, y1, x2, y2 = closest_box
            is_threat = closest_ratio >= config.TRIGGER_PROXIMITY
            color = (0, 0, 255) if is_threat else (0, 220, 0)

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            label = f"Boss Proximity: {closest_ratio * 100:.1f}%"
            cv2.putText(frame, label, (x1, max(y1 - 10, 20)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, color, 2)

            if is_threat and not engine.fired:
                engine.execute()

        # HUD Overlay
        status_text = "STATUS: FIRED (Press R to Reset)" if engine.fired else "STATUS: ARMED & WATCHING"
        status_color = (0, 0, 255) if engine.fired else (0, 200, 0)

        cv2.rectangle(frame, (0, 0), (frame_w, 35), (20, 20, 20), -1)
        cv2.putText(frame, status_text, (12, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.65, status_color, 2)

        # Draw threshold marker on right side of frame
        thresh_y = int(frame_h * (1.0 - config.TRIGGER_PROXIMITY))
        cv2.line(frame, (frame_w - 30, thresh_y), (frame_w, thresh_y), (0, 0, 255), 2)
        cv2.putText(frame, "Limit", (frame_w - 65, thresh_y + 4),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

        cv2.imshow("Rear-Guard Sensor", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord(" "):
            print("[!] Manual trigger activated via spacebar.")
            engine.execute()
        elif key == ord("r") or key == ord("R"):
            engine.reset()
        elif key == ord("q") or key == ord("Q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    engine.cleanup()
    print("[*] Exited cleanly.")

if __name__ == "__main__":
    main()
