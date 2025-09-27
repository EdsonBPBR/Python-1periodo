# Crie um programa que tenha apenas uma função, além do programa principal, que receberá como parâmetros três números naturais i, f e x e que deverá mostrar todos os valores múltiplos de x no intervalo [i, f]. O PROGRAMA PRINCIPAL deverá ler os valores e a FUNÇÃO deverá exibir os múltiplos.
def calculaMultiplos(i, f, x):
    k = 1
    while True:
        resultado = x * k
        if resultado >= i and resultado <= f:
            print(resultado)

        elif resultado > f:
            break

        k += 1

if __name__ == '__main__':
    i = int(input())
    f = int(input())
    x = int(input())

    calculaMultiplos(i, f, x)


   

