from random import randrange # permet d'importer le module nécessaire
alea=randrange(101) # renvoi un nombre aléatoire compris entre 0 et 100
s=0
e=1
print("Jouons au nombRE mystère ! Devines à quel nombre je pense :p")
s=int(input("Saisies un nombre ! "))
while s!=alea:
    e=e+1
    if s >=alea:
        s=int(input("Raté ! Trop grand... Essaies encore ! "))
    else:
        s=int(input("Raté ! Trop petit... Essaies encore ! "))
              
print("GG ! Tu as réussi en ",e," fois !")
