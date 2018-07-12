#Exercice 5
def envers (mot):
    NewMot=""
    for i in range(len (mot)):
            NewMot=mot[i]+NewMot
    return NewMot


#Programme d'appel
mot=str(input("Entrer un mot en minuscule : "))
n=""
if envers(mot)==mot:
    n="Le mot est un palindrome"
else:
    n=envers(mot)
print(n)
