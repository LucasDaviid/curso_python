#  try, except, else e finally + Built-in Exceptions
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__) # Exibe o nome do erro
    print(e) # Exibe a mensagem do erro
    print('DIVIDIU ZERO')
except IndexError as error:  # Captura o erro com as e uma variavel
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')