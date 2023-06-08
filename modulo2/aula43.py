# count é um iterador sem fim (itertools)
from itertools import count

c1 = count(8, 8) # Aqui passamos o início e o step
r1 = range(8, 50, 8) # Aqui passamos o início fim e o step

# O count entrega o valor e soma +1

print('c1', hasattr(c1, '__iter__')) # Checando se o objeto é um interavel
print('c1', hasattr(c1, '__next__')) # Checando se o objeto é um iterator

print('r1', hasattr(r1, '__iter__')) 
print('r1', hasattr(r1, '__next__'))

print('\ncount')
for i in c1:
    if i > 50: # Para evitar o loop infinito
        break
    print(i)

print('\nrange')
for i in r1:
    print(i)