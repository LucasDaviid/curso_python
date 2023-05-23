#  Introdução ao empacotamento, desempacotamento e tuplas
"""
Tipo tupla - Uma lista imutável
"""

nomes = ['Lucas', 'Ana', 'David']
# nomes = 'Lucas', 'Ana', 'David' - tupla
_, nome2, *_ = nomes
print(nome2, _)