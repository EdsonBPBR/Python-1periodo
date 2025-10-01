# Escrever um programa que lê um número N. Este N é o tamanho de um array.
# Em seguida, leia cada um dos N números do array, encontre o menor elemento desse array, a sua posição dentro do array e imprima essas informações.
# Considere que o array começa na posição 0

n = int(input())
dados = str(input()).split()

for a in range(n):
    if a == 0:
        menor = int(dados[a])
        posicao = 0
    else:
        b = int(dados[a])
        if b < menor:
            menor = b
            posicao = dados.index(dados[a])
            
print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')