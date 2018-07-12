n=int(input("Entrer le nombre d'éléments du tableau : "))
T=[0]*n #Permet d'ajouter un nombre saisi dans le tableau T
negative=0
positive=0
nulle=0
for i in range(n):
    print("Entrer l'élément N° ",i+1,end=" : ")
    T[i]=float(input())
    if T[i]<0:
        negative=negative+1
    elif T[i]>0:
        positive=positive+1
    else:
        nulle=nulle+1
print("Positif : ",positive,"\nNegatif : ", negative, "\nNulle : ",nulle)

# \n permet d'aller à la ligne.
