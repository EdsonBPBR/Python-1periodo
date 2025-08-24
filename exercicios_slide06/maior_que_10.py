# 5 (Maior de 10) Crie um programa em Python para receber 10 valores e determinar
# qual foi o maior valor dentre os números fornecidos

for k in range(10):
    n = float(input('Informe um número: '))

    if k == 0:
        maior = n
    else:
        if n >= maior:
            maior = n
        else:
            pass

print(maior)