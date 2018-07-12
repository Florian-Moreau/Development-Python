#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import *
from tkinter.messagebox import *

fenetre = Tk()

for ligne in range(5):
    for colonne in range(5):
        Button(fenetre, text='L%s-C%s' % (ligne, colonne), borderwidth=1).grid(row=ligne, column=colonne)

fenetre.mainloop()
