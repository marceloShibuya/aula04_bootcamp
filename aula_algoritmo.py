
# Função de ordenação personalizada

lista = [64, 34, 25, 12, 22, 11, 90]
lista_nova = []

for i in range(len(lista)):
    print(i)
    for j in range(i+1, len(lista)):
         print(j)
         if lista[i] > lista[j]:
             lista_nova = lista[j], lista[i]

print(lista_nova)
