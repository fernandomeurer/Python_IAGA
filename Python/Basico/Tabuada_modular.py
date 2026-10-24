# modulo "tabuada"
# n é o parametro de entrada da função tabuada
def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    print()

#modulo principal (main)
tabuada(5)
tabuada(7)
tabuada(9)
tabuada(int(input("Digite um número para ver a tabuada: ")))