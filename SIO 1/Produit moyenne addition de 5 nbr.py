T=[0]*5
somme=0
moyenne=0
produit=1
for i in range (5):
    print ("Entrer l'élément N° ",i+1,end=" : ")
    T[i]=float(input())
    somme=somme+T[i]
    produit=produit*T[i]
    moyenne=T[i]/5+moyenne
for i in range (5):
    print ("l'élément N° ",i+1," du tableau est ",T[i])
print(T[0]," + ",T[1], " + ",T[2]," + ",T[3]," + ",T[4]," = ",somme)
print(T[0]," * ",T[1], " * ",T[2]," * ",T[3]," * ",T[4]," = ",produit)
print("( ",T[0]," + ",T[1], " + ",T[2]," + ",T[3]," + ",T[4]," ) / 5 = ",moyenne)
