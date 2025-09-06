# Lanne é uma funcionária dedicada e seu chefe prometeu-lhe um bônus especial de 75% de seu salário no fim do ano. Ela decidiu usar o dinheiro para fazer uma viagem, mas a escolha do destino dependerá do valor do bônus. Caso ela receba menos de R$ 2000, ela irá conhecer a Argentina. Já se o bônus for entre R$ 2000 e R$ 3000, ela irá para a Espanha. Se o bônus ganho for maior que R$ 3000, ela realizará o sonho de conhecer a Alemanha. Escreva um programa que receba como entrada o salário de Lanne e exiba o nome do país que ela irá conhecer.

salario = float(input())

bonus = salario * 0.75  

if bonus > 3000:
    print('ALEMANHA')
elif bonus >= 2000: 
    print('ESPANHA')
else:
    print('ARGENTINA')
