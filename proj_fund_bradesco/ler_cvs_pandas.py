import pandas as pd
# por meio do pandas podemos realizar a importação de dados externos


try:
    autores = pd.read_csv('proj_fund_bradesco/autores.csv')
    print(autores)
except:
    print('Arquivo não encontrado ou não foi possível realizar a leitura!')