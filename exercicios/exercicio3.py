primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

condicao_1 = primeiro_valor >= segundo_valor
condicao_2 = segundo_valor >= primeiro_valor

if condicao_1:
    print(f'{primeiro_valor=}, é maior ou igual {segundo_valor=}')

elif condicao_2:
    print(f'{segundo_valor=}, é maior maior ou igual {primeiro_valor=}')

else:
    print('Você não digitou um dado válido')





# Resposta do professor:
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )