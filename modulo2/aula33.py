# Modularização - Entendendo os seus próprios módulos e sys.path no Python
"""
O primeiro módulo executado chama-se __main__ os demais tem seus próprios nomes.
Você pode importar outro módulo inteiro ou parte do módulo.
O python conhece a pasta onde o __main__ está e as pastas abaixo dele.
Ele não reconhece pastas e módulos acima do __main__ por padrão.
O python conhece todos os módulos e pacotes presentes nos caminhos de sys.path.
"""
import sys

# print('Este módulo se chama', __name__)

print(*sys.path, sep='\n') # Exibe a lista dos caminhos de sys

