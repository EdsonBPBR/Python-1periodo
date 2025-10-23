operacao = str(input()).upper().strip()
n = 12
matriz = []
for i in range(n):
    linha = [] 
    for j in range(n):
        numero = float(input())
        linha.append(numero)
    matriz.append(linha)    

somatorio = 0
for i in range(n):
    for j in range(n):
        if i < j:
            somatorio += (matriz[i][j])
if operacao == 'S':
    print(f'{somatorio:.1f}')
elif operacao == 'M':
    media = somatorio / 66
    print(f'{media:.1f}')