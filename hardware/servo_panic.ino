/*
 * servo_panic.ino
 * Hardware trigger for CareerDestructor 3000
 * Board: Arduino Uno / Nano / ESP32
 * 
 * Wire SG90 Servo:
 *   Brown/Black -> GND
 *   Red         -> 5V
 *   Orange/Yellow -> Pin 9
 */

#include <Servo.h>

Servo flailServo;
const int SERVO_PIN = 9;

void setup() {
  Serial.begin(9600);
  flailServo.attach(SERVO_PIN);
  flailServo.write(0); // parked position
}

void loop() {
  if (Serial.available() > 0) {
    char signal = Serial.read();

    if (signal == 'P') {
      // Violent flail to knock coffee cup or wave flag
      for (int i = 0; i < 4; i++) {
        flailServo.write(170);
        delay(140);
        flailServo.write(10);
        delay(140);
      }
      flailServo.write(0);
    }
  }
}
