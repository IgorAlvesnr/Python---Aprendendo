lista = [2,6,9,4,0,12,3,7]
palavra = 'Alves'
pedras = ['Rubi', 'Esmeralda','Quartzo', 'Safira','Diamante','Turmalina']

for item in lista:
    print(lista)

for letra in palavra:
    print(palavra)

for pedra in pedras:
    if pedra == 'Quartzo': # usou o if para especificar um item especifico dento da lista
        continue    #Vai fazer com que pular o que o if pediu e continuar 
    print(pedra)

########################
#Função range(inicial, final):

for numero in range(1,11):
    print(numero)

nome = input('Digite seu nome: ')

for x in range(10):
    print(f'{x+1} {nome}')

#Função range(inicial, final, incremento/decremento):

for x in range(2,20,2):
    print(x)

for x in range(20,2,-2):
    print(x)

