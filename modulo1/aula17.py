# Exercício de programação com if e comparação
# Comparar 2 valores e exibir o maior primeiro

primeiro_valor = input('digite o primeiro valor: ')
segundo_valor = input('digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que o {segundo_valor=}')
elif primeiro_valor == segundo_valor:
    print(f'{primeiro_valor=} é igual ao {segundo_valor=}')
else:
     print(f'{segundo_valor=} é maior que o {primeiro_valor=}')


