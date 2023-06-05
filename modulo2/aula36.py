# Variáveis livres + nonlocal
def fora(x):
    a = x # Variavel a é livre pois não está definida dentro do escopo da função dentro()

    def dentro():
        return a
    return dentro

dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())
