n=int(input("Entrer le nombre d'éléments du tableau : "))
T=[0]*n #Permet d'ajouter un nombre saisi dans le tableau T

for i in range(n):
    print("Entrer l'élément N° ",i+1,end=" : ")
    T[i]=float(input())

print("Il y a ",n," valeurs dans le tableau suivant ")
print(T)
