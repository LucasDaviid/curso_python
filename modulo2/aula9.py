#  Exercício com funções
"""
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.
"""

def multiplicador(multiplo):
    def multiplicar(numero):
        return numero * multiplo
    return multiplicar

duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
