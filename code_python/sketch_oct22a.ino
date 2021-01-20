/*
    On each loop, this program checks the analog input connected to the LDR and adjust
    the brightness of the RGB Green LED to match the measured brightness.
*/
#include "ESP8266WiFi.h"

const int BUTTON_PIN = 4;    // Define pin the button is connected to
const int ON_BOARD_LED = 2;  // Define pin the on-board LED is connected to
const int RGB_G_PIN = 12;    // RGB Green LED
const int LDR_PIN = A0;      // Define the analog pin the LDR is connected to

//===============================================================================
//  Initialization
//===============================================================================
void setup() {
  pinMode(ON_BOARD_LED, OUTPUT);       // Initialize the LED_BUILTIN pin as an output
  pinMode(BUTTON_PIN, INPUT_PULLUP);  // Initialize button pin with built-in pullup.
  Serial.begin(115200);               // Set comm rate to 115200
  delay(5);

}



void loop() {
  int lightIntensity;

  lightIntensity = analogRead(LDR_PIN);  // Read the light intensity
  // analogWrite( RGB_G_PIN, map(lightIntensity, 40, 1023, 0, 1023)); // if we want to make led change it's intensity
  Serial.println(lightIntensity);
  delay(5);
  
}