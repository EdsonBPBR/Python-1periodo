# Helena é dona de uma pequena cantina que fornece refeições para os universitários. No cardápio de hoje, eles podem escolher entre lasanha (R$ 8,00) ou estrogonofe (R$ 11,00) para comer, e entre refrigerante (R$ 3,00) ou suco (R$ 2,50) para beber. Escreva um programa que receba como entrada as escolhas de cada cliente e exiba o valor total a ser pago.

opc1 = str(input())
opc2 = str(input())
valor_total = 0

if opc1.upper() == 'LASANHA':
    valor_total += 8
elif opc1.upper() == 'ESTROGONOFE':
    valor_total += 11
else:
    valor_total += 0

if opc2.upper() == 'REFRIGERANTE':
    valor_total += 3
elif opc2.upper() == 'SUCO':
    valor_total += 2.5
else:
    valor_total += 0

print(f'{valor_total:.2f}')