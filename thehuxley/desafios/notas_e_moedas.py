valor = float(input())

notas = [100, 50, 20, 10, 5, 2, 1]

nota = {
    100: 0,
    50: 0,
    20: 0,
    10: 0,
    5: 0,
    2: 0,
    1: 0,
}
colunas = {
    1: 100,
    2: 50,
    3: 20,
    4: 10,
    5: 5,
    6: 2,
    7: 1,
}

resto = valor
i = 0
while True:
    if i == 0:
        resto = valor
    else:
        if int(resto // notas[i-1]) != 0:
            print(f'{int(resto // notas[i-1])} notas(s) de R$ {(colunas[i]):.2f}')
        resto = resto % notas[i-1]
        if resto == 0:
            break
    i += 1