# Fonction PERMUT
def PERMUT(A,B):
    temp=A # Variable temporaire
    A=B
    B=temp
    return A,B
# Appel
A=int(input("Entrer A : "))
B=int(input("Entrer B : "))
print(PERMUT(A,B))
