def moyenne(L):
    somme=0
    for i in range (len(L)):
        somme=somme+L[i]
    return somme/len(L)

n=int(input("Entrer le nombre d'éléments du tableau : "))
T=[0]*n #Permet d'ajouter un nombre saisi dans le tableau T
for i in range(n):
    print("Entrer l'élément N° ",i+1,end=" : ")
    T[i]=int(input())
print(T)
print(moyenne (T))
