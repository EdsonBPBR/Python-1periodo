# (Fatorial) Crie um programa em Python para calcular o fatorial de um n ́umero N
# fornecido pelo usu ́ario

#5! = 5 x 4 x 3 x 2 x 1
#n! = n x (n-1) x (n-2) x (n-3) x ... x 1

try: 
    n = int(input('Informe um número: '))

    if n >= 0:
        fatorial = 1

        for i in range(n):
            fatorial = fatorial * (n-i)

        print(f'{n}! = {fatorial}')
    else:
        print('Não é possível calcular o fatorial de um número negativo!')
except ValueError as erro_entrada:
    print(f'Entrada inválida: {erro_entrada}')