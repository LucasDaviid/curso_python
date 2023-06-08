#  Combinations, Permutations e Product - Itertools
"""
 Combinations - Ordem não importa - iterável + tamanho do grupo
 Permutations - Ordem importa
 Product - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = ['João', 'Joana', 'Luiz', 'Letícia',]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g', 'xg'],
    ['masculino', 'feminino'],
    ['algodão', 'poliéster'],
]

# print_iter(combinations(pessoas, 2)) 
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas)) 

