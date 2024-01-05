class ListaTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, tarefa):
        self.tarefas.append(tarefa)

    def remover(self, tarefa):
        if tarefa in self.tarefas:
            self.tarefas.remove(tarefa)

    def exibir(self):
        for tarefa in self.tarefas:
            print(tarefa)


# Cria uma instância da classe ListaTarefas
minhas_tarefas = ListaTarefas()

# Adiciona algumas tarefas
minhas_tarefas.adicionar('Ir à academia')
minhas_tarefas.adicionar('Comprar leite')
minhas_tarefas.adicionar('Estudar para a prova')

# Exibe as tarefas
print("Minhas tarefas:")
minhas_tarefas.exibir()

# Remove uma tarefa
minhas_tarefas.remover('Ir à academia')

# Exibe as tarefas novamente
print("Minhas tarefas após remover uma:")
minhas_tarefas.exibir()
