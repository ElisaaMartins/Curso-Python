# manipulação de arquivos de tecto (txt)

manipulador = open('arquivo.txt', 'r', encoding='utf-8')

print(f'\Método read():\n')
print(manipulador.read())

print(f'\Método readline():\n')
print(manipulador.readline())
print(manipulador.readline())

print(f'\nMétodo redlines():\n')
print(manipulador.redlines())

texto = input('Qual termo deseja procurar no arquivo?')

try:
    manipulador = open('arquivo.txt', 'r', encoding='utf-8')
    for linha in manipulador:
        linha = linha.rstrip()
        if texto in linha:
            print(f'A string foi encontrada')
            print(linha)
        else:
            print(f'String não encontrada')
except IOError: 
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()