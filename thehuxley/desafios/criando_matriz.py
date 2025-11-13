# montar matriz
def montaMatriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            if i == j:
                elemento = 1
            elif i < j:
                elemento = 10
            else:
                elemento = -10
            linha.append(elemento)
        matriz.append(linha)
    return matriz

 # imprimir a matriz:
def exibirMatriz(matriz):
    for i in range(len(matriz)):
        linha = ''
        for j in range(len(matriz[0])):
            linha += f'{matriz[i][j]:<7}'
        print(linha)
        
def main():
    print('Digite a ordem N da matriz:')
    n = int(input())
    matriz = montaMatriz(n)
    exibirMatriz(matriz)
    
if __name__ == '__main__':
    main()