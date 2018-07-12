#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import *
from tkinter.messagebox import *

fenetre = Tk()

Button(fenetre, text='L1-C1', borderwidth=1).grid(row=1, column=1)
Button(fenetre, text='L1-C2', borderwidth=1).grid(row=1, column=2)
Button(fenetre, text='L2-C3', borderwidth=1).grid(row=2, column=3)
Button(fenetre, text='L2-C4', borderwidth=1).grid(row=2, column=4)
Button(fenetre, text='L3-C3', borderwidth=1).grid(row=3, column=3)


fenetre.mainloop()
