#Exercice 6
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
    i=int(input()) #On cherche si X est dans le tableau
    if i<0 or i>N-1:
        print("Position hors limite du tableau.")
    else:
        print("L'élément à consulter est : ",T[i-1])
