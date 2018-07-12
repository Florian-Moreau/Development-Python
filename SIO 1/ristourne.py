#Question 1 : Fonction Ristourne
def RIST(CA):
      if CA<1500:
          MtRist=0
      elif CA>=1500 and CA<=15000:
          MtRist=CA*0.03*1.196
      else:
          MtRist=CA*0.05*1.196
      return MtRist

# Programme d'appel
N=int(input("Entrer le nombre de clients : "))
RistTotale=0
for I in range(N):
    CAClient=float(input("Entrer le chiffre d'affaire du client : "))
    RistClient=RIST(CAClient)
    print("Ristourne client = ", RistClient)
    RistTotale=RistTotale+RistClient
RistMoyenne=RistTotale/N
print("Ristourne Moyenne = ",RistMoyenne)


#1500 < CA < 15000 3%
#CA >= 15000 5%
