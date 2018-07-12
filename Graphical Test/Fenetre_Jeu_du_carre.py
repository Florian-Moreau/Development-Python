###
 # ******************************** #
 # Programme Jeu du Carreau         #
 # Auteur Florian MOREAU            #
 # 27/05/2018                       #
 # deplacer le carreau              #
 # Python V3.6.4 et module tkinter  #
 # ******************************** #
###

#############
#Paquet utilisé
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
#############

#############
#Declaration de la fenetre
fenetre = Tk()
#############

#############
#Les fonctions
#############

def clavier(event): #Clavier
    global coords

    touche = event.keysym

    if touche == "Up":
        coords = (coords[0], coords[1] - 10)
    elif touche == "Down":
        coords = (coords[0], coords[1] + 10)
    elif touche == "Right":
        coords = (coords[0] + 10, coords[1])
    elif touche == "Left":
        coords = (coords[0] -10, coords[1])
    # changement de coordonnées pour le rectangle
    canvas.coords(rectangle, coords[0], coords[1], coords[0]+25, coords[1]+25)
    print(coords)
def Gauche():
    global coords
    coords = (coords[0] -10, coords[1])
    canvas.coords(rectangle, coords[0], coords[1], coords[0]+25, coords[1]+25)
    
def Droite():
    global coords
    coords = (coords[0] + 10, coords[1])
    canvas.coords(rectangle, coords[0], coords[1], coords[0]+25, coords[1]+25)
    
def Haut():
    global coords
    coords = (coords[0], coords[1] - 10)
    canvas.coords(rectangle, coords[0], coords[1], coords[0]+25, coords[1]+25)

def Bas():
    global coords
    coords = (coords[0], coords[1] + 10)
    canvas.coords(rectangle, coords[0], coords[1], coords[0]+25, coords[1]+25)


#####################
#       Start       #
#####################


# création du canvas
canvas = Canvas(fenetre, width=250, height=250, bg="ivory")

Button(fenetre, text ='Gauche', command=Gauche).pack(side=LEFT, padx=5, pady=5)
Button(fenetre, text ='Droite', command=Droite).pack(side=RIGHT, padx=5, pady=5)
Button(fenetre, text ='Haut', command=Haut).pack(side=TOP, padx=5, pady=5)
Button(fenetre, text ='Bas', command=Bas).pack(side=BOTTOM, padx=5, pady=5)

# coordonnées initiales
coords = (0, 0)
# création du rectangle
rectangle = canvas.create_rectangle(0,0,25,25,fill="violet")
# ajout du bond sur les touches du clavier
canvas.focus_set()
canvas.bind("<Key>", clavier)
# création du canvas
canvas.pack()
fenetre.mainloop()
