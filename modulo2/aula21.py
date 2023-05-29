# Mapeamento de dados em list comprehension 
produtos = [
    {'Nome': 'p1', 'preco': 20, },
    {'Nome': 'p2', 'preco': 10, },
    {'Nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} # Copiamos o que tinha no dicionário anterior, realizamos o desempacotamento e subimos o preço em 5%
    if produto['preco'] > 20 else {**produto} # Aplica o aumento em valores > 20
    # As 2 linhas acima são o mapeamento
    for produto in produtos
]

print(*novos_produtos, sep='\n')
