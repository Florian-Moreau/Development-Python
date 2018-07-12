def tableMulti(base,debut,fin):
    print('Partie de la table de multiplication par',base,' : ')
    n=debut
    while n<=fin:
        print(n,'x','=',n*base)
        n=n+1
    tableMulti(8,13,17)
