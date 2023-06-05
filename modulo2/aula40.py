# Ordem dos decoradores

def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}' # Convertido o resultado da func de int/float para string passando uma fstring e concatenamos o nome do decorador
            return final
        return sua_nova_funcao
    return decorador

@parametros_decorador(nome='segundo')
@parametros_decorador(nome='primeiro') # A ordem de aplicação dos decoradores é debaixo para cima
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)