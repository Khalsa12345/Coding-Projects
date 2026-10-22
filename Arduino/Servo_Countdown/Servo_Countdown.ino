#include <Servo.h>

Servo myServo;

int servoDelay=1000;
int servoMax=180;
int servoMin=0;
int servoPos=0;
int timerSeconds = 60;


void setup() {
  // put your setup code here, to run once:
  myServo.attach(9);

}

void loop() {
  // put your main code here, to run repeatedly:
  for (servoPos = servoMin; servoPos <= servoMax; servoPos += (servoMax/timerSeconds)) {
    myServo.write(servoPos);
    delay(servoDelay);
  }
}
