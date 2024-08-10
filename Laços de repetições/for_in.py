# Sintaxe:
# for item in sequência:
#   instruções para cada item da sequencia

lista = [2, 6, 9, 4, 0, 12, 3, 7]

for item in lista:
    print(item)

# imprime letra por letra
palavra = 'Elisa'

for letra in palavra:
    print(letra)


# função range => faixa de numeros em que a repetição vai acontecer
# range (valor_inicial, valor_final, incrememto - de quanto em quanto)
for numero in range(1,11):
    print(numero)

nome = input('Digite seu nome: ')
for x in range(10):
    print(f'{x + 1} {nome}')

