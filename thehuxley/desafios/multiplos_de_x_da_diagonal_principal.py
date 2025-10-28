n, x = map(int, input().split())
matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        elemento = int(input())
        linha.append(elemento)
    matriz.append(linha)

elementos_diagonal = []
for i in range(n):
    for j in range(n):
        if i == j:
            elementos_diagonal.append(matriz[i][j])

freq = 0
for numero in elementos_diagonal:
    if numero % x == 0:
        print(numero, end= ' ')
        freq += 1

if freq == 0:
    print('NMDX')