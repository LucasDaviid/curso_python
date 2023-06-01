# Proposta de 3 exercícios em 1
import copy
from aula34_dados import produtos
"""
 Ordene os produtos por nome decrescente (do maior para menor)
 Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

 Ordene os produtos por preco crescente (do menor para maior)
 Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
"""
#  Aumente os preços dos produtos a seguir em 10%
#  Gere novos_produtos por deep copy (cópia profunda)


novos_produtos= [
    {**p, 'preco': round(p['preco'] * 1.1, 2)} # Recriamos a chave preço, subimos em 10% e round para 2 casas decimais
    for p in copy.deepcopy(produtos)
]

print(*produtos, sep='\n') 
print()
print(*novos_produtos, sep='\n')



