# Proposta de 3 exercícios em 1
import copy
from aula34_dados import produtos

#  Aumente os preços dos produtos a seguir em 10%
#  Gere novos_produtos por deep copy (cópia profunda)

novos_produtos= [
    {**p, 'preco': round(p['preco'] * 1.1, 2)} # Recriamos a chave preço, subimos em 10% e round para 2 casas decimais
    for p in copy.deepcopy(produtos)
]

#  Ordene os produtos por nome decrescente (do maior para menor)
#  Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'], # Função recebe o produto e retorna o nome
    reverse=True
)

#  Ordene os produtos por preco crescente (do menor para maior)
#  Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'], # Função recebe o produto e retorna o preço
)

# Exibir

print(*produtos, sep='\n') 
print('\nPreço elevado em 10%:\n')
print(*novos_produtos, sep='\n')
print('\nProdutos ordenados por nome:\n')
print(*produtos_ordenados_por_nome, sep='\n')
print('\nProdutos ordenados por preço:\n')
print(*produtos_ordenados_por_preco, sep='\n')