# raise - lançando exceções (erros)
# raise ValueError('Deu erro') # Utilizamos raise para lançar um erro

def nao_aceito_zero(d):
    if d == 0:
       raise ZeroDivisionError('Não posso dividir por 0')
    return True

def deve_ser_int_ou_float(n): # Função para checagem de valores
    tipo_n = type(n) # Captura o tipo da variavel
    if not isinstance(n, (float, int)): # Define os valores aceitos como int ou float
        raise TypeError(
            f'"{n}" deve ser int ou float' # Caso seja um valor diferente retorna um TypeError com mensagem personalizada
            f'"{tipo_n}" enviado' # Informa qual o tipo enviado para variavel
            ) 
    return True

def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d) 
    return n / d


print(divide(8, '0'))

