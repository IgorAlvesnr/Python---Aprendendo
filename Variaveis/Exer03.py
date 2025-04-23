# Desafio: Cadastro com Resumo de Vida

#Objetivo: Criar um mini sistema de cadastro que pede dados ao usuário e mostra um resumo no final.

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
cidade = str(input('Digite a cidade onde você mora: '))
profissão = str(input('Digite sua profissão: '))
diasVividos = idade * 365

print (f'Olá, {nome}! Você tem {idade} anos, mora no {cidade} e trabalha como {profissão}. Você já viveu aproximadamente {diasVividos} dias!')