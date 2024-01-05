class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def exibir_informacoes(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, \
Número de páginas: {self.num_paginas}'


livro = Livro('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 96)
print(livro.exibir_informacoes())
