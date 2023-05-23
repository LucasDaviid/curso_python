# Exercício - Calculadora com while

while True:
    numero_1 = input('Digite um número: ')
    operador = input('Digite o operador (+-*/): ')
    numero_2 = input('Digite outro número: ')
    

    numeros_validos = None
    nfloat_1 = 0
    nfloat_2 = 0
    
    try:
        nfloat_1 = float(numero_1)
        nfloat_2 = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números são inválidos.')
        continue
    
    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Operador inválido. Aceitos +-*/')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    print(f'{nfloat_1} {operador} {nfloat_2} =', end = ' ')

    if operador == '+':
        print(nfloat_1 + nfloat_2)
    elif operador == '-':
        print(nfloat_1 - nfloat_2)
    elif operador == '*':
        print(nfloat_1 * nfloat_2)
    elif operador == '/':
        print(nfloat_1 / nfloat_2)    

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        print('Obrigado por utilizar a calculadora, até a proxima!')
        break
