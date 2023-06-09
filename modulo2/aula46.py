#   map, partial, GeneratorType e esgotamento de Iterators
from functools import partial # partial é uma funçao que retorna uma closure

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

novos_produtos = [
    {**p, 'preco': aumentar_dez_porcento(p['preco'])} for p in produtos
]

print_inter(produtos)
print_inter(novos_produtos)