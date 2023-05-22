# split, join e strip - Métodos da str
"""
split - divide uma string / list
join - une uma string
strip - corta espaços do começo e do fim da str
    rstrip - espaços direita
    lstrip - espaços esquerda
"""

frase = '  Olha só que  ,   coisa interessante  '
lista_frase_inicial = frase.split(',') # Quando vazio divide as palavras nos espaços em branco

lista_frase = []
for i, frase in enumerate(lista_frase_inicial):
    lista_frase.append(lista_frase_inicial[i].strip())

# print(lista_frase_inicial)
# print(lista_frase)

frases_unidas = '-'.join(lista_frase)
print(frases_unidas)