s=0
while n!=0:
      if n<0:
            print("Entrer la note numéro ",i,end=" : ")
            note=float(input())
            s=s+note
      else:
      moyenne=s/n
print("La moyenne est : ",moyenne)
