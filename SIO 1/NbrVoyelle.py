#Excercice 3
def NBRVOYELLE():
    n=0
    phrase=str(input("Entrer une phrase en minuscule : ")) #Phrase
    for i in range(len (phrase)):
        if phrase[i] == "a" or phrase[i] == "e" or phrase[i] == "y" or phrase[i] == "u" or phrase[i] == "i" or phrase[i] == "o":
            n=n+1
    print (n)

NBRVOYELLE()
