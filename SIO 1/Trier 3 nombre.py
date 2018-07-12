# Rangement par ordre croissant de 3 nombres quelconques

def PERMUT(A,B):
    temp=A # Variable temporaire
    A=B
    B=temp
    return A,B
# Appel
X=int(input("Entrer X : "))
Y=int(input("Entrer Y : "))
Z=int(input("Entrer Z : "))
if X>Y:
    X,Y=PERMUT(X,Y) # On permute X et Y 
if Y>Z: # Sinon on compare Y et Z
    Y,Z=PERMUT(Y,Z) # Si Y > Z alors on permute Y et Z
if X>Y: # On compare leurs contenus a nouveau car cela à changé
    X,Y=PERMUT(X,Y)

print(X,Y,Z)

