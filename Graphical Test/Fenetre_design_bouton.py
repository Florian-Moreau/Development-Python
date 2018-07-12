#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import *
from tkinter.messagebox import *

fenetre = Tk()

b1 = Button(fenetre, text ="FLAT", relief=FLAT).pack()
b2 = Button(fenetre, text ="RAISED", relief=RAISED).pack()
b3 = Button(fenetre, text ="SUNKEN", relief=SUNKEN).pack()
b4 = Button(fenetre, text ="GROOVE", relief=GROOVE).pack()
b5 = Button(fenetre, text ="RIDGE", relief=RIDGE).pack()

fenetre.mainloop()
