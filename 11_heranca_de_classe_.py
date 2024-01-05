class Animal:
    def __init__(self, nome):
        self.nome = nome


class Mamifero(Animal):
    def __init__(self, nome, cor_do_pelo):
        super().__init__(nome)
        self.cor_do_pelo = cor_do_pelo


# Testando o código
mamifero = Mamifero("Cachorro", "Marrom")
print(f"Nome: {mamifero.nome}, Cor do pelo: {mamifero.cor_do_pelo}")
