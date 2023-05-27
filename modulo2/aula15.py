# Exemplo de uso do set
# exemplo de uso baseado no exercicio Palavra secreta, aqui estamos armazenando cada letra em um set

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra)

    if 'l' in letras:
        print('Parabéns')
        break

    print(letras)
