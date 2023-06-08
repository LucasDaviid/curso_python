#  Combinations, Permutations e Product - Itertools
"""
 Combinations - Ordem não importa - iterável + tamanho do grupo
 Permutations - Ordem importa
 Product - Ordem importa e repete valores únicos
"""
from itertools import combinations

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = ['João', 'Joana', 'Luiz', 'Letícia',]
camisetas = [['preta', 'branca'],]

print_iter(combinations(pessoas, 2)) # Combinação das pessoas em grupos de 2