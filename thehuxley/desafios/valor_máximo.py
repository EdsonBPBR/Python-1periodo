# Crie um programa que tenha apenas uma função, além do programa principal, que receberá como parâmetros uma sequência de inteiros L e um natural n (n>=1), que representam uma sequência L de tamanho n. A função deverá devolver um valor inteiro indicando o maior valor de L.

def maiorValor(n):
    lista = []

    for _ in range(n):
        l = int(input())
        lista.append(l)
    
    return max(lista)

if __name__ == '__main__':
    n = int(input())
    print(maiorValor(n))
