class Emprestimo:
    def __init__(self, data_emprestimo, data_devolucao, livro):
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.livro = livro
        
    def __str__(self):
        return f'{self.livro.titulo.title()} {self.data_emprestimo} {self.data_devolucao}'