# Escreva um programa que receba como entrada o peso da bagagem de um cliente e exiba o valor da taxa a ser paga, ou uma mensagem informando que o peso limite foi excedido.

peso = float(input('Informe o peso da Bagagem: '))

if peso <= 20:
    valor = 0
    print(f'{valor:.2f}')

elif peso <= 25:
    adicional = peso - 20
    valor = adicional * 12.5
    print(f'{valor:.2f}')

elif peso <= 30:
    adicional = peso - 20
    valor = adicional *  32.75
    print(f'{valor:.2f}')

else:
    print('PESO LIMITE EXCEDIDO')