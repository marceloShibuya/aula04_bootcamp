
# 1 - Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

# lista: list = list(range(1,11))

# for i in lista:
#     print(i ** 2)

# 2 - Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

# lista: list = ["Python", "Java", "C++", "JavaScript"]
# print(lista)
# lista.remove("C++")
# print(lista)
# lista.append("Ruby")

# print(lista)

# 3 - Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. 
# Imprima cada informação.

# from typing import Dict, Any

# dicionario = []

# infos: Dict[str, Any] = {
#     "titulo": "Harry Potter",
#     "autor": "J.K.Rowling",
#     "ano_pub": 1995
# }

# titulo = infos['titulo']
# autor = infos['autor']
# ano = infos["ano_pub"]

# print(f'O título do livro é {titulo}, autor {autor} e o ano de publicação foi em {ano}.')

# infos_elementos = infos.items()

# for i in infos_elementos:
#     print(i)


#Exemplo criando um dicionário com dicionário dentro

# lista_de_livros_usando_dict: dict = {
#     "livro_01": {
#         "titulo": "Game of Thrones",
#         "autor": "estagiario",
#         "ano_pub": 2001
#     },
#     "livro_02": {
#         "titulo": "Harry Potter",
#         "autor": "J.K.Rowling",
#         "ano_pub": 1995
#     }  
# }

# #print(lista_de_livros_usando_dict["livro_02"])
# print(lista_de_livros_usando_dict["livro_02"]["titulo"])


# 4- Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

# texto = "hoje e dia de estudar python e git"
# contagem = {}

# for i in texto:
#     if i in contagem:
#         contagem[i] += 1
#     else:
#         contagem[i] = 1

# print(contagem)


# 5 - Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, 
# calcule o preço total da lista de compras.

# lista = ["maçã", "banana", "cereja"] 
# dicionario = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

# total = sum(dicionario[i] for i in lista)

# print(total)


# Exercícios intermediários e mais avançados

# 6 - Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.

emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = list(set(emails))
print(emails_unicos)
