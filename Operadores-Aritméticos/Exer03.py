# Desafio: Máquina de Cálculos

#Objetivo: Criar um programa que recebe dois números e mostra:

#A soma
#A subtração
#O dobro do primeiro número
#O quadrado do segundo número
#A média entre os dois números
#O resto da divisão do primeiro pelo segundo

num1 = float(input('Digite o um número: '))
num2 = float(input('Digite outro número: '))

print(f'A soma de {num1} e {num2} é: {num1 + num2}')
print(f'A subtração de {num1} e {num2} é: {num1 - num2}')
print(f'O dobro de {num1} é: {num1 * 2}')
print(f'O quadrado de {num2} é: {num2 ** 2}')
print(f'A média de {num1} e {num2} é: {(num1 + num2)/2:.2f}')
print(f'O resto da divisão do primeiro {num1} pelo segundo {num2} é: {num1 % num2}')