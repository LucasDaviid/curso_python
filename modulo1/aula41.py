# Imprecisão dos números de ponto flutuante + round e decimal.Decimal
"""
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal # contem dentro uma classe chamada Decimal

# numero_1 = 0.1
# numero_2 = 0.7
numero_1 = decimal.Decimal('0.1') #  E preciso passar o valor em string para o funcionamento correto. Usado para cálculos precisos
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2

print(numero_3)
print(f'{numero_3}:.2f') # Aqui indicamos a formatação ao final 
print(round(numero_3, 2)) # No round passamos - valor, qtd. casas decimais(arredondando elas)
