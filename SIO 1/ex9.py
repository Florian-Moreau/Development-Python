#Exercice 9
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
    Existe=False
    i=N-1 #Initialisation obligatoire pour boucle WHILE
    while i<N-1 and Existe==False:
        if T[i]==X:
             Existe=True
             position=i+1
        else:
            i=i-1
    if Existe==True:
        print("La dernière position de ",X," est ",position)
    else:
        print(X," n'est pas dans le tableau.")

#NE MARCHE PAS 
