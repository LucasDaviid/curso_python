# Usando a função input para coletar dados do usuário

"""
nome = input('Qual seu nome? ')
print(f'Seu nome é {nome}')
"""

numero_1 = input('Digite um número: ') # Aqui a variável é str
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1) # Fazemos a conversão da variável para int
int_numero_2 = int(numero_2) 

print(f'A soma dos números é = {int_numero_1 + int_numero_2}')