Nota1 = float(input('digite a primeira nota: '))
Nota2 = float (input(' digite a segunda nota: '))

if Nota1 > 6 and Nota2 > 6:
    print(f' a nota {Nota1} e {Nota2} são maiores que 6')

elif Nota1 ==6 and Nota2 == 6:
    print(f"as notas{Nota1} e {Nota2} são iguais a 6")

elif Nota1 >= 6:
    print(f'a nota {Nota1} é maior ou igual a 6, mas {Nota2} não é')

elif Nota2 >= 6:
    print(f" a nota {Nota2} é maior ou igual a 6, mas a {Nota1} não é")

else:
    print("nenhuma nota é maior ou igual a 6")

