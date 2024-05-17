import markovify
import serial
import time
import random

# Connexion au arduino
ser = serial.Serial('COM4', 9600)  # Assurez-vous de spécifier le bon port série
ser.flush()

# Fonction pour ouvrir la base de donnée
def charger_donnees(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        texte = f.read()
    return texte

# Boucle pour définir sur quelle base de donnée on travaille
# Chaque valeurs correspond à la position de chaque boutons.
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
        if valeur0 == "0":
            base_de_donnees = "actions_verites.txt"
            break
        if valeur1 == "0":
            base_de_donnees = "dinosaures_descriptions.txt"
            break
        if valeur2 == "0":
            base_de_donnees = "citations_celebres.txt"
            break
        if valeur3 == "0":
            base_de_donnees = "random.txt"
            break
        if valeur4 == "0":
            base_de_donnees = "dinosaures_noms.txt"
            break
        if valeur5 == "0":
            base_de_donnees = "donnees_participants.txt"
        base_de_donnees = "rap.txt" #Cette base de données est prise chaque fois que le bouton n'est pas dans une position valide.
        break

# Charger le fichier sélectionné
texte = charger_donnees(base_de_donnees)

# Cas particulier pour les noms de dinosaures
# On spécifie la taille des la base de données
# On supprime aussi les espaces entre chaque syllabes
if base_de_donnees == "dinosaures_noms.txt":
    ser.write(("----------").encode())
    time.sleep(2)
    modele = markovify.Text(texte,state_size=1)
    phrase = modele.make_sentence()
    phrase = phrase.replace(' ','')
    ser.write((phrase).encode())
    time.sleep(3)
    print(base_de_donnees)
    print(phrase)
    exit()

# Créer le modèle de Markov
modele = markovify.Text(texte)

# Générer une phrase aléatoire cas particulier mode random
# On choisit une phrase aléatoire
if base_de_donnees == "random.txt":
    lignes = open('random.txt').read().splitlines()
    phrase = random.choice(lignes) 
else:
    # Générer une phrase aléatoire avec Markov cas classique
    phrase = modele.make_sentence()

# Envoyer un entête sur le port série de l'Arduino
ser.write(("----------").encode())

# Attendre un court instant avec de générer la phrase
time.sleep(2)

# Fonction pour couper les phrases en groupe de 4
def splitTextToQuadruplet(phrase):
    mots = phrase.split()
    mots_groupes = [' '.join(mots[i: i + 4]) for i in range(0, len(mots), 4)]
    return mots_groupes

# Fonction pour couper les phrases en groupe de 3
def splitTextToTriplet(phrase):
    mots = phrase.split()
    mots_groupes = [' '.join(mots[i: i + 3]) for i in range(0, len(mots), 3)]
    return mots_groupes

# Envoyer la phrase sur le port série de l'Arduino par groupe de 4 ou de 3
if (base_de_donnees == "dinosaures_descriptions.txt") or (base_de_donnees == "random.txt"):
    for groupe in splitTextToTriplet(str(phrase)):
        ser.write((groupe).encode())
        time.sleep(3)
else:
    for groupe in splitTextToQuadruplet(str(phrase)):
        ser.write((groupe).encode())
        time.sleep(3)

# Ecrire la phrase pour vérifier
print(base_de_donnees)
print(phrase)
