# Exercício
"""
Peça ao usuário para digitar seu nome e idade
se nome e idade forem digitados exiba:
    Seu nome é {nome}
    Seu nome invertido é {nome_invertido}
    Seu nome contem (ou não) espaços
    Seu nome tem {x} letras
    A primeira letra do seu nome é {inicial}
    A última letra do seu nome é {final}
Se nada for digitado em nome ou idade exiba:
    "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade :
    print(f'Seu nome é - {nome}')
    print(f'Sua idade é - {idade}')
    print(f'Seu nome invertido é - {nome[::-1]}')
    
    if ' ' in nome:
        print("Seu nome contém espaços!")
    else:
        print('Seu nome não contém espaços')
    
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é - {nome[0]}')
    print(f'A última letra do seu nome é - {nome[-1]}')
    
else:
    print('Desculpe, você deixou campos vazios.')
