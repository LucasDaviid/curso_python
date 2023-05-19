# Formatação de strings com f-strings
"""
s - string
d - int
f - float
<número de digitos>f
x ou X - hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
= - Força o número a aparecer antes do zero
sinal + ou -
Ex: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = "ABC"
print(f'{variavel}')
print(f'{variavel: >10}') # preenche com espaços a esquerda até atingir 10 caracteres totais
print(f'{variavel: <10}.')
print(f'{variavel: ^10}')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
