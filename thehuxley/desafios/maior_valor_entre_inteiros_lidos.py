# Escreva um programa que encontre o maior valor entre vários inteiros lidos e a sua posição. Admita que o primeiro valor lido especifica o número de valores de entrada.

n = int(input())
lista = []

for _ in range(n):
    x = int(input())
    lista.append(x)

print(f'o maior numero eh {max(lista)}, e foi lido na posicao {lista.index(max(lista))}')