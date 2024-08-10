# Uma função que aplica funções
#  sintaxe: map(função, iterável)

num = [1,2,3,4,5,6,7,8,9,10]
dobro = list(map(lambda x: x * 2, num))
print(dobro)

palavras = ['Pyhton', 'é', 'uma', 'linguagem', 'de', 'programação']
maiusculas = list(map(str.upper, palavras))
print(maiusculas)