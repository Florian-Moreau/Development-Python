def diviseur():
    N=int(input("Entrer un entier naturel : "))
    t=[]
    for i in range(1,N+1):
        if N%i==0:
            t.append(i)
    print("Tableau des diviseurs de ",N," : ",t)
diviseur()
