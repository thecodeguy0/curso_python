# Introdução às f-strings (formatação de strings)

nome = 'Batata Doce'
altura = 1.88
peso = 75
imc = peso / (altura * altura)
linha_print = f'{nome},tem {altura} de altura, pesa {peso} quilos e seu IMC é: {imc:.2f}'

print(linha_print)