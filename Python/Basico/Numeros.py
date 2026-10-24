# Arquivo de modulos ou biblioteca de funções com 3 funções:
# 1. mostrar_numeros(n): mostra os números de 1 até n em formato de conjunto.
# 2. calcular_soma(n): soma os números de 1 até n e retorna o resultado.
# 3. resultados(n): mostra os números de 1 até n e a soma desses números.

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