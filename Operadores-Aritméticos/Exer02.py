# Exercício 2: Calculando o Troco

#Objetivo: Simular uma compra e calcular quanto de troco o cliente deve receber.

valorProduto = float(input('Digite o valor do Produto: '))
valorPago = float(input('Digite o valor pago pelo Cliente: '))

print(f'O troco é: R$ {valorPago - valorProduto:.2f}')