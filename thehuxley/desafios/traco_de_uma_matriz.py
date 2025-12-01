def montar_matriz(n,m):
    somatorio_principal = 0
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            elemento = int(input())
            linha.append(elemento)
            if i == j:
                somatorio_principal += elemento
        matriz.append(linha)
    return matriz, somatorio_principal

def exibir_matriz(matriz):
    for i in range(len(matriz)):
        linha = ''
        for j in range(len(matriz[0])):
            linha += f'{matriz[i][j]} '
        print(linha.strip())

def calculo_secundaria(matriz, n):
    somatorio_secundaria = 0
    c = 0
    for u in range(n-1,-1,-1):
        somatorio_secundaria += matriz[c][u]
        c += 1
    return somatorio_secundaria

def main():
    n = int(input())
    m = int(input())
    matriz, somatorio_principal = montar_matriz(n,m)
    if n == m: 
        print(somatorio_principal)
        print(calculo_secundaria(matriz,n))
        exibir_matriz(matriz)    
    else:
        print('A matriz nao possui traco')
        exibir_matriz(matriz)    
        
if __name__ == '__main__':
    main()