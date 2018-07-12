#Exercice 7
from random import *
N=int(input("Entrer le nombre d'éléments du tableau : "))
T=[0]*N #Tableau contenant N zéros au départ
if N==0:
    print("Ce tableau est vide.")
else:
    for i in range(N):
        T[i]=randint(0,100) #Entiers aléatoires entre 0 et 100
    print(T)
    print("Entrer l'indice de l'élément à consulter dans le tableau : ")
    X=int(input()) #On cherche si X est dans le tableau
    Bool=False
    for i in range(N):
        if T[i]==X:
            Bool=True
            print(X," est présent dans la position numéro : ",i+1)
    if Bool==False:
            print(X," n'est pas dans le tableau")
