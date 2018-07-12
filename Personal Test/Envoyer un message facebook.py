#Florian MOREAU
#18 Mai 2018
#Script enovyant python à Elsa sur facebook
#Module pyautogui et time requis

import webbrowser
import pyautogui
import time

webbrowser.open('http://www.facebook.com') # site ciblé
time.sleep(30) #temps d'attente en seconde
pyautogui.hotkey('tab')
time.sleep(.1) 
pyautogui.hotkey('tab')
time.sleep(.1) 
pyautogui.hotkey('tab')
time.sleep(.1) 
pyautogui.hotkey('tab')
time.sleep(.1) 
pyautogui.hotkey('tab')
time.sleep(.1) 
pyautogui.hotkey('tab')
time.sleep(.1) 
pyautogui.hotkey('tab')
time.sleep(.1) 
pyautogui.hotkey('tab')#8 tab pour aller sur l'onglet messenger

time.sleep(.1) 
pyautogui.hotkey('enter')
time.sleep(.2) 
pyautogui.hotkey('tab')
time.sleep(.1) 
pyautogui.hotkey('enter')

time.sleep(5) 
pyautogui.hotkey('f','l','o','r','i','a','n') #Selection du récepteur
time.sleep(3) 
pyautogui.hotkey('enter')
time.sleep(.1) 
pyautogui.hotkey('enter')
time.sleep(.1)
pyautogui.hotkey('p','y','t','h','o','n')
time.sleep(.1) 
pyautogui.hotkey('enter')
