# Chama-se de quadrado mágico um arranjo, na forma de um quadrado, de N x N números inteiros tal que todas as linhas, colunas e diagonais têm a mesma soma.

n = int(input())
matriz = []
for i in range(n):
    linha = []
    entrada = str(input()).split()
    for elemento in entrada:
        linha.append(int(elemento))
    matriz.append(linha)

somatorio_linha = 0
somatorio_coluna = 0
somatorio_dia_princ = 0
somatorio_dia_secund = 0

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        somatorio_linha += matriz[i][j]
        somatorio_coluna += matriz[j][i]
        if i == j:
            somatorio_dia_princ += matriz[i][j]
c = 0
for i in range(len(matriz)-1,-1,-1):
    somatorio_dia_secund += matriz[c][i]
    c += 1
    
if somatorio_linha/len(matriz) == somatorio_coluna/len(matriz) == somatorio_dia_princ == somatorio_dia_secund:
    print(somatorio_dia_secund)
else:
    print(-1)
    