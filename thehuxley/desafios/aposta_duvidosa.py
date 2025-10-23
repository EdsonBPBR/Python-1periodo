t = int(input())
for _ in range(t):
    n = int(input())
    matriz = []

    for i in range(n):
        entrada = str(input()).split()
        linha = []
        for elemento in entrada:
            linha.append(int(elemento))
        matriz.append(linha)
        
    # verifica se é magicoo
    verifica = []
    # linhas
    for i in range(n):
        verifica.append(sum(matriz[i]))

    # colunas
    for j in range(n):
        somatorio_colu = 0
        for i in range(n):
            somatorio_colu += (matriz[i][j])
        verifica.append(somatorio_colu)

    # diag principal
    somatorio_dia_princ = 0
    for i in range(n):
        somatorio_dia_princ += matriz[i][i]
    verifica.append(somatorio_dia_princ)

    # diag secundaria:
    somatorio_dia_secun = 0
    c = 0
    for j in range(n-1, -1, -1):
        somatorio_dia_secun += matriz[c][j]
        c += 1
    verifica.append(somatorio_dia_secun)

    if all(elemento == verifica[0] for elemento in verifica):
        print('Eh quadrado magico!!!')
    else:
        print('Nao eh!!!')