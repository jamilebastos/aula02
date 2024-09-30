frase = input('Digite uma Frase: ')
palavra = input ('Digite uma palavra')

if palavra in frase:
    print(f'a palavra {palavra} está na frase ')
else:
    print ('A palavra não foi encontrada')