# Sintaxe: 
# print(objetos, argumentos)

mensagem = 'Função print()'
print(mensagem)


nome = input('Digite seu nome: ')
print('Olá ' + nome + '! Bem-vindo ao curso de Python!')

nome = 'Maria'
idade = 30
msg_formatada = 'O nome dela é {0} e ela tem {1} anos' .format(nome, idade)
print(msg_formatada)

nome = 'Janice'
peso = 79.90
msg = f'Olá, meu nome é {nome} e eu peso {peso} quilos.'
print(msg)

valor = 1225.573637
print(f'O valor é {valor:.2f}')
print(f'O valor é \'{valor:.2f}\'')

nome = 'João'
idade = 32
print(f'Nome: {nome}\tIdade: {idade}')

