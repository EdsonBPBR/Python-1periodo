# Uma administradora de cartões está oferecendo uma promoção aos seus clientes. A pessoa que não puder pagar o total da fatura no mês de março poderá pagar apenas 50% do valor, e o restante poderá ser pago no mês seguinte com juros de 6,5%. 

# Desenvolva uma solução para ajudar o cliente a descobrir qual será o valor de sua fatura no mês de abril caso ele aceite a proposta.

valor = float(input('Informe o valor total da fatura: '))

marco = valor * 0.5
abril = (valor - marco) * 1.065 

print(f'Valor total da fatura: R$ {valor:.2f}')
print(f'Valor a pagar em Marco: R$ {marco:.2f}')
print(f'Valor a pagar em Abril: R$ {abril:.2f}')