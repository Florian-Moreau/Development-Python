def remplace_zero(L):
    for i in range (len(L)):
        if L[i]%2==0:
            L[i]=0
    return L

n=int(input("Entrer le nombre d'éléments du tableau : "))
T=[0]*n #Permet d'ajouter un nombre saisi dans le tableau T
for i in range(n):
    print("Entrer l'élément N° ",i+1,end=" : ")
    T[i]=int(input())
print(T)
print(remplace_zero (T))
