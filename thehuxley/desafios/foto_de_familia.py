# Consiste de 04 números reais, separados por um final de linha, ordenados de acordo com a mania de Ambrosina. Os números devem ser formatados com 02 casas decimais.

numeros = []
for a in range(4):
    n = float(input())
    numeros.append(n)
    
numeros.reverse()

print(f'{numeros[0]:.2f}')
print(f'{numeros[2]:.2f}')
print(f'{numeros[3]:.2f}')
print(f'{numeros[1]:.2f}')