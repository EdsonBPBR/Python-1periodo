# Escreva um programa que receba como entrada o peso da bagagem de um cliente e exiba o valor da taxa a ser paga, ou uma mensagem informando que o peso limite foi excedido.
peso = float(input('Informe o peso da bagagem (KM): '))

if peso <= 20:
    #excesso = peso - 20
    valor = 0
    print(f'{valor:.2f}')

elif peso >= 21 and peso <= 25:
    excesso = peso - 20
    valor = excesso * 12.5
    print(f'{valor:.2f}')

elif peso >= 26 and peso <= 30:
    excesso = peso - 20
    valor = excesso * 32.75
    print(f'{valor:.2f}')

else:
    print('PESO LIMITE EXCEDIDO')