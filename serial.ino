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

  // Lire les valeurs des ports analogiques
  int analogValueA0 = analogRead(A0);
  int analogValueA1 = analogRead(A1);
  int analogValueA2 = analogRead(A2);

  // Envoyer les valeurs via le port série
  Serial.print(analogValueA0);
  Serial.print(",");
  Serial.print(analogValueA1);
  Serial.print(",");
  Serial.println(analogValueA2);

  delay(100); // Délai pour éviter de surcharger le port série
  
  if (Serial.available() > 0)
  {
    Adafruit_Thermal warm_up(heat_time);
    prompt = Serial.readString();
    printer.setLineHeight(20);
    printer.boldOn();
    printer.println(prompt);
    printer.feed();
} 
}
