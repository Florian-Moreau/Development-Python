def frequence(L):
    compteur=0
    for i in range (len(L)):
        if L[i]>=10:
            compteur=compteur+1
    compteur= compteur/len(L)*100
    return compteur

def moyenne(L):
    somme=0
    for i in range (len(L)):
        somme=somme+L[i]
    return somme/len(L)

def saisie():
    list=[]
    nombre=float(input("Entrer une note >= 0 : "))
    while nombre!=-1:
        if nombre<0:
            print("Attention, le nombre doit être positif")
        else:
            list.append(nombre)
        nombre=float(input("Entrer une note >= 0 : "))
    return list
L=saisie()
print("Liste saisie : ", L)
print("Moyenne : ",moyenne(L))
print("Frequence des notes supérieur à 10 : ",frequence(L))
