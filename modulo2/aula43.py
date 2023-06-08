# count é um iterador sem fim (itertools)
from itertools import count

c1 = count()
r1 = range(10)

# O count entrega o valor e soma +1

print('c1', hasattr(c1, '__iter__')) # Checando se o objeto é um interavel
print('c1', hasattr(c1, '__next__')) # Checando se o objeto é um iterator

print('r1', hasattr(r1, '__iter__')) 
print('r1', hasattr(r1, '__next__'))