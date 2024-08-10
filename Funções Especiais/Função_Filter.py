# sintaxe: filter(função, sequencia)

def numeros_pares(n):
    return n % 2 == 0

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

num_par = list(filter(numeros_pares,numeros))
print(num_par)

num_impar = list(filter(lambda x: x % 2 != 0, numeros))
print(num_impar)
