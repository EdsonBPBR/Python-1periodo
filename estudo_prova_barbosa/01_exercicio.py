
# solucção do problema 1 utilizando as funções nativas do Python> max e sum
# ilimitado de números
# lista = []
# while True:
#     n = float(input('Informe um número: '))
#     if n == 0:
#         break
    
#     lista.append(n)
# print(f'Maior valor informado: {max(lista)}')
# print(f'Soma dos elementos informados: {sum(lista)}')

# solução do problema 1 desenvolvendo as próprias funções
def main():
    lista = []
    while True:
        n = float(input('Informe um número: '))
        if n == 0:
            break
        
        lista.append(n)
    print(f'O maior valor informado: {maiorValor(lista)}')
    print(f'A soma dos valores informados foi: {somaValores(lista)}')

def maiorValor(lista):
    for posicao, valor in enumerate(lista):
        if posicao == 0:
            maior_valor = valor
        else:
            if valor > maior_valor:
                maior_valor = valor

    return maior_valor

def somaValores(lista):
    somatorio = 0
    for elemento in lista:
        somatorio += elemento
    return somatorio

if __name__ == '__main__':
    main()