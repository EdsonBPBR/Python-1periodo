# 1. Uma linha com um inteiro n que representa o número de inscritos que se apresentaram à prova.# 2. Uma sequência de n inteiros,  um por linha, cada um representando um CPF.
# 3. Uma sequência de n inteiros, um por linha, cada um representando uma not. # 4. Uma linha com um inteiro m que representa o número de casos de teste.# 5. Uma sequência de m CPFs, um por linha, para os quais serão pesquisadas as notas.

registros = {}

n = int(input())

for _ in range(n):
    cpf = int(input())
    registros[cpf] = None
    
for chaves in registros.keys():
    nota = int(input())
    registros[chaves] = nota
    
m = int(input())

for _ in range(m):
    cpf_busca = int(input())
    
    if cpf_busca in registros:
        print(registros[cpf_busca])
    else:
        print('NAO SE APRESENTOU')