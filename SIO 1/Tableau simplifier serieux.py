N=[0]*6
N[0]=1
for k in range (1,6):
    N[k]=N[k-1]+2
print (N)

#Affiche les 6 premiers impairs

N=[1]*6
k=1
while k<6:
    N[k]=N[k-1]+2
    k=k+1
print (N)
