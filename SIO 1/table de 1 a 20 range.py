# Programme tulisent la procédure table, affiche les tables de 1 à 20
def table(base):
    n=1
    while n<11:
        print(n*base,end=" ")
        n=n+1
for i in range(1,21):
    table(i)

    print(
        )
