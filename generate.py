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

# Configuration du port série
ser = serial.Serial('COM3', 9600)  # Remplacez 'COM3' par le port série de votre Arduino

# Générer une phrase aléatoire
sentence = model.make_sentence()

# Attendre un court instant avant de générer la prochaine phrase
time.sleep(2) #On en a besoin

# Envoyer une entête sur le port série de l'Arduino
ser.write(("----------").encode())
time.sleep(4)

# Fonction pour couper les phrases en groupe de 4
def splitTextToTriplet(string):
    words = string.split()
    grouped_words = [' '.join(words[i: i + 4]) for i in range(0, len(words), 4)]
    return grouped_words

# Envoyer la phrase sur le port série de l'Arduino par groupe de 4
for groupe in splitTextToTriplet(str(sentence)):
    ser.write((groupe).encode())
    time.sleep(4)

# Ecrire la phrase pour vérifier
print(sentence)
print(splitTextToTriplet(str(sentence)))
