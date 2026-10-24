s= input("Digite uma string: ")

print()
print(s.upper()) #em maiúscula
print(s.lower()) #em minúscula
print("[" + s.center(40) + "]") 
print("[" + s.center(40, '*') + "]")

s = s.replace("A", "@") #substitui A por @
s = s.replace("a", "@") #substitui a por @
s = s.replace("Á", "@") #substitui Á por @
s = s.replace("á", "@") #substitui á por @
print(s)

print(s.split(" ")) #divide a string em uma lista de palavras
print(f"@ existe {s.count('@')} vezes") #conta quantas vezes o caracter @ aparece na string