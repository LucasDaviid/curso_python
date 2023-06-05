# Variáveis livres + nonlocal
# funções locals e globals
# locals - informa quais variáveis são locais
def fora(x):
    a = x # Variável a é livre pois não está definida dentro do escopo da função dentro()

    def dentro():
        print(locals())
        return a
    return dentro

dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())
