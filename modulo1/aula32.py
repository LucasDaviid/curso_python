# while / else (recurso específico do Python)
# quando o break é utilizado o else não é executado

string = input('Digite algo: ')

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('a string não contém espaço.')

print('Fora do while')