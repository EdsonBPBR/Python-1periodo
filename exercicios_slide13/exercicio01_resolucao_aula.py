def montaMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            elemento = int(input(f'Informe o elemento: ({i+1}, {j+1}): '))
            linha.append(elemento)
        matriz.append(linha)
        
    return matriz

def imprimeMatriz(linhas, colunas, matriz):
    for i in range(linhas):
        linha = '| '
        for j in range(colunas):
            linha += f'{matriz[i][j]:^3} '
        linha += '|'
        print(linha)
        
def somaMatrizes(linhas, colunas):
    n_linhas = len(linhas)
    n_colunas = len(linhas[0])
    matriz_soma = []
    for i in range(n_linhas):
        linhas = []
        for j in range(n_colunas):
            soma = linhas[i][j] + colunas[i][j]
            linhas.append(soma)
            
        matriz_soma.append(linhas)
        
    return matriz_soma
        
def main():
    try:
        linhas = int(input('Linhas: '))
        colunas = int(input('Colunas: '))
        matriz = montaMatriz(linhas, colunas)
        imprimeMatriz(linhas, colunas, matriz)
        
    except ValueError:
        print('Dado de entrada inválido!')
    
if __name__ == '__main__':
    main()