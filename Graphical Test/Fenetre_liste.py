#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import * 

fenetre = Tk()

# liste
liste = Listbox(fenetre)
liste.insert(1, "Python")
liste.insert(2, "PHP")
liste.insert(3, "jQuery")
liste.insert(4, "CSS")
liste.insert(5, "Javascript")

liste.pack()

fenetre.mainloop()
