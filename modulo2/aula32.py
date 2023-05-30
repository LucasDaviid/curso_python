#  Módulos - import, from, as e *
#  https://docs.python.org/3/py-modindex.html

"""
inteiro - import nome_modulo
 Vantagens: você tem o namespace do módulo protegendo o que tiver dentro do módulo
 Desvantagens: nomes grandes
"""
# import sys
# platform = 'A MINHA'
# print(sys.platform) # Exibe o kernel do OS
# print(platform)

"""
partes - from nome_modulo import objeto1, objeto2
 Vantagens: nomes pequenos
 Desvantagens: Sem o namespace do módulo
"""
# from sys import exit, platform
# print(platform)

"""
alias 1 - import nome_modulo as apelido
É recomendado sempre mudar o nome da variável!
Utilizar somente em casos que não for possível alterar nomes de variável.
"""
# import sys as s # utilizando as damos um apelido ao sys
# sys = 'alguma coisa'
# print(s.platform)
# print(sys)

"""
alias 2 - from nome_modulo import objeto as apelido
"""
# from sys import exit as ex
# from sys import platform as pf

# print(pf)
"""
alias 1 e alias 2
 Vantagens: você pode reservar nomes para seu código
 Desvantagens: pode ficar fora do padrão da linguagem
"""

"""
Má prática - from nome_modulo import *
 Vantagens: importa tudo de um módulo
 Desvantagens: importa tudo de um módulo
"""
# from sys import *

# print(platform)
# exit()
