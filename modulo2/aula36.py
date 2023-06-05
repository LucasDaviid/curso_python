# Variáveis livres + nonlocal
"""
 Funções locals e globals
 locals - informa quais variáveis são locais
 globals - informa as variáveis globais definidas
"""

# def fora(x):
#     a = x # Variável a é livre pois não está definida dentro do escopo da função dentro()

#     def dentro():
#         # print(locals())
#         # print(dentro.__code__.co_freevars) # Podemos ver as variáveis livres com essa linha de cod.
#         return a
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial
    
    def interna(valor_a_concatenar=''):
        nonlocal valor_final # Agora o Pyton ira buscar acima o valor da variável e o erro não ocorrera.  
        valor_final += valor_a_concatenar # Vai gerar um UnboundLocalError. Precisamos informar que a variável não é local
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)