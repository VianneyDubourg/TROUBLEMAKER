import markovify
import serial
import time

# Connexion au arduino
ser = serial.Serial('COM3', 9600)  # Assurez-vous de spécifier le bon port série
ser.flush()

# Fonction pour ouvrir la base de donnée
def load_prompt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text

# Boucle pour définir sur quelle base de donnée on travaille
while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        values = line.split(",")
        analogValueA0 = str(values[0])
        analogValueA1 = str(values[1])
        analogValueA2 = str(values[2])
        if str(analogValueA0) == "0":
            prompt_file = "prompt.txt"
            break
        if str(analogValueA1) == "0":
            prompt_file = "dinosaures.txt"
            break
        if str(analogValueA2) == "0":
            prompt_file = "citations.txt"
        break

# Charger le fichier prompt
text = load_prompt(prompt_file)

# Créer le modèle Markovify
model = markovify.Text(text)

# Générer une phrase aléatoire
sentence = model.make_sentence()

# Attendre un court instant avant de générer la prochaine phrase
time.sleep(1)

# Envoyer une entête sur le port série de l'Arduino
ser.write(("----------").encode())
time.sleep(2)

# Fonction pour couper les phrases en groupe de 4
def splitTextToTriplet(string):
    words = string.split()
    grouped_words = [' '.join(words[i: i + 4]) for i in range(0, len(words), 4)]
    return grouped_words

# Envoyer la phrase sur le port série de l'Arduino par groupe de 4
for groupe in splitTextToTriplet(str(sentence)):
    ser.write((groupe).encode())
    time.sleep(3)

# Ecrire la phrase pour vérifier
print(prompt_file)
print(sentence)
print(splitTextToTriplet(str(sentence)))
