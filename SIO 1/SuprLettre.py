#Exercice 4
def SuprLettre():
    phrase=str(input("Entrer une phrase en minuscule : ")) #Phrase
    supr=str(input("Entrer une lettre à supprimer en minuscule : "))
    NewPhrase=""
    for i in range(len (phrase)):
        if phrase[i] != supr:
            NewPhrase=NewPhrase+phrase[i]
    print(NewPhrase)

SuprLettre()
