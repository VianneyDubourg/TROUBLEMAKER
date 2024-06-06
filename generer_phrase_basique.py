import markovify
import serial
import time

# Fonction pour charger le fichier de prompt
def load_prompt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text

# Chemin vers votre fichier prompt.txt
prompt_file = "actions_verites.txt"

# Charger le fichier prompt
text = load_prompt(prompt_file)

# Créer le modèle Markovify
model = markovify.Text(text)

# Configuration du port série
ser = serial.Serial('COM3', 9600)  # Remplacez 'COM3' par le port série de votre Arduino
ser.flush()

# Générer une phrase aléatoire
sentence = model.make_sentence()

# Envoyer une entête sur le port série de l'Arduino
ser.write(("----------").encode())
time.sleep(2)

# Envoyer la phrase sur le port série de l'Arduino
ser.write((sentence).encode())

# Ecrire la phrase pour vérifier
print(sentence)
