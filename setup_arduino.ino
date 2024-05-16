#include <SoftwareSerial.h>
#include <Adafruit_Thermal.h>

#define RX_PIN 7
#define TX_PIN 8

String prompt;

SoftwareSerial mySerial(RX_PIN, TX_PIN); // RX, TX
Adafruit_Thermal printer(&mySerial);
int heat_time = 120000;
Adafruit_Thermal warm_up(heat_time); // Echauffement de l'imprimante

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);  // Vitesse de communication série
  printer.begin(); // Initialise l'imprimante thermique
  
  //Choix des ports utilisés par le bouton
  pinMode(9, INPUT); // Ports en position de receveur
  pinMode(10, INPUT);
  pinMode(11, INPUT);
  digitalWrite(9, HIGH); // Ouverture des ports
  digitalWrite(10, HIGH);
  digitalWrite(11, HIGH);
}

void loop() {

  // Lire les valeurs des ports numériques
  int valeur0 = digitalRead(9);
  int valeur1 = digitalRead(10);
  int valeur2 = digitalRead(11);
  int valeur3 = digitalRead(12);
  int valeur4 = digitalRead(13);

  // Envoyer les valeurs via le port série
  Serial.print(valeur0);
  Serial.print(",");
  Serial.print(valeur1);
  Serial.print(",");
  Serial.print(valeur2);
  Serial.print(",");
  Serial.print(valeur3);
  Serial.print(",");
  Serial.println(valeur4);
  delay(1000);
  
  // Imprimer les phrases si on en reçoit une phrase
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
