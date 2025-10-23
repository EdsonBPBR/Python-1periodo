import pandas as pd

autor = ['Roque de Laraia','Rodney William', 'Tanenbaum', 'Rômulo']
livro = ['Cultura: um conceito antropológico', 'Apropriação Cultural', 'Redes de Computadores v8', 'Lógica no Cotidiano']
ano = [2001, 2010, 2008, 2013]

dados = {
    'Autor': autor, 
    'Livro': livro,
    'Ano': ano,
}

autores = pd.DataFrame(dados)
print(autores)


# exportar para CSV
autores.to_csv('proj_fund_bradesco/autores.csv')