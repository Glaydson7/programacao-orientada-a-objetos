class Animal:
    def __init__(self, especie, habitat):
        self.especie = especie
        self.habitat = habitat

    def exibir_informacoes(self):
        print(f"Espécie: {self.especie}")
        print(f"Habitat: {self.habitat}")


# Exemplo de uso
gato = Animal('Felis catus', 'Doméstico')
gato.exibir_informacoes()
