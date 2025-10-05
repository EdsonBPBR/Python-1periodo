# Faça um programa que leia uma sequência de 10 números e informe o total de ocorrências do último número lido.
# O programa receberá uma sequência de 10 números inteiros.

entrada = str(input()).split()
print(f'O numero {entrada[-1]} apareceu {entrada.count(entrada[-1])} vezes')