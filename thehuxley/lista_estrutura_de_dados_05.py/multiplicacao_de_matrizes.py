# Dadas duas matrizes A e B, é possível determinar a matriz C = A*B usando a definição padrão de multiplicação de matrizes:

dados = str(input()).split()

n = int(dados[0]) # quantidade de linhas MATRIZ A
m = int(dados[1]) # quantidade de colunas MATRIZ A e quantidade linhas MATRIZ B
o = int(dados[2]) # quantidade de colunas MATRIZ B 
print('-'*25)
# montar MATRIZ A
matriz_a = []
for i in range(n):
    linha = []
    entrada_linha = str(input()).split()
    for elemento in entrada_linha:
        linha.append(int(elemento))
    matriz_a.append(linha)

print(matriz_a)

# montar MATRIZ B:
matriz_b = []
for i in range(m):
    linha = []
    entrada_linha = str(input()).split()
    for elemento in entrada_linha:
        linha.append(int(elemento))
    matriz_b.append(linha)
    
print(matriz_b)

# for k in range(n):
#     i = 0
#     for j in range(m):
#         print(matriz_a[i], matriz_b[j][k])
#     i += 1

print('-'*52)
matriz_c = []
linha = []

for k in range(n):
    i = 0
    c = 0
    somatorio = 0
    for j in range(m):
        somatorio += matriz_a[i][c] * matriz_b[j][k]
        c += 1
    linha.append(somatorio)
    i += 1
    matriz_c.append(linha)

print(linha)
print(matriz_c)