#include <SoftwareSerial.h>
#include <Adafruit_Thermal.h>

#define RX_PIN 5
#define TX_PIN 6

String prompt;

SoftwareSerial mySerial(RX_PIN, TX_PIN); // RX, TX
Adafruit_Thermal printer(&mySerial);

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);  // Vitesse de communication série
  printer.begin(); // Initialise l'imprimante thermique
}

void loop() {
    if (Serial.available() > 0)
  {
    prompt = Serial.readString();
    printer.println(prompt);
    printer.println();  
}

    
