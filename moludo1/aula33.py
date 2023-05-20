# Exercício - conta letras 

frase = 'O Python é uma lignguagem de programação multiparadigma. ' \
    'Python foi criado por Guido Van Rossum.'

i = 0
qtd_aparicao = 0
letra_maior_aparicao = ''

while i < len(frase): # Cada loop feito é chamado de iteração
    letra_atual = frase[i]
    atual_aparicao_qtd = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue
    
    if qtd_aparicao < atual_aparicao_qtd:
        qtd_aparicao = atual_aparicao_qtd
        letra_maior_aparicao = letra_atual
    
    i += 1

print(f'A letra que apareceu mais vezes foi "{letra_maior_aparicao}" que apareceu {qtd_aparicao}x.')