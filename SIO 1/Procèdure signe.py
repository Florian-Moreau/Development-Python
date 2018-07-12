#Programme de procédure
def signe(x):
    if x<0:
        print (x, " est négatif")
    elif x>0:
        print (x, " est positif")
    else:
        print (x, " est nul")
#End

#Programme d'appel
nombre = float (input("Entrer un nombre : "))
print (nombre, " est : ")
signe(nombre)
