# Escopo global - criado fora da função e acessado de qualquer lugar
# Escopo local- criado dentro da função e acessado somente dentro da função

var_global = 'Curso completo de pyhton'

def escreve_texto():
    var_global = 'Banco de dados com SQL'
    var_local = 'Elisa Martins'
    print(f'Variável Global: {var_global}')
    print(f'Variável Local: {var_local}')

if __name__ == '__main__':
    print(f'Executar a função escreve_texto')
    escreve_texto()

    print('Tentar acessar as variáveis diretamente')
    print(f'Variável Global: {var_global}')
    # print(f'Variável Local: {var_local}') # não vai pq é local

