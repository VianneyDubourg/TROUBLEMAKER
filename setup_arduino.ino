#include <SoftwareSerial.h>
#include <Adafruit_Thermal.h>

#define RX_PIN 6
#define TX_PIN 7

String prompt;

SoftwareSerial mySerial(RX_PIN, TX_PIN);
Adafruit_Thermal printer(&mySerial);
int heat_time = 120000;
Adafruit_Thermal warm_up(heat_time);

void setup() {
  // Initialiser l'imprimante
  Serial.begin(9600);
  mySerial.begin(9600);
  printer.begin();
  //printer.setTimes(30000,2100); // Modifie le comportement de l'imprimante

  // Choix des ports utilisés par le bouton
    // Passage des ports numériques en receveur
    pinMode(13, INPUT);
    pinMode(12, INPUT);
    pinMode(11, INPUT);
    pinMode(10, INPUT);
    pinMode(9, INPUT);
    pinMode(8, INPUT);
    // Allumage des ports numériques
    digitalWrite(13, HIGH);
    digitalWrite(12, HIGH);
    digitalWrite(11, HIGH);
    digitalWrite(10, HIGH);
    digitalWrite(9, HIGH);
    digitalWrite(8, HIGH);
}

void loop() {

  // Lire les valeurs des ports numériques
  int valeur0 = digitalRead(8);
  int valeur1 = digitalRead(9);
  int valeur2 = digitalRead(10);
  int valeur3 = digitalRead(11);
  int valeur4 = digitalRead(12);
  int valeur5 = digitalRead(13);

  // Envoyer les valeurs via le port série
  Serial.print(valeur0);
  Serial.print(",");
  Serial.print(valeur1);
  Serial.print(",");
  Serial.print(valeur2);
  Serial.print(",");
  Serial.print(valeur3);
  Serial.print(",");
  Serial.print(valeur4);
  Serial.print(",");
  Serial.println(valeur5);
  delay(1000);
  
  // Imprimer les phrases si on reçoit des données
  if (Serial.available() > 0)
  {
    Adafruit_Thermal warm_up(heat_time);
    prompt = Serial.readString();
    printer.setLineHeight(20);
    printer.boldOn();
    printer.println(prompt);
    printer.feed();
  delay(100);
} 
}
