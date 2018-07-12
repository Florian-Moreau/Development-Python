#Scrabble
#Florian MOREAU
#Lethfy
def POINTS(L):
    
    if L=="d" or L=="g" or L=="m":
        P=2
    elif L=="b" or L=="c" or L=="p":
        P=3
    elif L=="f" or L=="h" or L=="v":
        P=4
    elif L=="j" or L=="q":
        P=8
    elif L=="k" or L=="w" or L=="x" or L=="y" or L=="z":
        P=10
    else:
        P=1
    return P

#End points


totalpoints=0 #Initialisation des points
mot=str(input("Entrer un mot en lettre minuscule : ")) #On entre un mot
for i in range(len (mot)):
    totalpoints=totalpoints+POINTS(mot[i])
#end for
print("Votre score est de ",totalpoints)
