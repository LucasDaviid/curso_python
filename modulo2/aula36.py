# Variáveis livres + nonlocal
# funções locals e globals
# locals - informa quais variáveis são locais
# globals - informa as variáveis globais definidas

def fora(x):
    a = x # Variável a é livre pois não está definida dentro do escopo da função dentro()

    def dentro():
        # print(locals())
        # print(dentro.__code__.co_freevars) # Podemos ver as variáveis livres com essa linha de cod.
        return a
    return dentro

dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())
