class Calculadora:
    def adicao(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Erro: Divisão por zero não é permitida"


calc = Calculadora()

print("Adição: 15 + 7 =", calc.adicao(15, 7))
print("Subtração: 15 - 7 =", calc.subtracao(15, 7))
print("Multiplicação: 15 * 7 =", calc.multiplicacao(15, 7))
print("Divisão: 15 / 7 =", calc.divisao(15, 7))
