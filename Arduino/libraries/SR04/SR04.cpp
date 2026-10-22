#include "SR04.h"

SR04::SR04(int echo, int trig) {
  echoPin = echo;
  trigPin = trig;
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

long SR04::Distance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  long duration = pulseIn(echoPin, HIGH);
  long distance = duration * 0.034 / 2;
  return distance;
}
