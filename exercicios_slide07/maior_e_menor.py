# (Maior e menor) Crie um programa em Python para receber n ́umeros do usu ́ario e
# informar o maior valor digitado e o menor valor digitado. Caso o valor 0 (zero) seja
# informado o programa deve finalizar sua execu ̧c ̃ao

c = 0
while True:
    numero = float(input('Informe um número: '))

    if c == 0:
        maior = numero
        menor = numero

    elif numero == 0:
        break

    else:
        if numero >= maior:
            maior = numero
        elif numero <= menor:
            menor = numero
        else:
            pass
    c += 1

print(f'Maior número informado foi {maior}')
print(f'Menor número informado foi {menor}')