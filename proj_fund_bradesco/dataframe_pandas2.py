import pandas as pd
nome_cidade = pd.Series(['Minador do Negrão', 'Palmeira dos Índios', 'Arapiraca'])
populacao = pd.Series([5000,120000,450000])


populacao_cidades = dict(zip(nome_cidade, populacao))
print(populacao_cidades)
del populacao_cidades['Palmeira dos Índios']
print(populacao_cidades)

# dados = {
#     'Cidade': nome_cidade,
#     'Populacao': populacao
# }

# data = pd.DataFrame(dados)
# print(data)