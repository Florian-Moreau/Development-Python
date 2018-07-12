n=int(input("Entrer le nombre d'éléments du tableau : "))
T=[0]*n #Permet d'ajouter un nombre saisi dans le tableau T
elem=0
for i in range(n):
    print("Entrer l'élément N° ",i+1,end=" : ")
    T[i]=float(input())
nombre=int(input("Entrer le nombre que vous voulez : "))
for i in range(n):
    if T[i]==nombre:
        print("le nombre choisit est l'élément N° ",i+1)
