T=[0]*5
somme=0
for i in range (5):
    print ("Entrer l'élément N° ",i+1,end=" : ")
    T[i]=float(input())
    somme=somme+T[i]
for i in range (5):
    print ("l'élément N° ",i+1," du tableau est ",T[i])
print("On additionne le tout ")
print(T[0]," + ",T[1], " + ",T[2]," + ",T[3]," + ",T[4]," = ",somme)
