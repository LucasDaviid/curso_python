# Operador lógico "not"
# Utilizado para inverter expressões 

senha = input('Senha: ')

if not senha:
    print('Você não inseriu uma senha')
elif senha == '12345':
    print('Entrou.')
else:
    print('Senha incorreta.')
