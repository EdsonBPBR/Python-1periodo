# Escreva um programa que calcule os N termos da série S  abaixo:
# S = (1/3) + (2/6) + (3/9) + (4/12) + …
# O seu programa deve imprimir na saída padrão tanto os termos da série quanto o valor da soma com precisão de 2 casas decimais

s = int(input())

numerador = 1
denominador = 3
valor = 0
sequencia = ''

c = 0
while c < s:
    valor += (numerador / denominador)
    sequencia += f'{numerador}/{denominador}'
    if (c + 1) < s:
        sequencia += ' + '
    numerador += 1
    denominador += 3
    
    c += 1

print(sequencia)
print(f'{valor:.2f}')