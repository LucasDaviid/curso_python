# List comprehension com mais de um for

lista = [] 
for x in range(3):
    for y in range(3):
       lista.append((x, y)) # Adicionamos uma tupla para colocar 2 valores por indice

lista = [ # Formado List comprehension
    (x, y) # Mapeamento sempre a Esquerda do for
    for x in range(3)
    for y in range(3)
]

print(lista)
