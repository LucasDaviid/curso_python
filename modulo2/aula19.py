# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}
# a, b = pessoa # Desempacota as chaves (nome / sobrenome) 
# a, b = pessoa.items() # Desempacota em tuplas a chave e o valor ('nome', 'Aline)
# a, b = pessoa.values() # Desempacota os valores (Aline / Souza)
# (a1, a2), (b1, b2) = pessoa.items() # Desempacotamento interno

dados_pessoa = {
    'idade': 16,
    'altura': 1.87,
}

pessoa_completa = {**pessoa, **dados_pessoa} # Desempacotamos os dicionários acima em um novo dicionário
# print(pessoa_completa)


# args e kwargs
# kwargs -- keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs): # Função para exibir argumentos
    print('NÂO NOMEADOS:', args) 

    for chave, valor in kwargs.items(): 
        print(chave, valor)

# mostro_argumentos_nomeados(1, 2, nome='Marcelo', qlq=123)    
mostro_argumentos_nomeados(**pessoa_completa) # Desempacotando  chamada de função passando os argumentos



