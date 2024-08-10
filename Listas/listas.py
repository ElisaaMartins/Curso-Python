# algumas funções em listas
# Sintaxe: nome_lista = [valores]

n1 = [1, 2, 3, 4, 5]
n2 = [6, 7, 8, 9, 10]
valores = n1 + n2

valores [0] = 9
print(valores[:4])

print(len(valores))

print(sorted(valores, reverse = True))

print(sum(valores))

valores.append(13)
print(valores)

valores.pop()
print(valores)

valores.pop(3)
print(valores)

valores.insert(3, 21)
print(valores)

print(17 in valores)

# for in em um lista
planetas = ['Mercúrio', 'Vênus', 'Marte', 'Saturno', 'Urano', 'Netuno']
for planeta in planetas:
    print(planeta)