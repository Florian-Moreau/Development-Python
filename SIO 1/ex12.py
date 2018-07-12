#Exercice 12
from random import *
N=int(input("Entrer le nombre d'éléments du tableau : "))
T=[0]*N #Tableau contenant N zéros au départ
X=0
if N==0:
    print("Ce tableau est vide.")
else:
    for i in range(N):
        T[i]=randint(0,100) #Entiers aléatoires entre 0 et 100
    print("Tableau dans le désordre : ",T)
    print("Entrer l'indice de l'élément à consulter dans le tableau : ")
    for i in range(N-1):
        for j in range(i+1,N):
            if T[j]>T[i]:
                temp=T[i]
                T[i]=T[j]
                T[j]=temp
    print("Tableau dans l'ordre : ",T)
