#   map, partial, GeneratorType e esgotamento de Iterators

from functools import partial # partial é uma funçao que retorna uma closure
from types import GeneratorType # Verifica se é um generator type

def print_inter(interator):
    print(*list(interator), sep='\n')
    print()


produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)

# novos_produtos = [
#     {**p,
#       'preco': aumentar_dez_porcento(p['preco'])}
#      for p in produtos
# ]

def alterar_preco_produtos(produto):
    return {**produto, 'preco': aumentar_dez_porcento(produto['preco'])}

novos_produtos = map( # Passa a função em cada um dos produtos
    alterar_preco_produtos, 
    produtos
)

# Como sabe se é um iterator ou um generator?
# novos_produtos = (x for x in produtos) - Esse é um generator
# todo generator é um iterator mas nem todo iterator é um generator

print(novos_produtos) # Retorna um map object
print(hasattr(novos_produtos, '__iter__'))
print(hasattr(novos_produtos, '__next__'))

# print(list(novos_produtos)) # esgota o interator do map

print_inter(produtos)
print_inter(novos_produtos)

print(isinstance(novos_produtos, GeneratorType)) # Retorna se é ou não um generator type

# Como fazer o mapeamento com os valores triplicados diretamente
print(
    list(map( # Convertemos em uma lista para não ocorrer esgotamento
        lambda x: x * 3, # Primeiro parâmetro  é sempre uma função
        [1, 2, 3, 4] 
    ))
)