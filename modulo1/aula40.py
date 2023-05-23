# Exercício - crie uma lista de compras com lista
"""
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de:
inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de índice inexistentes na lista.
"""
import os

lista = []
separador = '--' * 10
while True:
    print('\ni - Inserir \nl - Listar \na - Apagar \ns - sair')
    opcao = input('Selecione uma opção: ')

    if opcao == 'i':
        os.system('cls')
        item = input('Item: ')
        lista.append(item)
    
    elif opcao == 'l':
        os.system('cls')
        
        if len(lista) == 0:
            print('Sua lista está vazia!')
            
        for i, item in enumerate(lista):
            print(f'{i} - {item}')
        print(separador)
    
    elif opcao == 'a':
        os.system('cls')

        for i, item in enumerate(lista):
            print(f'{i} - {item}')          
        print(separador)

        indice_str = input('Informe o número do item que deseja apagar: ')
        
        try:
            indice = int(indice_str)
            del lista[indice]
            print('Item apagado!')
        except ValueError:
            print('Por favor digite apenas o número do produto em sua lista.')
        except IndexError:
            print('Item não existe em sua lista.')
        except Exception:
            print('Erro desconhecido')    

    elif opcao == 's':
        os.system('cls')
        print('Até a próxima!')
        break

    else:
        print('Opção inválida!\nPor favor, escolha entre i, a, l ou s.')    