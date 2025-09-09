# Faça um programa que receba dois inteiros x e n, com x, n > 0 e x < n, e conte o número de múltplos de x menores do que n.

def contantoMultiplos(x, n):
    multiplos = 0
    c = 1
    while True:
        resultado = c * x
        
        if resultado >= n:
            break
        else:
            multiplos += 1
        
        c += 1
        
    return f'O numero {x} tem {multiplos} multiplos menores que {n}.'

if __name__ == '__main__':
    x = int(input())
    n = int(input())

    print(contantoMultiplos(x,n))
