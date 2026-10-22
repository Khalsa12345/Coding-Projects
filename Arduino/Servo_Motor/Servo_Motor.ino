#include <Servo.h>

Servo myServo;

int servoDelay=1000;
int servoMax=180;
int servoMin=0;


void setup() {
  // put your setup code here, to run once:
  myServo.attach(9);

}

void loop() {
  // put your main code here, to run repeatedly:
  myServo.write(servoMax);
  delay(servoDelay);

  myServo.write(servoMin);
  delay(servoDelay);
}
