nome= input ('nome de usuário: ')
senha= int(input('digite sua senha '))

if nome == "admin" and senha == 1234:
    print('acesso concluido')
else:
    print('acesso negado')