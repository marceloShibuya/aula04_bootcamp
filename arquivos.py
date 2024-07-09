import csv

#caminho para o csv
caminho_do_arquivo: str = 'exemplos.csv'

#Inicializa uma lista vazia para armazenas os dados
arquivo_csv: list = []

with open(caminho_do_arquivo, mode='r',encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)



