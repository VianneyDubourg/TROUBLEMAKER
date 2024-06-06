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

  // Choix des ports utilisés par le bouton
    // Passer des ports numériques en receveur
    pinMode(13, INPUT);
    pinMode(12, INPUT);
    pinMode(11, INPUT);
    pinMode(10, INPUT);
    pinMode(9, INPUT);
    pinMode(8, INPUT);
    pinMode(5, INPUT);
    pinMode(4, INPUT);
    // Allumer des ports numériques
    digitalWrite(13, HIGH);
    digitalWrite(12, HIGH);
    digitalWrite(11, HIGH);
    digitalWrite(10, HIGH);
    digitalWrite(9, HIGH);
    digitalWrite(8, HIGH);
    digitalWrite(5,HIGH);
    digitalWrite(4,HIGH);
}

void loop() {
  // Lire les valeurs des ports numériques
  int valeur0 = digitalRead(8);
  int valeur1 = digitalRead(9);
  int valeur2 = digitalRead(10);
  int valeur3 = digitalRead(11);
  int valeur4 = digitalRead(12);
  int valeur5 = digitalRead(13);
  int valeur6 = digitalRead(5);
  int valeur7 = digitalRead(4);

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
  Serial.print(valeur5);
  Serial.print(",");
  Serial.print(valeur6);
  Serial.print(",");
  Serial.println(valeur7);
  delay(100);
  
  // Imprimer les phrases si on reçoit des données
  if (Serial.available() > 0)
  {
    Adafruit_Thermal warm_up(heat_time);
    // Créer une nouvelle variable en lisant la phrase envoyée par le PC
    prompt = Serial.readString();
    // Paramétrer l'interligne
    printer.setLineHeight(20);
    // Ecrire en gras
    printer.boldOn();
    // Imprimer la phrase
    printer.println(prompt);
    // Sauter une ligne
    printer.feed();
  // Attendre une demie seconde
  delay(500);
} 
}
