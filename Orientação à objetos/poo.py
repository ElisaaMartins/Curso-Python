# Python é multipardigma
# O rientação a objetos: Paradigma de programação
# Classes e Objetos

class veiculo:
    def movimentar(self):
        print(f'Sou um veículo e me desloco!')

    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo
        self.num_registro = None

    # Setter
    def set_num_registro(self, registro):
        self.num_registro = registro

    # Getter
    def get_fabr_modelo(self):
        print(f'Modelo: {self.modelo}, Fabricante: {self.fabricante}.\n')

    def get_num_registro(self):
        return self.num_registro

# HERANÇA
class carro(veiculo):
    # metodo __init__ será herdado
    def movimentar(self):
        print(f'Sou um carro e ando pelas ruas!')

class motocicleta(veiculo):
    def movimentar(self):
        print(f'Corro muito')

class aviao(veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante, modelo)

    def get_categoria(self):
        return self.__cat

# ENCAPSULAMENTO
if __name__ == '__main__':
    meu_veiculo = veiculo('GM', 'Cadilac Escalde')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabr_modelo()
    meu_veiculo.set_num_registro(490321-1)
    print(meu_veiculo.fabricante)
    print(f'Registro: {meu_veiculo.get_num_registro()}\n')

    meu_carro = carro('Volkswagem', 'Polo')
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()
    
    moto = motocicleta('Harley Davison', 'Nightster Specioal')
    moto.movimentar()
    moto.get_fabr_modelo()

    meu_aviao = aviao('Boeing', '747', 'Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fabr_modelo()
    print(f'Categoria: {meu_aviao.get_categoria()}')

