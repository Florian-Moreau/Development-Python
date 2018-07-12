# Compte nombre de voyelle et consonne
def VOY_OU_CONS(L):
    
    if L=="a" or L=="e" or L=="y" or L=="u" or L=="o" or L=="i":
        return 1 # La fonction retourne 1 si la lettre saisie est une voyelle
    else:
        return 0 # La fonction retourne 1 si la lettre saisie est une consonne

#appel
nbcons=0 # Initialisation
nbvoy=0  # Initialisation    
mot=str(input("Entrer un mot en lettre minuscule : "))
for i in range (len(mot)):
    if VOY_OU_CONS(mot[i])==1:
        nbvoy=nbvoy+1
    else:
        nbcons=nbcons+1
print("Nombre de voyelle : ",nbvoy," Nombre de consonne : ",nbcons)
