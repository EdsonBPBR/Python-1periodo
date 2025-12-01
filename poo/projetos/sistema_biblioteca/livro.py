class Livro:
    def __init__(self, isbn, titulo, autor, ano, genero, disponibilidade):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero
        self.disponibilidade = disponibilidade
    
    def __str__(self):
        return f'{self.isbn} {self.titulo.title()} {self.autor.title()} {self.ano} {self.genero} {self.disponibilidade}' 
