#Escreva um programa que receba como entrada dois números e retorne a quantidade de números positivos menores que 50 que são múltiplos de ambos.

n = int(input())
m = int(input())

multiplos = 0
x = 1

while x < 50:
    if x % n == 0 and x % m == 0:
        multiplos += 1
    x += 1

print(multiplos)
