from random import randint

jogo = []

i = 1
while i <= 6:
    numero = randint(1, 60)
    if numero not in jogo:
        jogo.append(numero)
        i += 1

print("Números do jogo:", sorted(jogo))