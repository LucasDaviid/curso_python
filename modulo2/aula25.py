# dir, hasattr e getattr
# dir -> trás todos os atributos definido dentro de sua string, utilizado no debuger

string = 'Lucas'
metodo = 'upper' # Metodo informado na variavel para ser chamado dinamicamente

# hasattr -> verifica se determinado objeto tem determinado nome dentro dele
if hasattr(string, 'upper'): # Aqui estamos verificando se a string tem o metodo upper. Passamos o nome do metodo como string('upper')
    print('Existe upper')
    print(string.upper())

# getattr -> Verifica se o metodo existe dentro da string, caso exista o mesmo é executado.
if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)