# 2 Crie um programa que realize a soma de duas matrizes fornecidas pelo usu ́ario

def montarMatriz(matriz):
    for i in range(2):
        linha = []
        for j in range(2):
            elemento = int(input(f'({i},{j}): '))
            linha.append(elemento)
        matriz.append(linha)

def imprimirMatriz(matriz):
    for i in range(2):
        linha = '|'
        for j in range(2):
            linha += ' ' + f'{matriz[i][j]}'
        linha += ' |'
        
        print(linha)
        
def somaDuasMatrizes(matriz_a, matriz_b):
    # soma das matrizes
    for i in range(2):
        linha = '|'
        for j in range(2):
            linha += ' ' + f'{matriz_b[i][j] + matriz_a[i][j]}'
        linha += ' |'
        print(linha)

if __name__ == '__main__':
    matriz_a = []
    matriz_b = []

    montarMatriz(matriz_a)
    montarMatriz(matriz_b)

    imprimirMatriz(matriz_a)
    print(f'{'+':^7}')
    imprimirMatriz(matriz_b)
    print(f'{'=':^7}')

    somaDuasMatrizes(matriz_a, matriz_b)