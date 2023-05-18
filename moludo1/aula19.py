# Operador Lógico "or"
# or - Qualquer condição verdadeira avalia toda expressão como verdadeira

entrada = input('Você quer [E]ntrar ou [S]air? ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
