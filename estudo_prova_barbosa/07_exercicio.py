import os
def montaMatriz(linha, coluna, termo):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            elemento = int(input(f'{termo}({i}, {j}): '))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def imprimeMatriz(matriz):
    if not(matriz):
        print('Não foi possível realizar a multiplicação da matriz')
    else:
        linhas = len(matriz)
        colunas = len(matriz[0])
        
        for i in range(linhas):
            linha = '| '
            for j in range(colunas):
                linha += f'{matriz[i][j]} '
            linha += '|'
            print(linha)

def somaMatrizes(matriz_a, matriz_b):
    matriz = []
    linha = len(matriz_a)
    coluna = len(matriz_b[0])
    
    for i in range(linha):
        linha = []
        for j in range(coluna):
            elemento = matriz_a[i][j] + matriz_b[i][j]
            linha.append(elemento)
        matriz.append(linha)
    return matriz
        
def subtracaoMatrizes(matriz_a, matriz_b):
    matriz = []
    linha = len(matriz_a)     
    coluna = len(matriz_b[0])  
    
    for i in range(linha):
        linha = []
        for j in range(coluna):
            elemento = matriz_a[i][j] - matriz_b[i][j]
            linha.append(elemento)
        matriz.append(linha)
    return matriz    

def multiplicacaoMatrizes(matriz_a, matriz_b):
    matriz = []
    if len(matriz_a[0]) == len(matriz_b):
        for x in range(len(matriz_a)):
            linha = []
            for y in range(len(matriz_b[0])):
                somatorio = 0
                for k in range(len(matriz_b)):
                    somatorio += matriz_a[x][k] * matriz_b[k][y]
                linha.append(somatorio)
            matriz.append(linha)
        return matriz
    else:
        return False

def menu():
    os.system('cls')
    print('1 - Inserir Matrizes')
    print('2 - Somar Matrizes')
    print('3 - Subtrair Matrizes')
    print('4 - Multiplicar Matrizes')
    print('5 - Sair Matrizes')
    opc = int(input("Opção: "))
    return opc

def exibeResultado(opc, matriz_a, matriz_b):
    os.system('cls')
    match opc+1:
        case 2:
            matriz = somaMatrizes(matriz_a, matriz_b)
            sinal = '+'
            operacao = 'Soma'
        case 3:
            matriz = subtracaoMatrizes(matriz_a, matriz_b)
            sinal = '-'
            operacao = 'Subtração'
        case 4:
            matriz = multiplicacaoMatrizes(matriz_a, matriz_b)
            sinal = 'x'
            operacao = 'Multiplicação'
            
    print(f"{operacao} de Matrizes\n")
    imprimeMatriz(matriz_a)
    print(f"{sinal:^8}")
    imprimeMatriz(matriz_b)
    print(f'{'=':^8}')
    imprimeMatriz(matriz)
    input('Pressione ENTER para continuar...')
    
def main():
    while True:
        opc = menu()
        match opc:
            case 1:
                os.system('cls')
                print(f"{'Inserir Matrizes':^25}\n")
                try:
                    linha, coluna = map(int, input('Linha x Coluna (n, m): ').split())
                    matriz_a = montaMatriz(linha, coluna, termo='a')
                    imprimeMatriz(matriz_a)
                    print('Matriz A cadastrada com sucesso!\n')
                    
                    matriz_b = montaMatriz(linha, coluna, termo='b')
                    imprimeMatriz(matriz_b)
                    print('Matriz B cadastrada com sucesso!\n')
                    
                    input('Pressione ENTER para continuar...')  

                except:
                    print('Entrada Inválida! Não foi possível inserir os valores das matrizes\n')
                    input('Pressione ENTER para continuar...')  
                
            case 2:
                exibeResultado(1, matriz_a, matriz_b)
                
            case 3:
                exibeResultado(2, matriz_a, matriz_b)
                
            case 4:
                exibeResultado(3, matriz_a, matriz_b)
                
            case 5:
                print('Saindo do programa...')
                break   
    
if __name__ == '__main__':
    main()