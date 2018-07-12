#Exercice 10
from random import *
N=int(input("Entrer le nombre d'éléments du tableau : "))
T=[0]*N #Tableau contenant N zéros au départ
if N==0:
    print("Ce tableau est vide.")
else:
    for i in range(N):
        T[i]=randint(0,100) #Entiers aléatoires entre 0 et 100
    print("Tableau dans le désordre : ",T)
    print("Entrer l'indice de l'élément à consulter dans le tableau : ")
    X=int(input()) #On cherche si X est dans le tableau
    compteur=0 # Compte le nombre de fois ou X est présent dans le tableau
    for i in range(N):
        if T[i]==X:
            compteur=compteur+1
    if compteur==0:
        print(X," n'est pas présent dans le tableau")
    else:
        print(X," est présent ",compteur," fois ")
