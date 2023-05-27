# Introdução à função lambda + list.sort e sorted
"""
 A função lambda é uma função como qualquer outra em Python.
 Porém, são funções anônimas que contém apenas uma linha.
 Ou seja, tudo deve ser contido dentro de uma única expressão.

 O Python utiliza a tabela unicode para fazer a ordenação por letra

"""
# list.sort e sorted

# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True) # .sort() ordena a lista original, (reverse=True) altera a ordem para decrescente
# # sorted(lista) -> cria uma nova lista ordenada com uma copia rasa da sua lista original
# print(lista)

 
lista = [ 
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
] 

# def ordena(item): # Função criada para ordenar a lista.
#     return item['nome'] # Aqui passamos o parâmetro de ordenação.

# lista.sort(key=ordena) # Aqui passamos a definição da função que sera usada junto ao sort para ordenar a lista.

# lista.sort(key=lambda item: item['nome'])  # Criada a mesma função acima só que agora utilizando lambda

def exibir(lista): # Função para exibir a lista
    for item in lista:
        print(item)
    print()

# Utilizando sorted com lambda
l1 = sorted(lista, key=lambda item: item['nome']) # Como primeiro parametro informamos a lista que queremos ordenar
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
