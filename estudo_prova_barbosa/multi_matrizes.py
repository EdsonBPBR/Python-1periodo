matriz_a = [
    [1,2],
    [6,7]
]

matriz_b = [
    [0,3],
    [5,4]
]


matriz_multi = []

for x in range(len(matriz_a)):  # percorre linhas de a
    linha = []
    for c in range(len(matriz_b[0])):  # percorre colunas de B
        soma = 0
        for k in range(len(matriz_b)):  # percorre os elementos da linha/coluna
            soma += matriz_a[x][k] * matriz_b[k][c]
        linha.append(soma)
    matriz_multi.append(linha)
    
print(matriz_multi)