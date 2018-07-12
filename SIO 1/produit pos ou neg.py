n1=int (input("Entrer un premier nombre : "))
n2=int (input("Entrer un second nombre : "))
p=n1*n2
if p<0:
    print (p, " est negatif")
elif p==0:
    print (p, " est nul ")
else:
    print (p, " est positif")
