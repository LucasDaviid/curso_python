# Exercício - Gerar o segundo dígito de um CPF
"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

# Primeiro dígito
cpf_enviado = '74682489070'
nove_digitos = cpf_enviado[:9]
contador_regressivo_1 = 10
resultado_dig_1 = 0

for digito in nove_digitos:
    resultado_dig_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

dig_1 = (resultado_dig_1 * 10) % 11
dig_1 = 0 if dig_1 > 9 else dig_1


# Segundo dígito
dez_digitos = nove_digitos + str(dig_1)
contador_regressivo_2 = 11
resultado_dig_2 = 0

for digito in dez_digitos:
    resultado_dig_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

dig_2 = (resultado_dig_2 * 10) % 11
dig_2 = 0 if dig_2 > 9 else dig_2

# Validação
cpf_gerado = f'{nove_digitos}{dig_1}{dig_2}'

if cpf_enviado == cpf_gerado:
    print(f'{cpf_enviado} é válido')
else:
    print('CPF inválido')

