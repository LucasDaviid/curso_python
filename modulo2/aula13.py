# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Qual a capital do Brasil?',
        'Opcoes': ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Goiânia'],
        'Resposta': 'Brasília'
    },
    {
        'Pergunta': 'Quanto é 7/2?',
        'Opcoes': ['3', '2.5', '7', '3.5'],
        'Resposta': '3.5'
    },
    {
        'Pergunta': 'Qual é o maior estado do Brasil?',
        'Opcoes': ['Bahia', 'Amazonas', 'São Paulo', 'Mato Grosso do Sul'],
        'Resposta': 'Amazonas'
    }
]

qts_acertos = 0 # Contador de acertos

for pergunta in perguntas:
    print('\nPergunta:', pergunta['Pergunta'], end='\n\n') # Acessando a chave pergunta
    
    opcoes = pergunta['Opcoes']
    for i, opcao in enumerate(opcoes): # i, enumerate retorna os indices da lista
        print(f'{i})', opcao, end='\n\n') # aqui exibimos o i (indice) e os valores

    escolha = input('Escolha uma opção: ') # Solicitando resposta

    acertou = False # Validação de acerto/erro
    escolha_int = None # Variável para armazenar a escolha pós-conversão para int
    qtd_opcoes = len(opcoes) # Quantidade de opções por pergunta

    if escolha.isdigit(): # Verifica se foi inserido um dígito  
        escolha_int = int(escolha) # Ser for dígito convertemos para int

    if escolha_int is not None: # Após escolha e verificação de dígito
        if escolha_int >= 1 and escolha_int < qtd_opcoes: # Validando se foi escolhida uma das opções disponiveis
            if opcoes[escolha_int] == pergunta['Resposta']: # Validando se a resposta escolhida é a correta
                acertou = True 

    if acertou: # Retorno da validação
        qts_acertos += 1
        print('Acertou🚀') #  Atalho para teclado de emoji no Windows = (windows + .)
    else:
        print('Errou❌')

print(f'Você acertou {qts_acertos} de {len(perguntas)} perguntas.')  # Informa a qtd de acertos ao final do quiz
