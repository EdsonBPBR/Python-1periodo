# Chama-se de quadrado mágico um arranjo, na forma de um quadrado, de N x N números inteiros tal que todas as linhas, colunas e diagonais têm a mesma soma.
# Por exemplo, o quadrado abaixo
# 16 3 2 13
# 5 10 11 8
# 9 6 7 12
# 4 15 14 1
# é um quadrado mágico de soma 15, pois todas as linhas (2 + 7 + 6 = 15, 9 + 5 + 1 = 15 e 4 + 3 + 8 = 15), colunas (2 + 9 + 4 = 15, 7 + 5 + 3 = 15 e 6 + 1 + 8 = 15) e diagonais (2 + 5 + 8 = 15 e 6 + 5 + 4 = 15) têm a mesma soma (15).

matriz = []
n = int(input())

for a in range(n):
    entrada = str(input()).split()
    linha = []
    for caracteres in entrada:
        linha.append(int(caracteres))
    matriz.append(linha)

# linhas
somas_linhas = []
for i in range(n):
    soma = 0
    for j in range(n):
        soma += matriz[i][j]
    somas_linhas.append(soma)

# colunas
somas_colunas = []
for i in range(n):
    soma = 0
    for j in range(n):
       soma += matriz[j][i]
    somas_colunas.append(soma)

# diagonal principal   
somas_principal = []
soma = 0
for i in range(n):
    soma += matriz[i][i]
somas_principal.append(soma)

# diagonal secundária 
soma_secundaria = []
j = n-1
soma = 0
for i in range(n):
    soma += matriz[i][n-1-i]
    j -= 1
soma_secundaria.append(soma)

resultado = somas_linhas + somas_colunas + somas_principal + soma_secundaria

if resultado.count(somas_principal[0]) == ((n*2) + 2):
    print(somas_principal[0])
else:
    print(-1)