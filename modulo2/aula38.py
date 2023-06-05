# Decoradores em Python (@syntax_sugar)
"""
 Decorar = Adicionar / Remover/ Restringir / Alterar
 Funções decoradoras são funções que decoram outras funções.
 Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.
 Decoradores são "Syntax Sugar"
"""

def criar_funcao(func): # Função decoradora
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            checar_string(arg)
        resultado = func(*args, **kwargs)
        print('Ok, você foi decorada')
        return resultado
    return interna

@criar_funcao # Aqui falamos que criar_funcao seja usada em inverte_string
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

def checar_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

invertida = inverte_string('123')
print(invertida)
