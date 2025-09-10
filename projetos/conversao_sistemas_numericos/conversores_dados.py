# como algumas funções que convertem de decimal para outra base a entrada é um número inteiro, é necessário fazer a conversão de alguns desses dados pois algumas funções retornam valores em strings e se for necessário fazer a conexão entre elas para conversão de bases é necessário trabalhar com somente um tipo de dado, visando não alterar o algoritmo das funções faz-se necessário criar um arquivo de conversão.

def conversorStrInt(n_str):
    n_int = int(n_str)
    return n_int

def conversorIntStr(n_int):
    n_str = str(n_int)
    return n_str
