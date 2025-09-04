# Escreva um programa que receba como entrada um número inteiro positivo e exiba todos os divisores positivos dele em ordem decrescente.

n = int(input())
c = n
while True:
    if c <= 1:
        print(c)
        break
    elif n % c == 0:
        print(c)
    c -= 1
    