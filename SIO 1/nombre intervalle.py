n=int(input("Entrer un nombre entier compris entre 123 et 773 : "))
while n<123 or n>773:
    n=int(input("Attention le nombre doit être comprise entre 123 et 773 : "))
if n%9==0:
    print("Le nombre ",n," est pas un multiple de 9")
else:
    print("Le nombre ",n," n'est pas un multiple de 9")
        
