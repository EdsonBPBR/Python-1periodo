# (N ́umeros negativos) Crie um programa em Python para receber n ́umeros do usu ́ario
# e informar quantos do valores digitados s ̃ao negativos. Caso o valor 0 (zero) seja
# informado o programa deve finalizar sua execu ̧c ̃ao

negativos = 0

while True:
    n = float(input('Informe um número: '))

    if n < 0:
        negativos += 1
    elif n == 0:
        break
    else:
        pass

print(f'Foram informados {negativos} número(s) negativo(s)')