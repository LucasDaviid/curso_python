# Operador Lógico "and"
# and - Todas as condições precisam ser verdadeiras

entrada = input('Você quer "entrar" ou "sair"? ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == "entrar" and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')