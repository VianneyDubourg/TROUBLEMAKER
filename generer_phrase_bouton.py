import markovify
import serial
import time
import random

# Connexion au arduino
ser = serial.Serial('COM4', 9600)  # Remplacer COM4 par votre port série
ser.flush()

# Fonction pour ouvrir la base de donnée
def charger_donnees(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        texte = f.read()
    return texte

# Choix de la mise en page des prints dans python
underline = '\033[4m'
end_underline = '\033[0m'

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

# Début de la boucle qui permet l'impression de phrases
modeles = []
noms = []
while True:
    # Récolte des informations envoyées par l'arduino
    line = ser.readline().decode('latin-1').rstrip()
    valeurs = line.split(",")
    valeur0 = str(valeurs[0])
    valeur1 = str(valeurs[1])
    valeur2 = str(valeurs[2])
    valeur3 = str(valeurs[3])
    valeur4 = str(valeurs[4])
    valeur5 = str(valeurs[5])
    valeur6 = str(valeurs[6])
    valeur7 = str(valeurs[7])
    
    # Condition sur l'assemblage de plusieurs bases de données
    if str(valeurs[7]) == "0":
        if valeur0 == "0":
            base_de_donnees = "actions_verites.txt"
        elif valeur1 == "0":
            base_de_donnees = "dinosaures_descriptions.txt"
        elif valeur2 == "0":
            base_de_donnees = "citations_celebres.txt"
        elif valeur3 == "0":
            base_de_donnees = "random.txt"
        elif valeur4 == "0":
            base_de_donnees = "dinosaures_noms.txt"
        elif valeur5 == "0":
            base_de_donnees = "rap.txt"
        else:
            base_de_donnees = "erreur.txt"
        # Ajout de la base de données aux modèles
        if base_de_donnees not in noms and base_de_donnees != "dinosaures_noms.txt":
            noms.append(base_de_donnees)
            texte_ajout = charger_donnees(base_de_donnees)
            modeles.append(texte_ajout)
            print("fichiers dans la base de données: ", noms)

    # Condition de lancement pour lancer l'impression
    if str(valeurs[6]) == "0":
        # Utiliser l'assemblage de plusieurs bases de données uniquement si on en a enregistré plusieurs
        if len(noms) > 2 or (len(noms) > 1 and "erreur.txt" not in noms) :
            print("Début de l'impression...")
            modeles_utilises = {}
            coef = {}
            i=0
            for mots in noms:
                i+=1
                modeles_utilises["modele{0}".format(i)] = markovify.Text(charger_donnees(mots))
                coef["{0}".format(i)] = 1
            model_combo = markovify.combine(list(modeles_utilises.values()),list(coef.values()))
            phrase = model_combo.make_sentence()
            ser.write(("----------").encode("utf-8"))
            time.sleep(3)
            for groupe in splitTextToTriplet(str(phrase)):
                ser.write((groupe).encode("utf-8"))
                time.sleep(3)
            print(f"{underline}{'La base de données sélectionnée est:'}{end_underline}{' '}{noms}")
            print(f"{underline}{'La phrase à imprimer est:'}{end_underline}{' '}{phrase}")
            print("Fin d'impression")
            modeles = []
            noms = []

        # Imprimer avec une seule base de données
        else:
            if valeur0 == "0":
                base_de_donnees = "actions_verites.txt"
            elif valeur1 == "0":
                base_de_donnees = "dinosaures_descriptions.txt"
            elif valeur2 == "0":
                base_de_donnees = "citations_celebres.txt"
            elif valeur3 == "0":
                base_de_donnees = "random.txt"
            elif valeur4 == "0":
                base_de_donnees = "dinosaures_noms.txt"
            elif valeur5 == "0":
                base_de_donnees = "rap.txt"
            else:
                base_de_donnees = "erreur.txt"
            
            print("Début d'impression...")
            
            # Charger le fichier sélectionné
            texte = charger_donnees(base_de_donnees)
            
            # Cas particulier pour les noms de dinosaures
            # On spécifie la taille sur laquelle se base markov pour établir des probabilités
            # On supprime aussi les espaces entre chaque syllabes
            if base_de_donnees == "dinosaures_noms.txt":
                ser.write(("----------").encode("utf-8"))
                time.sleep(3)
                modele = markovify.Text(texte)
                phrase = modele.make_sentence()
                phrase = phrase.replace(' ','')
                ser.write((phrase).encode("utf-8"))
                time.sleep(3)
                print(f"{underline}{'La base de données sélectionnée est:'}{end_underline}{' '}{base_de_donnees}")
                print(f"{underline}{'La phrase à imprimer est:'}{end_underline}{' '}{phrase}")
                print("Fin d'impression")
            
            elif base_de_donnees == "erreur.txt":
                print("erreur bouton")
                ser.write(("----------").encode("utf-8"))
                time.sleep(3)
                ser.write(("Bouton invalide").encode("utf-8"))
                time.sleep(3)
            
            else:
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
                ser.write(("----------").encode("utf-8"))

                # Attendre un court instant avec de générer la phrase
                time.sleep(3)

                # Envoyer la phrase sur le port série de l'Arduino par groupe de 4 ou de 3
                if (base_de_donnees == "dinosaures_descriptions.txt") or (base_de_donnees == "random.txt"):
                    for groupe in splitTextToTriplet(str(phrase)):
                        ser.write((groupe).encode("utf-8"))
                        time.sleep(3)
                else:
                    for groupe in splitTextToQuadruplet(str(phrase)):
                        ser.write((groupe).encode("utf-8"))
                        time.sleep(3)

                # Ecrire la phrase pour vérifier
                print(f"{underline}{'La base de données sélectionnée est:'}{end_underline}{' '}{base_de_donnees}")
                print(f"{underline}{'La phrase à imprimer est:'}{end_underline}{' '}{phrase}")
                print("Fin d'impression")
