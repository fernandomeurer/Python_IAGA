n = int(input("Tamanho da lista: "))

print()

soma = 0
l = []
for i in range(n):
    item = int(input(f"Digite o {i + 1}º elemento da lista: "))

    soma = soma + item
    l.append(item)

print()
#1ª forma de imprimir a lista
print(l, "soma = ", soma)

#2ª forma de imprimir a lista
for item in l:
    print(f"{item}", end=", ")
print("soma = ", soma)

#3ª forma de imprimir a lista
print("[", end="")
for i in range(n):
    print(f"{l[i]}", end="")
    if (i != (n - 1)):
        print(", ", end="")
print("] soma = ", soma)
