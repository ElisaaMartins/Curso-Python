# Dicionários

elemento = {
    'Z':  3,
    'nome': 'Litio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(f'Elemento: {elemento['nome']}')
print(f'Densidade: {elemento['densidade']}')
print(f'O dicionário possui: {len(elemento)} elementos')

# Atualizar uma entrada
elemento ['grupo'] = 'Alcalinos' 
print(elemento)

# Adicionar uma entrada 
elemento ['periodo'] = 1 
print(elemento)

# Exclusão de itens em dicionários
del elemento['periodo']
print(elemento)

elemento.clear()
print(elemento)

# vai excluir mesmo a variavel
""" del elemento
print(elemento) """

print(elemento.items())
for i in elemento.items():
    print(i)

print(elemento.keys())
for i in elemento.keys():
    print(i)

for i, j in elemento.items():
    print(f'{i}: {j}')

    