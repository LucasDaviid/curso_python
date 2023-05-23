# Introdução aos blocos de código + if / elif / else (condicionais)

entrada = input('Você quer "entrar", "suspender" ou "sair" do sistema? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'suspender':
    print('O sistema sera suspenso')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou entrar, suspender ou sair.')