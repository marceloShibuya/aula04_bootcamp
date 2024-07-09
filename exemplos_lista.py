produto: str = "sapato"
produto_2: str = "camiseta"
produto_3: str = "videogame"

produtos: list = []

produtos.append(produto)
print(produtos)
produtos.append(produto_2)
print(produtos)
produtos.append(produto_3)
print(produtos)

#remover a última posição da lista
print("Exemplo de pop, removendo a última posição da lista")
produtos.pop()
print(produtos)
#remover o item desejado
print("Exemplo de remove, removendo o que deseja retirar da lista")
produtos.remove(produto)
print(produtos)

#exemplo de extend
print("Exemplo de extend")
numeros: list = []
numeros.extend(range(0,5))
print(numeros)


