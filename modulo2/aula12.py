# Métodos úteis dos dicionários 
"""
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
"""
pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'David'
}

# print(len(pessoa))

# print(pessoa.keys())
# print(tuple(pessoa.keys()))
# print(list(pessoa.keys()))

# print(pessoa.values())

# print(pessoa.items())
# for chave, valor in pessoa.items():
#     print(chave, valor)

# pessoa.setdefault('idade', 0)

# pessoa2 = pessoa.copy()
# Copia todos os valores imutaveis e linka os valores mutaveis
# import copy / deepcopy() faz a copia de tudo

# nome = pessoa.pop('nome') # Retorna o valor e elimina
# print(nome)
# print(pessoa)

# ultima_chave = pessoa.popitem()
# print(ultima_chave)
# print(pessoa)

# .update
# pessoa.update({ # Atualizando e criando chaves
#     'nome': 'Sei',
#     'idade': 23,
# })
# print(pessoa)

# pessoa.update(nome='Bia', idade=30) # Forma alternativa
# print(pessoa)

# tupla = ('nome', 'Guilherme'), ('idade', 37)
# pessoa.update(tupla)
# print(pessoa)

# pessoa.update((('nome', 'Guilherme'), ('idade', 37))) # Passando diretamente
