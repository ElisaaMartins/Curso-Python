# Simples, Composto, Encadeado

n1 = n2 = 0.0
media = 0.0

n1 = float(input('Digite a primeita nota: '))
n2 = float(input('Digite a segunda nota: '))

# Calcular a média aritmética das notas
media = (n1 + n2) / 2

if (media >= 7):
    print('Resultado: Aprovado!')
    print('Parabéns!')

print('Sua média é {}' .format(media))

