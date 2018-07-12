#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from tkinter import * 

fenetre = Tk()

s = Spinbox(fenetre, from_=0, to=10)
s.pack()

fenetre.mainloop()
