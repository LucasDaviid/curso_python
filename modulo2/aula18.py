#  Funções lambda complexas (para entendimento)
#  Refatorando as funções para lambda

# 1
def executa(funcao, *args): # Recebe uma função e argumentos não nomeados
    return funcao(*args) # Retorna a função executada

# funcao = lambda parametro: parametro # não recomendado / Má prática
# A pep8 diz para criarmos uma função para execução e não uma lambda

# 2
# def soma(x, y):
#     return(x + y)

# print(
#     executa(
#         lambda x, y: x + y
#     )
# )

# 3
# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

# duplica = executa(
#     lambda m: lambda n: n * m
#     2 # Nesse caso temos que passar o primeiro parametro por ser um função que retorna outra função
#     )