import markovify
import serial
import time

# Fonction pour charger le fichier de prompt
def load_prompt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text

# Chemin vers votre fichier prompt.txt
prompt_file = "prompt.txt"

# Charger le fichier prompt
text = load_prompt(prompt_file)

# Créer le modèle Markovify
model = markovify.Text(text)
time.sleep(10)

# Configuration du port série
ser = serial.Serial('COM9', 9600)  # Remplacez 'COM3' par le port série de votre Arduino
time.sleep(10)

# Générer une phrase aléatoire
sentence = model.make_sentence()

# Envoyer la phrase sur le port série de l'Arduino
ser.write((sentence + '\n').encode('utf-8'))

# Attendre un court instant avant de générer la prochaine phrase
time.sleep(10)
print(sentence)
