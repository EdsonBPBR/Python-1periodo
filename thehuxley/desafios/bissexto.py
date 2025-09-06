# Construa um algortimo que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

def bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return 'Bissexto'
    else:
        return 'Nao bissexto'

ano = int(input())

print(bissexto(ano))