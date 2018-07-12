#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

fenetre = Tk()

def clavier(event):
    touche = event.keysym
    print(touche)

canvas = Canvas(fenetre, width=500, height=500)
canvas.focus_set()
canvas.bind("<Key>", clavier)
canvas.pack()

fenetre.mainloop()

#D'autre event exite :
#<Button-1>           : Click gauche
#<Button-2>           : Click milieu 
#<Button-3>           : Click droit
#<Double-Button-1>    : Double click droit
#<Double-Button-2>    : Double click gauche
#<KeyPress>           : Pression sur une touche
#<KeyPress-a>         : Pression sur la touche A (minuscule)
#<KeyPress-A>         : Pression sur la touche A (majuscule)
#<Return>             : Pression sur la touche entrée
#<Escape>             : Touche Echap
#<Up>                 : Pression sur la flèche directionnelle haut
#<Down>               : Pression sur la flèche directionnelle bas
#<ButtonRelease>      : Lorsque qu'on relache le click
#<Motion>             : Mouvement de la souris
#<B1-Motion>          : Mouvement de la souris avec click gauche
#<Enter>              : Entrée du curseur dans un widget
#<Leave>              : Sortie du curseur dans un widget
#<Configure>          : Redimensionnement de la fenêtre
#<Map> <Unmap>        : Ouverture et iconification de la fenêtre
#<MouseWheel>         : Utilisation de la roulette
