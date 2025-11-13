n, m = map(int, input().split())

matriz = []
pares = []

c = 0
while True:
    c += 1
    if len(pares) == n:
        break
    if c % 2 == 0:
        pares.append(c) 

c = 0
for i in range(len(pares)//m):
    linha = []
    for j in range(m):
        elemento = pares[c]
        linha.append(elemento)
        c += 1
    matriz.append(linha)

for i in range(m):
    for j in range(len(pares)//m):
        if j > 0:
            print(' ', end='')
        print(matriz[j][i], end='')
    print()