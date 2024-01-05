class Aluno:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self):
        return round(sum(self.notas) / len(self.notas), 2)


aluno1 = Aluno("João", 20, [7.5, 8.0, 9.0])
media = aluno1.calcular_media()
print(f"A média das notas do {aluno1.nome} é {media}")
