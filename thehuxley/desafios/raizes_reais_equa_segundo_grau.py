# Escreva um programa computacional para calcular e mostrar as raízes de uma equação do segundo grau dada por Ax2 + Bx + C = 0. Os valores de A, B e C devem ser lidos. Considere que a equação possui 2 raízes reais.

def calculaDelta(a, b, c):
    delta = (b**2) - (4*a*c)
    return delta

def calculaRaizes(a, b, delta):

    x1 = (-b + (delta**(1/2)))/ (2*a)
    x2 = (-b - (delta**(1/2)))/ (2*a)

    return x1, x2

if __name__ == '__main__':
    dados = str(input()).split()

    a = float(dados[0])
    b = float(dados[1])
    c = float(dados[2])

    delta = calculaDelta(a, b, c)
    x1, x2 = calculaRaizes(a, b, delta)
    print(f'{x2:.2f} {x1:.2f}')
