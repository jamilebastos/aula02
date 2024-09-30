idade =  int(input("Digite sua idade: "))
habilitação = input('você possui habilitação?: (sim/não):' )

if idade >= 18 and habilitação == 'sim':
   print('você pode dirigir')

elif idade < 18:
   print ("você não possui idade para dirigir")
else:
   print("você é maior de idade, mas não tem habilitação")