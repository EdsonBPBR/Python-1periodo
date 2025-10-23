n = 3
matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        numero = float(input())
        linha.append(numero)
    matriz.append(linha)
    

for i in range(n):
    print('-'*25)
    for j in range(n-1, -1, -1):
        print(matriz[i][j])