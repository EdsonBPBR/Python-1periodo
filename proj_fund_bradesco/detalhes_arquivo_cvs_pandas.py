import pandas as pd

autores = pd.read_csv('proj_fund_bradesco/autores.csv')
print(autores.info()) # obtem as informações do arquivo, como tipo, número de colunas, etc...
print(autores.columns) # exibe as colunas do arquivo
