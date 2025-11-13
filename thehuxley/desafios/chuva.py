n = int(input())

# primeira matriz:
matriz_a = []
for i in range(n):
    linha = []
    entrada = str(input()).strip().split()
    for elemento in entrada:
        linha.append(int(elemento))
    matriz_a.append(linha)

# segunda matriz:
matriz_b = []
for i in range(n):
    linha = []
    entrada = str(input()).strip().split()
    for elemento in entrada:
        linha.append(int(elemento))
    matriz_b.append(linha)

# soma matriz:
matriz_resultante = []
for i in range(n):
    linha = []
    for j in range(n):
        soma = matriz_a[i][j] + matriz_b[i][j]
        linha.append(soma)
    matriz_resultante.append(linha)

# imprime matriz:
for i in range(n):
    linha = ""
    for j in range(n):
        linha += f'{matriz_resultante[i][j]} '
    print(linha)