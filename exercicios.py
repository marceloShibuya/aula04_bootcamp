# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. 
# Imprima cada informação.

from typing import Dict, Any

dicionario = []

infos: Dict[str, Any] = {
    "titulo": "Harry Potter",
    "autor": "J.K.Rowling",
    "ano_pub": 1995
}

# titulo = infos['titulo']
# autor = infos['autor']
# ano = infos["ano_pub"]

# print(f'O título do livro é {titulo}, autor {autor} e o ano de publicação foi em {ano}.')

infos_elementos = infos.items()

for i in infos_elementos:
    print(i)
