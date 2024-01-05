class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def exibir_informacoes(self):
        print(f"\nNome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Cidade: {self.cidade}")


nome = input("\nDigite o seu nome: ")
idade = int(input("\nDigite a sua idade: "))
cidade = input("\nDigite a sua cidade: ")

pessoa = Pessoa(nome, idade, cidade)
pessoa.exibir_informacoes()
