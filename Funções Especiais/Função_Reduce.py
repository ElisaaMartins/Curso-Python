# Retorna o valor total da Função
# sintaxe: reduce(função, sequencia, valor_inicial)

from functools import reduce

def mult(x, y):
    return x * y

numeros = [1, 2, 3, 4, 5, 6, 7]
total = reduce(mult, numeros)
print(total)

# Soma cumulativa dos quadrados de valores, usando expressão lambda

numeros = [1, 2, 3, 4]
# ((1^2 + 2^2)^2 + 3^2)^2 + 4^2

total2 = reduce(lambda x, y: x**2 + y**2, numeros)
print(total2)