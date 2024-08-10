import random 

valor = random.randint(1,20)
print(valor)

print('Gerar cinco números aleatórios entre 1 e 50: \n')
for i in range(5):
    n = random.randint(1,50)
    print(f'Número gerado: {n}')

valor2 = random.random()
print(f'Número gerado: {round(valor2 * 10)}')

valor3 = random.uniform(1,100)
print(f'Número: {valor3}')

L = [1, 8, 7, 6, 9, 5, 4, 3, 2, 10]
n = random.choice(L)

print(f'Número escolhido: {n}')

n = random.sample(L,3)
print(f'Número escolhido: {n}')

# Embaralhar
print(f'Exibir a lista original: {L}')
print(f'Embaralhar a lista e exibi-lá: ')
n = random.shuffle(L)
print(L)
