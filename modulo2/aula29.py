# try e except para tratar exceções

try:
    a = 18
    b = 0 
    # print(b[0]) # TypeError
    print('Linha 1'[1000]) # IndexError
    c = a / b # ZeroDivisionError
    # Ao ir para o except devido ao erro e as linhas abaixo são ignoradas
    print('Linha 2')
except ZeroDivisionError: # Aqui passamos a exceção que estamos tratando. Caso ocorra outro tipo de exceção ele ira mostrar ao executar.
    print('Dividiu por 0')
except NameError:
    print('Nome b não está definido')
    # Podemos utilizar uma tupla para passar mais de uma exceção
except (TypeError, IndexError) as error: # Aqui informamos os tipos de erro que podem ocorrer e utilizando 'as' jogamos a instancia do erro dentro de uma variavel.
    print('TypeError ou IndexError')
    print('MSG ->', error) # Ao printar a var. de erro ela exibe apenas a mensagem do erro.
    print('Erro ->', error.__class__.__name__)  # Aqui estamos pegando o nome do erro que está na var.   
except Exception: # Exception é a classe de erro superior, que representa todos os erros de pyton. 
    print('ERRO DESCONHECIDO')    

print('Continuar')
