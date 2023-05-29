# Filtro de dados em list comprehension (filter)
import pprint

def p(v): pprint.pprint(v, sort_dicts=False, width=40) 
# Função que recebe o import pprint configurado para naão ordenar chaves(sort_dicts) e largura de linha maxima de 40 caracteres (width=40)

produtos = [
    {'Nome': 'p1', 'preco': 20, },
    {'Nome': 'p2', 'preco': 10, },
    {'Nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(*novos_produtos, sep='\n')
# p(novos_produtos)

# lista = [n for n in range(10) if n < 5] # Aqui o filtro inclui o número se a condição for true

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10 # Filtro para inclusão se o preçõ for > 10
]
p(novos_produtos)
