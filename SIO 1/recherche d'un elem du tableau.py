from random import randint

n=int(input("Entrer le nombre d'éléments du tableau : "))
T=[0]*n #Permet d'ajouter un nombre saisi dans le tableau T
elem=0
if n==0:
    print("Ce tableau est vide")
else:
    for i in range(n):
        T[i]=randint(1,100)
elem=int(input("Entrer le numéro de l'élément que vous voulez : "))
print("L'élément N° ",elem," est égal à ",T[elem-1])
