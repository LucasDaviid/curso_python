# groupby - agrupando valores (itertools)
# Em groupby os dados precisam estar ordenados para que ele possa agrupar corretamente
# 
from itertools import groupby

alunos = [
    {'nome': 'Lucas', 'nota': 'A'},
    {'nome': 'Sei', 'nota': 'B'},
    {'nome': 'Bia', 'nota': 'A'},
    {'nome': 'Pedro', 'nota': 'C'},
    {'nome': 'Matheus', 'nota': 'D'},
    {'nome': 'Ciel', 'nota': 'A'},
    {'nome': 'Nara', 'nota': 'B'},
    {'nome': 'Igor', 'nota': 'A'},
    {'nome': 'Stephany', 'nota': 'C'},
]

# Exemplificação de funcionamento
alunos = ['a', 'a', 'a', 'b', 'c', 'a'] # Aqui tera 2 grupos de 'a', pois um deles não está ordenado
grupos = groupby(sorted(alunos)) # Utilizamos sorted para ordenar a lista e resolver o problema acima.

for chave, grupo in grupos:
    print(chave)
    print(list(grupo))