# Faça um programa que leia dois números inteiros, representando os valores inicio e fim de um intervalo e imprima os múltiplos de 5 entre eles.
entrada = input().split()

n = int(entrada[0])
m = int(entrada[1])

multiplos = []
for a in range(n, m + 1):
    if a % 5 == 0:
        multiplos.append(str(a))

print('|'.join(multiplos))