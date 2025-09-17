# Seu programa deve receber um vetor de N valores inteiros e imprimir na ordem inversa.

tamanho = int(input())
array = str(input()).split()

for elementos in range(tamanho):
    if elementos + 1 == tamanho:
        print(array[::-1][elementos])
    else:
        print(array[::-1][elementos], end=' ')