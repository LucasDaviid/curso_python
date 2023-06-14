# filter é um filtro funcional

def print_inter(iterador):
    print(*list(iterador), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def filtrar_preco(p): 
    return p['preco'] > 20

# novos_produtos = [  # Filtrando com list comprehension
#     p for p in produtos
#     if p['preco'] > 20
# ]

novos_produtos = filter(
    # lambda p: p['preco'] > 20,
    filtrar_preco,
    produtos
)

print_inter(produtos)
print_inter(novos_produtos)
