#include <SoftwareSerial.h>
#include <Adafruit_Thermal.h>

#define RX_PIN 5 // Choix du port d'entrée
#define TX_PIN 6 // Choix du port de sortie

String prompt;

SoftwareSerial mySerial(RX_PIN, TX_PIN); // RX, TX
Adafruit_Thermal printer(&mySerial);
int heat_time = 1200000000;
Adafruit_Thermal warm_up(heat_time); // Echauffement de l'imprimante

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);  // Vitesse de communication série
  printer.begin(); // Initialiser l'imprimante thermique
}

void loop() {
    if (Serial.available() > 0) // Condition sur l'arrivée d'informations
  {
    prompt = Serial.readString(); // Lecture des données 
    printer.boldOn();
    printer.println(prompt); // Impression des données
    printer.println(); // Saut d'une ligne 
}

    
