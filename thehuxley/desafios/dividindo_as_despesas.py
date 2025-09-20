c = 0
pago_clara = 0
pago_diana = 0
valor_total = 0

while c < 6:
    valor_conta = float(input())
    nome = str(input()).upper()
    
    if nome == 'CLARA':
        pago_clara += valor_conta
    
    elif nome == 'DIANA':
        pago_diana += valor_conta
    
    else:
        print('Nome inválido!')

    valor_total += valor_conta
    c += 1

if pago_clara > pago_diana:
    print('DIANA')
    taxa = pago_clara - (valor_total/2)
    print(f'{taxa:.2f}')

elif pago_diana > pago_clara:
    print('CLARA')
    taxa = pago_diana - (valor_total/2)
    print(f'{taxa:.2f}')

else:
    print('MORADORAS QUITES')