# groupby - agrupando valores (itertools)
# Em groupby os dados precisam estar ordenados para que ele possa agrupar corretamente
# Aqui eu quero que ele utilize a nota em si para gerar a chave e dentro da nota contenha o dicionário dos alunos que tiraram essa nota.
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
# alunos = ['a', 'a', 'a', 'b', 'c', 'a'] # Aqui tera 2 grupos de 'a', pois um deles não está ordenado
# grupos = groupby(sorted(alunos)) # Utilizamos sorted para ordenar a lista e resolver o problema acima.

# Ordenando pela nota
def ordena(aluno): # Criada função que ordena pela chave 'nota' para tratar a repetição de código.
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)