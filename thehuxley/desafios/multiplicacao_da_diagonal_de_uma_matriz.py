
def montaMatriz(n,k):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            elemento = int(input())
            if i == j:
                linha.append(elemento*k)
            else:
                linha.append(elemento)
        matriz.append(linha)
    return matriz

def imprimeMatriz(matriz, n):
    for i in range(n):
        for j in range(n):
            print(matriz[j][i], end = ' ')
        print()
        
def main():
    while True:
        n = 4
        k = int(input())
        if k == 0:
            break
        matriz = montaMatriz(n, k)
        imprimeMatriz(matriz, n)
    
if __name__ == '__main__':
    main()