# Introdução à List comprehension
# É uma forma rápida para criar listas a partir de interáveis.

# lista = []
# for numero in range(10):
#     lista.append(numero)

# abixo temos a mesma lista de cima usando à List comprehension
# lista = [numero for numero in range(10)] # A esquerda do for passamos o que queremos que seja incluido na lista

# lista = [1 for numero in range(10)] # Nesse caso ele ira incluir o numero 1 10x na lista

# Fazendo operações
lista = [numero * 2 for numero in range(10)] # Aqui multiplicamos cada número(0-9) da lista e multplicando por 2
print(lista)
