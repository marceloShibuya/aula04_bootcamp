
# Função de ordenação personalizada simples

# lista = [64, 34, 25, 12, 22, 11, 90]

# for i in range(len(lista)):
#     print(i)
#     for j in range(i+1, len(lista)):
#          print(j)
#          if lista[i] > lista[j]:
#              lista[i], lista[j] = lista[j], lista[i]

# print(lista)


# Criando uma API

lista = [64, 34, 25, 12, 22, 11, 90]

def ordernar_lista(lista: list) -> list:
    lista_ordenada = lista.copy()

    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

    return lista_ordenada

print(lista)

lista_1 = [80,3312,5,9,18,27,34,100,101]
print(ordernar_lista(lista_1))
