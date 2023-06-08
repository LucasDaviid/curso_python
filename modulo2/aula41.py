# Exercício - Unir listas
"""
Crie uma função zipper (como o zipper de roupas)
 O trabalho dessa função será unir duas listas na ordem.
Use todos os valores da menor lista.
 Ex.:
 ['Salvador', 'Ubatuba', 'Belo Horizonte']
 ['BA', 'SP', 'MG', 'RJ']
 Resultado
 [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
 """
from itertools import zip_longest
# def zipper(lista1,lista2):
#     intervalo_maximo = min(len(lista1), len(lista2))
#     return [(lista1[i], lista2[i]) for i in range(intervalo_maximo)]


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2)))     # A função zip faz a mesma coisa mas retorna um interaitor.
# Para visualizar o interaitor podemos consumi-lo com uma list ou usar um for.
print(list(zip_longest(l1, l2)))  # Faz o mesmo que zip só que invertido, utilizando o valor da maior list .