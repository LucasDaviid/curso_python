# Manipulando chaves e valores em dicionários em Python

pessoa = {} # criando o dict

# print(pessoa['nome'])  # Acessando a chave

# Criando e acessando dinamicamente
chave = 'nome'
pessoa[chave] = 'Lucas'

pessoa['sobrenome'] = 'David'

del pessoa['sobrenome'] # Apagando a chave
print(pessoa[chave])

# print(pessoa.get('sobrenome', 'Não existe'))
# .get tenta obter uma chave, retorna None se a chave não existir
#  mas podemos passar o valor de retonorno subistituindo None

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])
