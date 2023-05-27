# Introdução ao tipo set em Python
"""
Sets - Conjuntos em Python (tipo set)
Representados graficamente pelo diagrama de Venn

Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

Sets são eficientes para remover valores duplicados de iteráveis.
 - Seus valores serão sempre únicos;
 - Não aceitam valores mutáveis;
 - não tem índexes;
 - NÃO GARANTEM ORDEM;
 - são iteráveis (for, in, not in)

# Métodos úteis:
 add, update, clear, discard

# Operadores úteis:
união | união (union) - Une
intersecção & (intersection) - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ - Itens que não estão em ambos
"""

# Criando um set / set(iterável) ou {1, 2, 3}
# s1 = set() -> Vazio
# s1 = set('Lucas', 1, 2, 3) -> Com dados

# s1 = {1, 2, 3, 3, 3, 1} # O set elimina valores duplicados 
# print(s1)

# Métodos úteis:
# s1 = set()
# s1.add('Lucas') # Adiciona um valor por vez
# s1.update(('Hello world', 1, 3, 7)) # Adiciona o valor de forma interada (letra por letra), aqui usamos uma tupla para mais de um valor
# s1.clear() # Limpa o set 
# s1.discard('Hello world') # Elimina um valor informado do seu set
# print(s1)

# # Operadores úteis:
# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# s3 = s1 | s2 # Unimos 2 set com o |
# s3 = s1 & s2 # Retorna os itens presentes nos 2 set
# s3 = s1 - s2 # Retorna apenas os itens do set a esquerda(s1)
# s3 = s1 ^ s2 # Retorna os itens que não estão em ambos os set
# print(s3)

