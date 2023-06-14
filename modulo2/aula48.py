#  reduce - faz a redução de um iterável em um valor
"""
Podemos utilizar o reduce sem valor inicial inicial, mas gera transtornos.

Quando passamos o valor inicial o Produto 5 sera o primeiro produto,
se o valor inicial não for passado o Produto 5 sera o acumulador
e o Produto 1 será o primeiro produto.  
"""

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]
# def funcao_do_reduce(acumulador, produto): # Essa função recebe um acumulador e o produto
#     print('Acumulador', acumulador)
#     print('Produto', produto)
#     print()
#     return acumulador + produto['preco']

total = reduce(
    lambda ac, p: ac + p['preco'], # Passamos a função do reduce
    produtos, # Iteravel
    0  # Valor inicial
)

print('Total é', total)

# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)

# print(sum([p['preco'] for p in produtos])) # Utilizando a função sum em uma list comprehension obtemos o mesmo resultado do for acima