# Um número inteiro é dito perfeito se o dobro dele é igual à soma de todos os seus divisores.
# Por exemplo, como os divisores de 6 são 1, 2, 3 e 6 e 1 + 2 + 3 + 6 = 12, 6 é perfeito.
# A matemática ainda não sabe se a quantidade de números perfeitos é ou não finita. Escreva um programa que liste todos os números perfeitos menores que um inteiro n dado.

m = int(input())
n = 1  

while n < m:
    soma_divisores = 0
    c = 1

    while c <= n:  
        if n % c == 0:
            soma_divisores += c
        c += 1

    if soma_divisores == 2 * n:
        print(n)

    n += 1
