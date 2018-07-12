# Fonction MAX2
def MAX2(A,B):
    if A>B:
        return A
    else:
        return B

# Programme d'appel
X=int(input("Entrer X : "))
Y=int(input("Entrer Y : "))
Z=int(input("Entrer Z : "))

M=MAX2(X,Y)
print("Le maximum de ", X," " ,Y," ", Z ," est ",MAX2(M,Z))

# On utilise une fois la fonction entre 2 nombre
# On l'incrémente dans M
# On compare le max trouvé (M) par le max d'une autre combinaison
