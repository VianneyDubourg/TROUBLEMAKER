#include <SoftwareSerial.h>
#include <Adafruit_Thermal.h>

#define RX_PIN 5
#define TX_PIN 6 

String prompt;

SoftwareSerial mySerial(RX_PIN, TX_PIN); // RX, TX
Adafruit_Thermal printer(&mySerial);
int heat_time = 1200000000;
Adafruit_Thermal warm_up(heat_time);

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);  // Vitesse de communication série
  printer.begin(); // Initialise l'imprimante thermique
}

void loop() {
  if (Serial.available() > 0)
  {
    Adafruit_Thermal warm_up(heat_time);
    prompt = Serial.readString();
    printer.setLineHeight(20);
    printer.boldOn();
    printer.println(prompt);
} 
}
