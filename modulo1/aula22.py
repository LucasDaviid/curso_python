# Interpolação de string com %

"""
s - string
d e i - int
f - float
x e X - hexadecimal
"""

nome = 'Lucas'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('o hexadecimal de %d é %08X' % (1500, 1500))