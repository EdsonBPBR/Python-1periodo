# Dadas duas matrizes A e B, é possível determinar a matriz C = A*B usando a definição padrão de multiplicação de matrizes:

dados = str(input()).strip().split()

n = int(dados[0]) # quantidade de linhas MATRIZ A
m = int(dados[1]) # quantidade de colunas MATRIZ A e quantidade linhas MATRIZ B
o = int(dados[2]) # quantidade de colunas MATRIZ B 

# montar MATRIZ A
matriz_a = []
for i in range(n):
    linha = []
    entrada_linha = str(input()).split()
    for elemento in entrada_linha:
        linha.append(int(elemento))
    matriz_a.append(linha)

# montar MATRIZ B:
matriz_b = []
for i in range(m):
    linha = []
    entrada_linha = str(input()).split()
    for elemento in entrada_linha:
        linha.append(int(elemento))
    matriz_b.append(linha)
    
c = 0
k = 0
matriz_c = []
# multitplicacao dos elementos
for _ in range(n):
    linha_resultado = []
    for i in range(n):
        soma = 0
        for j in range(m):  
            soma += matriz_a[k][j] * matriz_b[j][c]
        c += 1
        linha_resultado.append(soma)
    matriz_c.append(linha_resultado)
    c = 0
    k += 1
    
# saida da matriz c
for i in range(n):
    linha = ""
    for j in range(o):
        linha += f'{matriz_c[i][j]}' + ' '
        
    print(linha.strip())