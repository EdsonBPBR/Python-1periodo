# Você deve implementar uma calculadora que calcule as 4 operações básicas, dados 2 números reais, e imprima os 4 resultados.
n = float(input())
m = float(input())

soma = m + n
subtracao = n - m
multi =  n * m
divisao = n / m

print(f'{soma:.2f}')
print(f'{subtracao:.2f}')
print(f'{multi:.2f}')
print(f'{divisao:.2f}')