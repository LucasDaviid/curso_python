# while, break, operadores de atribuição e continue
"""
while (enquanto) -> Executa uma ação enquanto uma condição for verdadeira
break -> Finaliza o while forçadamente
Operadores de atribuição -> =, +=, -=, *=, /=, //=, **=, %= 
continue -> retorna ao começo do while
"""
contador = 0

while contador <= 20:
    contador += 1

    if contador == 7:
        print('Não vou mostrar o 7')
        continue
    
    print(contador)

    if contador == 15:
        break

print('Acabou')