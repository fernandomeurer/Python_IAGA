def digaOla():
    print("Olá!!!")

def digaOlaPara(nome):
    print(f"Olá {nome}!!!")

def boasVindas(nome, sexo):
    if sexo == "M" or sexo == "m":
        print(f"Bem-vindo, {nome}!")
    elif sexo == "F" or sexo == "f":
        print(f"Bem-vinda, {nome}!")
    else:
        print(f"Bem-vindo(a), {nome}!")

# modulo principal (main)
digaOla()
print()

digaOlaPara("Alice")
digaOlaPara("Bob")
print()

boasVindas("Alice", "F")
boasVindas("Bob", "m")
boasVindas("Charlie", "O")