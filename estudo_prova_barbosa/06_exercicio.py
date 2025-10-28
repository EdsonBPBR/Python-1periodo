# linhas x colunas

# montar matriz
def montaMatriz(matriz, linhas, colunas):
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            elemento = int(input(f'({i}, {j}): '))
            linha.append(elemento)
        matriz.append(linha)
        
# imprimir a matriz
def imprimrMatriz(matriz, linhas, colunas):
    for i in range(linhas):
        linha = "| "
        for j in range(colunas):
            linha += f'{matriz[i][j]:^2}'
        linha += "|"
        print(linha)
        
def main():
    linhas, colunas = map(int, input('Linhas x Colunas: ').split())
    matriz = [] # dicionarios, poderia
    
    montaMatriz(matriz, linhas, colunas)
    imprimrMatriz(matriz, linhas, colunas)
    
if __name__ == '__main__':
    main()