def montaMatriz(n):
    matriz = []
    for i in range(n):
        elemento = str(input()).split()
        linha = []
        for caractere in elemento:
            linha.append(int(caractere))
        matriz.append(linha)
    return matriz

def matrizTransposta(matriz):
    print('Matriz transposta:')
    linha = len(matriz)
    coluna = len(matriz[0])
    j = 0
    for _ in range(coluna):
        for i in range(linha):
            print(f'{matriz[i][j]:<6}', end='')
        print()
        j += 1

def main():
    print('Digite as dimensoes da matriz:')
    print('Digite os elementos da matriz:')
    n, m = map(int, input().split())
    matriz = montaMatriz(n)
    matrizTransposta(matriz)

if __name__ == '__main__':
    main()