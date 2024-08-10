# Uma lista pode derivar de outra lista -> de forma concisa
# Sintaxe: [expressão for item in lista]
# expressão é o que será avaliado paracada elemento em 'lista'
# item é a varivável que representa cada elemento na lista 

numeros = [1,2,8,52,98,10]

quadrados = [num ** 2 for num in numeros]
print(quadrados)

frase = "A lógica é apenas o principío da sabedoria, e não o seu fim"
vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í','ó','ú']

lista_vogais = [v for v in frase if v in vogais]
print(f'A frase possui {len(lista_vogais)} vogais:')
print(lista_vogais)

