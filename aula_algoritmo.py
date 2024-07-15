
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

def ordernar_lista(lista: list) -> list:
    lista_ordenada = lista.copy()

    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

    return lista_ordenada



