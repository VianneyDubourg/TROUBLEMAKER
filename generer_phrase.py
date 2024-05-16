import markovify
import serial
import time
import random

# Connexion au arduino
ser = serial.Serial('COM3', 9600)  # Assurez-vous de spécifier le bon port série

# Fonction pour ouvrir la base de donnée
def load_prompt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text

# Boucle pour définir sur quelle base de donnée on travaille
while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        valeurs = line.split(",")
        valeur0 = str(valeurs[0])
        valeur1 = str(valeurs[1])
        valeur2 = str(valeurs[2])
        valeur3 = str(valeurs[3])
        valeur4 = str(valeurs[4])
        valeur5 = str(valeurs[5])
        if str(valeur0) == "0":
            prompt_file = "prompt.txt"
            break
        if str(valeur1) == "0":
            prompt_file = "dinosaures.txt"
            break
        if str(valeur2) == "0":
            prompt_file = "citations.txt"
            break
        if str(valeur3) == "0":
            prompt_file = "random.txt"
            break
        if str(valeur4) == "0":
            prompt_file = "dinosaures_nom.txt"
            break
        if str(valeur5) == "0":
            prompt_file = "donnees_participants.txt"
        prompt_file = "rap.txt"
        break
        
#Pour forcer le choix
#prompt_file = "dinosaures_nom.txt"

# Charger le fichier prompt
text = load_prompt(prompt_file)

# Cas particulier des noms de dinosaures
if prompt_file == "dinosaures_nom.txt":
    ser.write(("----------").encode())
    time.sleep(2)
    model = markovify.Text(text,state_size=1)
    sentence = model.make_sentence()
    sentence = sentence.replace(' ','')
    ser.write((sentence).encode())
    time.sleep(3)
    print(prompt_file)
    print(sentence)
    exit()

# Créer le modèle Markovify
model = markovify.Text(text)

# Générer une phrase aléatoire cas particulier mode random
if prompt_file == "random.txt":
    lines = open('random.txt').read().splitlines()
    sentence = random.choice(lines) 
else:
    # Générer une phrase aléatoire cas classique
    sentence = model.make_sentence()

# Attendre un court instant avant de générer la prochaine phrase
time.sleep(2)

# Envoyer un entête sur le port série de l'Arduino
ser.write(("----------").encode())
time.sleep(2)

# Fonction pour couper les phrases en groupe de 4
def splitTextToQuadruplet(string):
    words = string.split()
    grouped_words = [' '.join(words[i: i + 4]) for i in range(0, len(words), 4)]
    return grouped_words

# Envoyer la phrase sur le port série de l'Arduino par groupe de 4
for groupe in splitTextToQuadruplet(str(sentence)):
    ser.write((groupe).encode())
    time.sleep(3)

# Ecrire la phrase pour vérifier
print(prompt_file)
print(sentence)

