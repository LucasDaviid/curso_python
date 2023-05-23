# Uma introdução às f-strings

nome = 'Lucas David'
altura = 1.76
peso = 70
imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura'  # com o f no inicio da linha podemos inserir variaveis entre {chaves}. 
linha_2 = f'pesa {peso:.1f}Kg e seu IMC é {imc:.2f}' # : é utilizado para formatar as casas decimais

print(linha_1, linha_2)