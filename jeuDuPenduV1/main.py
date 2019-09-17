#Importation les modules nécessaires
from random import choice
from fonctions import *
from turtle import *

#Compteur d'erreurs
errors = 0
#Compteur de tour
tour = 0
#Liste d'essaie
essaie = []
#Liste juste
juste = []
#Liste de lettre du mot troué
motTrouer = []
#Numéro de la lettre dans la liste
lettre = 0

#Message de bienvenue
print("Bienvenue au jeu du pendu !")

#Entre chaque ligne de mots.txt dans la liste toutLesMots
toutLesMots = [mot.strip() for mot in open("mots.txt", encoding="utf-8")]

#Affiche le nombres de mots dans la liste
print("Il y a ", len(toutLesMots), "mots possibles")

#Choisi un mot aléatoirement
mot = choice(toutLesMots)
listeMot = list(mot)
#Préparation de l'affchage du mot troué
for i in range (0, len(mot)):
    motTrouer.append("_")

#fonction main
if __name__ == '__main__':

    #Tant que le joueur n'a pas fait 8 erreurs, il peut jouer
    while errors != 8:

        #Indentation du tour
        tour += 1
        print("")
        print("Tour numéro : ", tour)

        #Affichage des lettres déjà transmises
        print("Voici les lettres déjà utilisées : ", essaie)

        #Affichage du mot troué
        print(f"Voici les lettres du mots à trouvé : {motTrouer}")
        #Récupération de la lettre choisit
        choixLettre = ((input("Entrez une lettre : ")))

        #Insère la lettre au sein de la liste en minuscule
        essaie.append(choixLettre.lower())

        #Test de vérification
        if verifLettre(essaie[lettre], mot) == True:

            #Affiche que la lettre est en effet dans le mot !
            print(f"La lettre {essaie[lettre]} fait partie du mot !")

        else:
            print("Lettre invalide !")
            #Nombre d'erreur augmente
            errors += 1

        #Remplace le caractère vide par la lettre correspondante
        for i in range (0, len(mot)):
            if essaie[lettre] == mot[i]:
                motTrouer[i] = mot[i]

        #Victoire !
        if motTrouer == listeMot:
            print("")
            print("XXXXXXXXXXXXXXXX")
            print("Vous avez gagné !")
            print("XXXXXXXXXXXXXXXX")
            print(f"Voici le mot trouvé : {mot}")
            print("XXXXXXXXXXXXXXXX")
            print("")
            break
        #Indentation du numéro de lettre
        lettre += 1


    print(f"Le jeu est terminé en {tour} tours !")
