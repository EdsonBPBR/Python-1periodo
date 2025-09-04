# Devido aos altos índices de poluição, uma cidade resolveu multar as casas que possuem mais de 2 veículos em R$ 12.89 por mês por cada veículo extra. Escreva um programa que receba como entrada a quantidade de veículos de várias residências, até que seja informado o valor 999, e exiba o total mensal arrecadado com as multas, e a quantidade de casas multadas.

acumulo_impostos = 0
n_casas_multadas = 0

while True:
    n_veiculo = int(input())
    
    if n_veiculo == 999:
        break

    if n_veiculo > 2:
        multa = (n_veiculo - 2) * 12.89 
        acumulo_impostos += multa
        n_casas_multadas += 1

print(f'{acumulo_impostos:.2f}')
print(n_casas_multadas)
    