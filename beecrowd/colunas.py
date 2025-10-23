matriz = []
coluna = int(input())
operacao = str(input()).upper().strip()

for i in range(12):
    linha = []
    for j in range(12):
        n = float(input())
        linha.append(n)
    matriz.append(linha)

somatorio = 0
for i in range(12):
    somatorio += matriz[i][coluna]

if operacao == 'S':
    print(f'{somatorio:.1f}')
elif operacao == 'M':
    media = somatorio/12
    print(f'{media:.1f}')