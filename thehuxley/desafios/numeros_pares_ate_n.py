# Encontrar os números pares de 1 até N. Imprimir os números lado a lado com 3 espaços entre eles. 

n = int(input())

c = 0
while n >= c:
    if c % 2 == 0:
        print(c, end='   ')

    c += 1

print()