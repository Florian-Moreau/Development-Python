#Module de fonction du jeu du pendu

#Verification de la contenance de la lettre essaie au sein de mot
def verifLettre(essaie, mot):

    for i in range (0, len(mot)):
        if essaie == mot[i]:
            return True
