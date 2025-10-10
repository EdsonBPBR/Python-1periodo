# utilizando listas
matriz = [
    [ 1 , 2], 
    [ 3 , 7],
    [ 5 , 9],
    [ 10, 15]
]

linhas = len(matriz) # número de linhas

colunas = len(matriz[0]) # tamanho da coluna, o 0, 

for i in range(linhas):
    for j in range(colunas):
        print(f'a({i+1},{j+1}) : {matriz[i][j]}')