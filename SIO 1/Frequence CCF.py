def frequence(L):
    compteur=0
    for i in range (len(L)):
        if L[i]>=10:
            compteur=compteur+1
    compteur= compteur/len(L)*100
    return compteur

n=int(input("Entrer le nombre d'éléments du tableau : "))        
T=[0]*n #Permet d'ajouter un nombre saisi dans le tableau T
for i in range(n):
    print("Entrer l'élément N° ",i+1,end=" : ")
    T[i]=int(input())
print(T)
print(frequence(T),"%")
