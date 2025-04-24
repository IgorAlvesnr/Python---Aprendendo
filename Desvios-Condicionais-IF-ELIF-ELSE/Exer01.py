# simples, composto, encadeado

nota1 = nota2 = 0.0
media = 0.0

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

#Calcular média aritmética das notas
media = (nota1 + nota2)/2 

if (media >= 7):
    print('Resultado: Aprovado!')
    print('Parabens!')
elif (media >=5 ):
    print('Aluno em Recuperação!')
else:
    print('Aluno Reprovado...')

print('Sua média é {}'.format(media))