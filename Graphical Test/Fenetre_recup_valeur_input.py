#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import *
from tkinter.messagebox import *

fenetre = Tk()

def recupere():
    showinfo("Alerte", entree.get())

value = StringVar() 
value.set("Valeur")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()

bouton = Button(fenetre, text="Valider", command=recupere)
bouton.pack()


fenetre.mainloop()
