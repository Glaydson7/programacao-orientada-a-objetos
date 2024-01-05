class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade


# Testando o código
pessoa = Pessoa("João", 25)
print(f"Nome: {pessoa.get_nome()}, Idade: {pessoa.get_idade()}")

pessoa.set_nome("Maria")
pessoa.set_idade(30)
print(f"Nome: {pessoa.get_nome()}, Idade: {pessoa.get_idade()}")
