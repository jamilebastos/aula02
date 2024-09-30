preço_do_produto= float(input('digite o preço do produto'))
quantidade = int(input('Quantidade:'))

total = preço_do_produto*quantidade

if quantidade >10:
    desconto= total*0.10
    total-= desconto
    print('você recebeu desconto')
else:
    print('você não recebeu desconto')
