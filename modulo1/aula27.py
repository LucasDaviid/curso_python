# Exercícios:

"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro
"""
# numero_str = input('Digite um número: ')

# if numero_str.isnumeric():
#     numero = int(numero_str)
#     divisao = (numero%2)

#     if divisao == 0:
#         print(f'o número {numero} é par.')
#     else:
#         print(f'o número {numero} é impar.')   
 
# else:
#     print('Você não digitou um número inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e baseado nela exiba a saudação apropriada
Ex: 0-11 bom dia, 12-17 boa tarde e 18-23 boa noite
"""
# hora_str =  input('Informe apenas a hora: ')

# try:
#     hora = int(hora_str)

#     if hora >=0 and hora <= 11:
#         print('Bom dia!')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde!')
#     elif hora >= 18 and hora <=23:
#         print('Boa noite!')
#     else:
#         print('Horário inválido')
# except:
#     print('Digite apenas números inteiros')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# nome = input('Digite seu primeiro nome: ')
# letras = len(nome)

# if letras > 1:
#     if letras <= 4:
#         print('Seu nome é curto')
#     elif letras >= 5 and letras <= 6:
#         print('Seu nome é normal')
#     else:
#         print('Seu nome é muito grande')
# else:
#     print('Digite mais de uma letra')
