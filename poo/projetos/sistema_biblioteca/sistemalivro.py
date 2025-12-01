class SistemaLivro:
    def __init__(self):
        self.registros = []
    
    def inserir_livro(self, livro):
        self.registros.append(livro)
    
    def listar_livros(self):
        return self.registros