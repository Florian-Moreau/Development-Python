def comptecar (ca, ch):
    total=0
    for i in range len(ch):
        if ch[i]==ca:
            total=total+1
    return total

#FinFonction

#Appel

ch=str(input("Entrer une phrase : "))
ca=str(input("Entrer le caractère cherché : "))
print("Dans cette phrase, il y a ",comptecar(ca,ch)," ",ca)
