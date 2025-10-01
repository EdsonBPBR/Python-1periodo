# Escreva um programa que lê dois valores e exibe o resultado do primeiro número dividido pelo segundo número, com no máximo seis casas decimais.
# Não imprima nada na entrada e na saída.

n1 = float(input())
n2 = float(input())

if n2 == 0:
    pass
else:
    div = n1 / n2
    print(f'{div:.6f}')