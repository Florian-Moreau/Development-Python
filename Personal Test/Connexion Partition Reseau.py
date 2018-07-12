#Florian MOREAU
#07/03/2018
#BTS SIO 1 LAB
#Programme d'un configurateur d'IP pour Windows
#Version 1
#Nécessite Python
#Langage utilisé : Python et Batch
import os
#Création de méthode pour chaque choix
def lab (): #Choix numéro 1
    base = open('connexion.bat', 'w')
    base.write("""
if exist r:\ net use r: /d
net use r: \\172.16.50.10\classes /user:stssio\moreaufl

rem Pour mettre un mdp : net use r: \\172.16.50.10\classes MOTDEPASSE /user:stssio\moreaufl

if exist x:\ net use x: /d
net use x: \\172.16.50.10\outils_etudiants_sio /user:stssio\moreaufl

pause
erase connexion.bat
			""")

#Début du programme de lancement
print("Bienvenue sur le configurateur IP de Florian MOREAU")
print("")
print("Faites un choix !")
print("")
print("[+] 1 - Connexion Réseau Lycée Aristide Bergès   [+]")
print("")

choix=int(input("Numéro de votre choix : "))#Entrez le numéro du choix
if choix == 1:
    lab()
#Demande l'option de lancement
print("")
print("Faites un choix !")
print("")
print("[+] 1 - Lancer le script        [+]")
print("[+] 2 - Ne pas lancer le script [+]")
choix=int(input("Numéro de votre choix : ")) #Entrez le numéro du choix
print("")
if choix == 1:
    os.startfile("connexion.bat")#Lancement du base.bat
print("Fin du programme Python")
#Fin du programme
