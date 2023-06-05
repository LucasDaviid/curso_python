# Funções decoradoras em geral
"""
 Decorar = Adicionar / Remover/ Restringir / Alterar
 Funções decoradoras são funções que decoram outras funções.
 Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.
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

def inverte_string(string):
    return string[::-1]

def checar_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

checagem_parametro = criar_funcao(inverte_string)
invertida = checagem_parametro('123')
print(invertida)
