# A sequência de Fibonacci é definida pela seguinte sequência: 0 1 1 2 3 5 8 13 21... Em que cada termo da sequência é obtido somando os dois termos anteriores.
# Escreva um programa que imprima os n primeiros termos da sequência dos números Fibonacci.


while True:
    N = int(input())

    if N == 0:
        break

    termo_anterior = 1
    for k in range(N):
        if k == 0:
            soma = k + termo_anterior
            print(k, end='')

        else:
            soma += termo_anterior
            print(' ' + str(termo_anterior), end='')

            termo_anterior = soma - termo_anterior 
    print()
        