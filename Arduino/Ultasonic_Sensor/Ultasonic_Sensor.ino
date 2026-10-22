// include the code library for the sensor
#include "SR04.h"

// Specify pins for communicating with the sensor
int trig_pin = 12;
int echo_pin = 11;

// get an instance of an SR04 object representing the sensor
SR04 sensor = SR04(echo_pin,trig_pin);

// a variable for distnace measurments
long distance;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(1000);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  distance=sensor.Distance();
  Serial.println(distance);
  delay(1000);
}
