# Determinar todos os divisores de um número inteiro positivo.

n = int(input())

c = 0
while n > c:

    c += 1

    if n % c == 0:
        print(c)
