#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import *
from tkinter.messagebox import *

fenetre = Tk()

def Gauche():
    showinfo("Alerte", "Gauche !")

def Droite():
    showinfo("Alerte", "Droite !")

def Haut():
    showinfo("Alerte", "Haut !")

def Bas():
    showinfo("Alerte", "Bas !")


Canvas(fenetre, width=250, height=100, bg='ivory').pack(side=TOP, padx=5, pady=5)
Button(fenetre, text ='Gauche', command=Gauche).pack(side=LEFT, padx=5, pady=5)
Button(fenetre, text ='Droite', command=Droite).pack(side=RIGHT, padx=5, pady=5)
Button(fenetre, text ='Haut', command=Haut).pack(side=TOP, padx=5, pady=5)
Button(fenetre, text ='Bas', command=Bas).pack(side=BOTTOM, padx=5, pady=5)

fenetre.mainloop()

#Emplacement
#side=TOP     :  haut
#side=LEFT    :  gauche
#side=BOTTOM  :  bas
#side=RIGHT   :  droite
