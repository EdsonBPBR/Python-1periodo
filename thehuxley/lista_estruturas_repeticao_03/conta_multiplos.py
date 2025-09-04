# Escreva um programa que receba como entrada dois números e retorne a quantidade de números positivos menores que 50 que são múltiplos de ambos.

# AINDA FALTA FAZER

n = int(input())
m = int(input())

# print(m % n)

if n > m:
    if n % m == 0:
        c = 0
        resultado = n / m

        while True:
            c += 1
            if (c * n < 50) and (m * resultado < 50):
                print(f'{n} x {c} = {c*n}')
                print(f'{m} x {resultado} = {resultado*m}')
                resultado += resultado
            else:
                break
        
        

            
    else:
        print('calma ae')
else:
    if m % n  == 0:
        print(f'{m} tem multiplos com {n}')
    else:
        print('calma ae')
