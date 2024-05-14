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

# Condition pour le choix de la base de données
def check_condition(valeur):
    start_time = time.time()
    while time.time() - start_time < 2:
        if condition_est_verifiee(valeur):
            return True
        time.sleep(0.5)
    return False

# Fonction pour vérifier la condition
def condition_est_verifiee(valeur):
    return valeur == 0

# Boucle pour définir sur quelle base de donnée on travaille
while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        values = line.split(",")
        analogValueA0 = int(values[0])
        analogValueA1 = int(values[1])
        analogValueA2 = int(values[2])
        if check_condition(analogValueA0)==True:
            prompt_file = "dinosaures.txt"
        if check_condition(analogValueA1)==True:
            prompt_file = "prompt.txt"
        if check_condition(analogValueA2)==True:
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
print(sentence)
print(splitTextToTriplet(str(sentence)))
