#ifndef SR04_H
#define SR04_H

#include <Arduino.h>

class SR04 {
  int echoPin;
  int trigPin;

public:
  SR04(int echo, int trig);
  long Distance();
};

#endif
