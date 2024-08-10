# Função que está dentro de uma variável
# Anonima
# sintaxe: lambda argumentos: expressão

quadrado = lambda x: x**2

for i in range(1,11):
    print(quadrado(i))

par = lambda x: x % 2 == 0
print(par(9))
