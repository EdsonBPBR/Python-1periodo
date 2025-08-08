ano = int(input('Informe um ano: '))

# Se divisível por 4 e não divisível por 100: bissexto
# Se divisível por 4, divisível por 100 e por 400: bissexto
# Se for divisível por 4, divisível por 100 e não divisível por 400: não bissexto

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f'{ano} é bissexto')
else:
    print(f'{ano}')