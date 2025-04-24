idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você é menor de idade.")
elif idade < 60:
    print("Você é adulto.")
else:
    print("Você é idoso.")

# Verificando se um número é positivo, negativo ou zero

numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")


# Sistema de notas simples

nota = float(input("Digite a nota final do aluno: "))

if nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Recuperação.")
else:
    print("Reprovado.")


# Sistema de login simples

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == "admin" and senha == "1234":
    print("Acesso concedido!")
else:
    print("Usuário ou senha incorretos.")


# Verificando par ou ímpar

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
