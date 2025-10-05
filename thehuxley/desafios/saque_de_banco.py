# Crie um programa que gerencie a saída de notas em um caixa eletrônico.
# Recebendo a quantia, seu programa deve dizer quantas de cada nota devem ser retiradas. Utilize o critério da "distribuição ótima", ou seja, o menor número possível de cédulas. O caixa tem cédulas de R$50, R$20, R$10, R$5 e R$1.

valor = int(input())

n_cedulas_50 = valor // 50
resto_50 = valor % 50

n_cedulas_20 = resto_50 // 20
resto_20 = resto_50 % 20

n_cedulas_10 = resto_20 // 10
resto_10 = resto_20 % 10

n_cedulas_5 = resto_10 // 5
n_cedulas_1 = resto_10 % 5

print(f'Notas de 50: {n_cedulas_50}')
print(f'Notas de 20: {n_cedulas_20}')
print(f'Notas de 10: {n_cedulas_10}')
print(f'Notas de 5: {n_cedulas_5}')
print(f'Notas de 1: {n_cedulas_1}')
