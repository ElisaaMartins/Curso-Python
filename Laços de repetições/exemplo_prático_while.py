nome = None

while True:
    print('Digite seu nome, ou x para parar: ' )
    nome = input()
    if nome == 'x' or nome == 'X':
        break # para o laço
    print(f'Bem-vindo, {nome}')

print('Até logo')
