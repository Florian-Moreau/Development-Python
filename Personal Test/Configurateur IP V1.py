#Florian MOREAU
#07/03/2018
#BTS SIO 1 LAB
#Programme d'un configurateur d'IP pour Windows
#Version 1
#Nécessite Python
#Langage utilisé : Python et Batch
import os
#Création de méthode pour chaque choix
def auto (): #Choix numéro 1
    base = open('base.bat', 'w')
    base.write("""
set /p carte=" Nom de la carte reseau : "
netsh interface ip set address "%carte%" dhcp
netsh interface ip set dns "%carte%" dhcp
pause
erase base.bat
			""")
    base.close()

def manuelle (): #Choix numéro 2
    base = open('base.bat', 'w')#Création du fichier base.bat
    base.write("""
set /p carte=" Nom de la carte reseau : "
set /p IP=" IP : "
set /p mask=" Masque : "
set /p gateway=" Passerelle : "
set /p dns=" DNS : "
netsh interface ip set address "%carte%" static %IP% %mask% %gateway% 1
netsh interface ip set dns "%carte%" static %dns%
pause
erase base.bat
			""")
    base.close()#Fermeture du fichier base.bat après écriture

def lab (): #Choix numéro 3
    base = open('base.bat', 'w')
    base.write("""
netsh interface ip set address "Ethernet" static 172.16.43.225 255.255.0.0 172.16.0.1 1
netsh interface ip set dns "Ethernet" static 172.16.50.25
pause
erase base.bat
			""")
    base.close()

def dnsSeul (): #Choix numéro 4
    base = open('base.bat', 'w')
    base.write("""
set /p carte=" Nom de la carte reseau : "
set /p dns=" DNS : "
netsh interface ip set dns "%carte%" static %dns%
pause
erase base.bat
			""")
    base.close()

def dnsSpe (): #Choix numéro 5
    base = open('base.bat', 'w')
    base.write("""
netsh interface ip set dns "Connexion au réseau local" static 172.16.43.200
pause
erase base.bat
			""")
    base.close()
#Début du programme de lancement
print("Bienvenue sur le configurateur IP de Florian MOREAU")
print("")
print("Faites un choix !")
print("")
print("[+] 1 - Configuration IP automatique    [+]")
print("[+] 2 - Configuration IP manuelle       [+]")
print("[+] 3 - Configuration IP LAB salle info [+]")
print("[+] 4 - Configuration DNS uniquement    [+]")
print("[+] 5 - Configuration DNS 172.16.43.200 [+]")
print("")

choix=int(input("Numéro de votre choix : "))#Entrez le numéro du choix
if choix == 1:
    auto()
if choix == 2:
    manuelle()
if choix == 3:
    lab()
if choix == 4:
    dnsSeul()
if choix == 5:
    dnsSpe()
#Demande l'option de lancement
print("")
print("Faites un choix !")
print("")
print("[+] 1 - Lancer le script        [+]")
print("[+] 2 - Ne pas lancer le script [+]")
choix=int(input("Numéro de votre choix : ")) #Entrez le numéro du choix
print("")
if choix == 1:
    os.startfile("base.bat")#Lancement du base.bat
print("Fin du programme Python")
#Fin du programme
