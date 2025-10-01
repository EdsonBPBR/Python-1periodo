# Sua missão é fazer um programa que leia o código do produto, a quantidade comprada e imprima o valor que o cliente deve pagar, já considerando o desconto quando aplicável.

itens = {
    1: 5.3,
    2: 6,
    3: 3.2,
    4: 2.5
}

cod = int(input())
quant = int(input())

valor = itens[cod] * quant

if quant >= 15 or valor >= 40:
    print(f'R$ {(valor*0.85):.2f}')
else:
    print(f'R$ {valor:.2f}')