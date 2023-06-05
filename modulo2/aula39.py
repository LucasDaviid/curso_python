# Decoradores com parâmetros
def fabrica_de_decoradores(a=None, b=None, c=None): # Passamos parâmetros para o decorador utilizando um recurso da linguagem que é o escopo de uma nova função
    def fabrica_de_funcoes(func): # Decorador em python tem que receber uma função
        print('Decoradora 1')
    
        def aninhada(*args, **kwargs): # Função aninhada recebe o que quisermos.
            print('Parâmetros do decorador, ', a, b ,c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes
 
@fabrica_de_decoradores(1, 2, 3)
def soma(x, y): # A função aninhada mais interna ira subistituir a função real
    return x + y

multiplica = fabrica_de_decoradores()(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)
