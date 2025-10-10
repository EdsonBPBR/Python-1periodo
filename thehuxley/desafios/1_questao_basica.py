def maiorNumero(n1, n2):
    if n1 > n2:
        maior = n1
    elif n1 < n2:
        maior = n2
    else:
        maior = n1
    return maior

if __name__ == '__main__':
    try:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o primeiro número: "))

        print(f'Maior número: {maiorNumero(n1,n2)}')
    except ValueError:
        print("Dado de entrada inválido!")