# Introdução ao tipo de dados dict - Dicionários em Python
"""
Dicionários são estruturas de dados do tipo
par de "chave" e "valor".
Chaves podem ser consideradas como o "índice" 
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionário.
Usamos as chaves - {} - ou a classe dict para criar dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
"""

pessoa = { # Criando a classe
    'nome': 'Lucas',
    'sobrenome': 'David',
    'idade': 25,
    'altura': 1.76,
    'endereços': [ # Lista contem um dict
        {'rua': 'Aguas da Prata', 'numero': 666}
    ] 
} 

# Outra forma de se declarar porém pouco usada
# pessoa = dict(nome= 'Lucas', sobrenome= 'David)

print(pessoa['nome'])

for chave in pessoa:
    print(chave, '-', pessoa[chave])
