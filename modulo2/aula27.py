# Introdução às Generator functions
# generator = (n for n in range(100))

def generator(n=0):
    yield 1 # Pausa a execução da função nesse valor
    print('Continuando...')
    yield 2
    print('Mais uma...')
    yield 3 
    print('Finalizando')
    return 'End' # Dentro de uma Generator function ao atingir return ele levanta uma StopIteration com o objeto colocado


gen = generator(n=0)
# print(next(gen)) # Chamando o next ele entrega o valor que foi armazenado na pausa
# print(next(gen))
# print(next(gen))
# print(next(gen)) # Aqui será levantada a StopInteration. Chamar next em algo que não possui próximo valor mesmo sem o return levantará a mesma exceção. 

# Dinamicamente
for n in gen:
    print(n)
    