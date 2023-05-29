#  Generator expression e mais detalhes sobre Iterables e Iterators
"""
iterable - Tem a responsabilidade de deter os valores sequencialmente
iterator - A unica responsabilidade é te entregar um valor por vez (Só sabe o proximo valor e nada mais)
"""
import sys


iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__(retorna ele mesmo) e __next__(Retorna o prox. valor do iterable)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# Generator -> Basicamente é uma função que sabe pausar em determinada ocasião
# Todo generator é um iterator.
lista = [n for n in range(10000)]
generator = (n for n in range(100)) # generator expression

print(sys.getsizeof(lista)) # sys.getsizeof - retorna o tamanho da lista em bytes
print(sys.getsizeof(generator))

# print(next(generator)) 
# print(next(generator))
# print(next(generator))

for n in generator:
    print(n)

# A lista já salva os valores todos na memoria enquanto o generator espera a sua solicitação e retorna 1 valor por vez 

"""
Vantagens lista ->
Com ela já está inteira na memória podemos acessar índice por índice, acessar ultimo
elemento, saber o tamanho da lista, etc. 
Isso não ocorre com o generator, pois não possui tamanho, índice e outras características da lista
"""
