from livro import Livro
from emprestimo import Emprestimo
from sistemalivro import SistemaLivro

sistema = SistemaLivro()

livro = Livro('1234567891011', 'redes de Computadores', 'tannabaum',2008, 'Tecnologia', 'Disponivel')

emprestimo = Emprestimo('21/11/2025', '30/11/2025', livro)
# print(emprestimo)

sistema.inserir_livro(livro)

for registro in sistema.listar_livros():
    print(registro)