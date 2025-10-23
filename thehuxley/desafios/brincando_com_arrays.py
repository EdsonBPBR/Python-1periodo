# Faça um programa que leia n números inteiros dados em um array e os imprime:
# a) na ordem inversa dos números dados
# b) com um deslocamento para a esquerda
# c) ordenado em ordem decrescente

n = int(input())
elementos = str(input()).split()
array = []

for caractere in elementos:
    array.append(int(caractere))

a = (array[::-1])

for posicoes in range(len(a)):
    if len(a) - 1 == posicoes:
        print(a[posicoes], end=''+'\n')
    else:
        print(a[posicoes], end=' ')

primeiro_elemento = [array[0]]
b = (array[1:n]+primeiro_elemento)

for posicoes in range(len(b)):
    if len(b) - 1 == posicoes:
        print(b[posicoes], end=''+'\n')
    else:
        print(b[posicoes], end=' ')

array.sort(reverse=True)
c = (array)

for posicoes in range(len(c)):
    if len(c) - 1 == posicoes:
        print(c[posicoes], end=''+'\n')
    else:
        print(c[posicoes], end=' ')
