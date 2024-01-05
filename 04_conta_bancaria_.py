class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito realizado com sucesso! Seu saldo atual é: {
              self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque realizado com sucesso! Seu saldo atual é: {
                  self.saldo}")
        else:
            print("Saldo insuficiente!")

    def verificar_saldo(self):
        print(f"Seu saldo atual é: {self.saldo}")


conta = ContaBancaria()

while True:
    print("\n1. Depositar")
    print("2. Sacar")
    print("3. Verificar saldo")
    print("4. Sair")
    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        valor = float(input("Informe o valor a ser depositado: "))
        conta.depositar(valor)
    elif opcao == 2:
        valor = float(input("Informe o valor a ser sacado: "))
        conta.sacar(valor)
    elif opcao == 3:
        conta.verificar_saldo()
    elif opcao == 4:
        break
    else:
        print("Opção inválida!")
