# TYPE HINT

# idade: int = 39
# nome: str = "Marcelo"
# altura: float = 1.68
# is_estudante: bool = False

nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False

while nome_valido is False:
    try:
        nome: str = str(input("Digite o seu nome: "))
        if len(nome) == 0:
            print("O campo não pode estar vazio.")
        elif nome.isdigit():
            print("O campo não pode conter dígitos.")
        else:
            nome_valido = True
            print(f"Nome válido, {nome}!")
    except ValueError as e:
        print(e)
        exit()

