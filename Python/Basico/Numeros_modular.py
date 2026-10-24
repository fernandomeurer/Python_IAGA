def mostrar_numeros(n):
    # mostra os números de 1 até n em formato de conjunto
    print("{", end="")
    for i in range(1, n+1):
        print(f"{i}", end="")
        if i != n:
            print(end=", ")
    print("}")

def calcular_soma(n):
    # soma os números de 1 até n e retorna o resultado
    soma = 0
    for i in range(1, n+1):
        soma += i
    return soma

def resultados(n):
    # mostra os números de 1 até n e a soma desses números
    mostrar_numeros(n)
    print(f"Soma: {calcular_soma(n)}")
    print()

# modulo principal (main)
resultados(7)
resultados(10)

# Estrutura modularizada em 4 funções:
# 1. mostrar_numeros(n): mostra os números de 1 até n em formato de conjunto.
# 2. calcular_soma(n): soma os números de 1 até n e retorna o resultado.
# 3. resultados(n): mostra os números de 1 até n e a soma desses números.
# 4. A parte principal do código chama a função resultados() para os valores 7 e 10.