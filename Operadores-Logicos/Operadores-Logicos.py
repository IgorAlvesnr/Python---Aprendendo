idade = 25
altura = 1.77

resultado = (idade >= 18) and (altura >= 1.70)
msg = 'Pode participar do evento? ' + str(resultado)

print (msg)

#Programa de disparo de alarme

porta = 'f'
janela = 'f'

alarme = (porta == 'a') or (janela == 'a')
msg = 'alarme disparado? ' + str(alarme)
print(msg)

temDinheiro = False
temDinheiro = not temDinheiro

msg = 'Tem dinheiro? ' + str(temDinheiro)
print(msg)