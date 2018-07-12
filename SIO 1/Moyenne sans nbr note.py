i=0 # Compte le nombre de notes
S=0 # On stocke les notes dedans
print("Entrer une note négative lorsque toutes les notes ont été saisies")
note=float(input("Entrer la première note : "))
while note >=0:
           S=S+note
           i=i+1
           note=float(input("Entrer la note numéro "+str(i+1)+" : "))
moyenne=S/i
print("La moyenne des ",i," notes saisies est : ",moyenne)
