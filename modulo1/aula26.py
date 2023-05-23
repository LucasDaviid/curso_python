# Introdução ao try e except para capturar erros (exceptions)
"""
try -> tentar executar um código
except -> ocorreu algum erro ao tentar executar 
"""

numero_str = input('Vou dobrar o número digitado: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')
