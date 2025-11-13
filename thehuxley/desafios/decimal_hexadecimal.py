caracteres = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
}

entrada = int(input())

hexa = []

while True:
    if entrada > 16:
        x = (entrada % 16)
        entrada = entrada // 16
        if x in caracteres:
            hexa.append(f'{caracteres[x]}')
        else:
            hexa.append(f'{x}')
    else:
        x = (entrada % 16)
        if x in caracteres:
            hexa.append(f'{caracteres[x]}')
        else:
            hexa.append(f'{x}')
        break

for i in hexa[::-1]:
    print(i, end='')