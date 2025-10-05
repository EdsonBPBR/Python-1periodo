# dicionario = {
#     1: "um",
#     2: "dois",
#     3: "três"
# }

# dicionario[1] = "one"
# print(dicionario)



# print(dicionario)

# dic = {"disciplina": "APC"}
dic = {1: "primeiro", 2: "edson", 3: "ponciúncula"}

#funções
# del dicionario[1] # excluir a chave do dicionario, não retorna
# print(1 in dic) #verifica se o índice está presente no dicionário, chave
# colocacao = dic.pop(2)
# dic.clear() # limpa tudoo, deixa o dicionário vazio
# dic.keys - cria uma lista com as chaves
# len(dic) - quantos elementos estão armazenados

# for c in dic.keys(): # percorre os chaves do dicionário
#     print(c)

# for v in dic.values(): # percorre os valores do dicionario
#     print(v)
    
# for c, v in dic.items(): # chaves e valores
#     print(f'{c} = {v}')
    
pessoa = {"nome":"Edson", "profissao": "Universitário", "idade": 19}

print(pessoa["nome"])
print(pessoa["profissao"])
print(pessoa["idade"])