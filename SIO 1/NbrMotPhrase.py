#Exercice 2

def NBRMOT():
    n=1
    phrase=str(input("Entrer une phrase en minuscule : ")) #Phrase
    for i in range(len (phrase)):
        if phrase[i] == " ":
            n=n+1
    print (n)

NBRMOT()
