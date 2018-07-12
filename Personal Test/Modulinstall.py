###
 # ******************************** #
 # Programme installation module    #
 # Auteur Florian MOREAU            #
 # 27/05/2018                       #
 # installe module python au choix  #
 # Python V3.6.4 avec module OS     #
 # ******************************** #
###


#############
#Paquet utilisé
import os
#############

#############
#Les fonctions
#############

def tesseract(): #Lance installation de Tesseract
    os.system("start tesseract-ocr-setup-3.05.01.exe")
    
def module_autre():
    module=str(input("Entrer le nom du module : "))
    os.system("py -m pip install " + module)
    
def module_getpip(): #Lance get-pip
    os.system("start get-pip.py")

def module_tkinter(): #Installe module tkinter
    os.system("py -m pip install tkinter")

def module_math(): #Installe module tkinter
    os.system("py -m pip install math")
    
def module_pytesseract():
    os.system("py -m pip install pytesseract")
    
def module_time(): #Installe module time
    os.system("py -m pip install time")

def module_PIL(): #installe module PIL
    os.system("py -m pip install PIL")

def module_numpy(): #Installe module numpy
    os.system("py -m pip install numpy")

#############
#Lancement du programme
#############

print("*-- Choix du module ou paquet --*")
print(" ")
print("1 - get-pip")
print("2 - Tesseract 3.05.01")
print("3 - math")
print("4 - pytesseract")
print("5 - time")
print("6 - PIL")
print("7 - tkinter")
print("8 - numpy")
print("0 - Autre")
print(" ")
nbr=int(input("Numero du module ou paquet a installer : "))

if nbr==0:
    module_autre()
    
elif nbr==1:
    module_getpip()
    
elif nbr==2:
    tesseract()
    
elif nbr==3:
    module_math()

elif nbr==4:
    module_pytesseract()

elif nbr==5:
    module_time()
    
elif nbr==6:
    module_PIL()
    
elif nbr==7:
    module_tkinter()

elif nbr==8:
    module_numpy()
    
else:
    print("ERROR")
