# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio',
}

dc = { # Dictionary Comprehension
    chave: valor.upper()
    if isinstance(valor, str) else valor # isinstance - verifica se algo é de determinado tipo
    for chave, valor in produto.items()
}

# print(dc)

s1 = {i for i in range(10)} # Set Comprehension
