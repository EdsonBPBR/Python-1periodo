
def montaMatriz(entrada_matriz,n,m): 
    matriz = []
    c = 0
    for _ in range(n):
        linha = []  
        for _ in range(m):
            elemento = int(entrada_matriz[c]) # foda que ao inves de obter do usuario tenho que pegar da lista
            c += 1
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def imprimeMatriz(matriz): # uniica funcao ue nao retorna nada, somente printa
    for i in range(len(matriz)):
        linha = '| '
        for j in range(len(matriz[0])):
            linha += f'{matriz[i][j]} '
        linha += '|'
        print(linha)

def somaMatriz(matriz_a, matriz_b):
    matriz = []
    for i in range(len(matriz_a)):
        linha = []
        for j in range(len(matriz_b[0])):
            elemento = matriz_a[i][j] + matriz_b[i][j]
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def subtracaoMatriz(matriz_a, matriz_b):
    matriz = []
    for i in range(len(matriz_a)):
        linha = []
        for j in range(len(matriz_b[0])):
            elemento = matriz_a[i][j] - matriz_b[i][j]
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def main():
    n = int(input('Quantidade de linhas das matrizes: '))
    m = int(input('Quantidade de colunas das matrizes: '))
    entrada_matriz_1 = str(input('Forneça os valores para matriz 1: ')).split() # ['1', '2','3','4']
    entrada_matriz_2 = str(input('Forneça os valores para matriz 2: ')).split()

    matriz_1 = montaMatriz(entrada_matriz_1, n,m )
    print('Matriz 1:')
    imprimeMatriz(matriz_1)

    print('Matriz 2:')
    matriz_2 = montaMatriz(entrada_matriz_2,n,m)
    imprimeMatriz(matriz_2)

    print('Matriz Soma:')
    matriz_soma = somaMatriz(matriz_1, matriz_2)
    imprimeMatriz(matriz_soma)

    print('Matriz Subtração:')
    matriz_subtracao = subtracaoMatriz(matriz_1, matriz_2)
    imprimeMatriz(matriz_subtracao)
    
if __name__ == '__main__':
    main()