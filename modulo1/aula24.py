# Fatiamento de strings e a função len
"""
Fateamento [i:f:p] [::]
A função len retorna a qtd de caracteres da str 
o indice de caracteres começa no 0 e a contagem no 1
"""

variavel = 'Olá mundo'
print(variavel[4:]) # Ao deixarmos o f vazio sera percorrido até o final
print(variavel[:5])
print(variavel[4:8]) # O indice final não é incluido então colocamos 1+
print(len(variavel[3])) 
print(len(variavel))
print(variavel[0:9:2]) # o passo é a qntd de caracteres que sera pular
