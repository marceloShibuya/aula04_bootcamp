 
import json


dicionario: list = []

produto_01 = {
    "nome": "sapato",
    "quantidade": 39,
    "preco": 10.38,
    "disponibilidade": True
}

produto_02 = {
    "nome": "camiseta",
    "quantidade": 15,
    "preco": 15.01,
    "disponibilidade": False
}

dicionario.append(produto_01)
dicionario.append(produto_02)
#print(dicionario)


#criando um arquivo json
print("Criando um arquivo JSON")
carrinho_compra = json.dumps(dicionario)
print(carrinho_compra)

