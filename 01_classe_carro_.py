
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def exibir_informacoes(self):
        print(f"Modelo: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}")


carro_exemplo = Carro("Fusca", "Azul", 2020)
carro_exemplo.exibir_informacoes()
