# yield from em generator functions

def gen1():
    print('Começou gen1')
    yield 1
    yield 2
    yield 3
    print('Acabou gen1')

def gen2():
    print('Começou gen2')
    yield from gen1() # Retorna os dados do generator 1
    yield 4
    yield 5
    yield 6
    print('Acabou gen2')

g = gen2()
for numero in g:
    print(numero)