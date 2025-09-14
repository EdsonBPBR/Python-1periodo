# Leia quatro valores numéricos A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D.
def calculaOctave(A, B, C, D):
    diferenca = (A * B) - (C * D)
    return (diferenca)

if __name__ == '__main__':
    print('DIGITE O VALOR A:')
    A = int(input())
    print('DIGITE O VALOR B:')
    B = int(input())
    print('DIGITE O VALOR C:')
    C = int(input())
    print('DIGITE O VALOR D:')
    D = int(input())

    print(f'DIFERENCA = {calculaOctave(A, B, C, D)}')
