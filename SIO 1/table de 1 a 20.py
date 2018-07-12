# Programme tulisent la procédure table, affiche les tables de 1 à 20
def table(base):
    n=1
    while n<11:
        print(n*base,end=" ")
        n=n+1
a=1
while a<=20:
    table(a) # On fait appel à la proce nommé table t'en que a!=20
    a=a+1
    print (
        ) # saut de ligne
