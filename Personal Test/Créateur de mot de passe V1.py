#Florian MOREAU
#08/03/2018
#BTS SIO 1 LAB
#Programme qui génére des chaînes de mot de passe
#Version 1
#Nécessite Python
#Langage utilisé : Python

import random

element = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*/~$%&.:?!" #Elément possible
passwd = "" #Stock chaque mot de passe
tampon = 0 #Utile pour la boucle tant que
nbr_caractere = int(input("Entrez le nombre de caractère par mot de passe : "))
nbr_Mdp = int(input("Entrez le nombre de mot de passe à généré : "))
T=[]*nbr_Mdp #Tableau rassemblant tout les mots de passe
while tampon<nbr_Mdp:
    passwd = ""
    for i in range(nbr_caractere): passwd = passwd + element[random.randint(0, len(element) - 1)] #Création d'un mot de passe aléatoire avec les éléments préséléctionné
    T.append(passwd) #Ajoute le mot de passe dans le tableau T
    print(passwd)
    tampon = tampon+1
print("")
print("Voici un tableau du résultat : ")
print("")
print(T)

print("")
print("Voulez-vous enregistré la liste des mots de passe dans un fichier texte ?")
print("[+] 1 - Oui [+]")
print("[+] 2 - Non [+]")
choix = int(input("Réponse : "))

if choix == 1:
    fichier = open("passwd.txt", "w") #Ouvre un fichier passwd.txt
    for i in range (0,nbr_Mdp):
        fichier.write(T[i] + "\n") #écris la liste + saut de ligne ("\n")
    fichier.close() #Ferme le fichier
    print("Les mots de passe ont été enregistré dans le fichier passwd.txt")
else:
    print("Les mots de passe n'ont pas été sauvé")
print("")
print ("Fin du programme")
