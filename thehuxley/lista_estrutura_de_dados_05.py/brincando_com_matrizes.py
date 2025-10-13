# Escreva umprograma que leia uma matriz 3 x 3 de inteiros da entrada padrão e calcule a média de todos seus valores, o maior valor lido , o valor delta e a soma dos elementos da diagonal princial.
# O delta é igual a 1 se o maior valor for positivo, -1 se for negativo e zero se for zero.

def somaDiagonalPrincipal(matriz):
    return matriz[0][0] + matriz[1][1] + matriz[2][2]

def calculaDelta(maior_valor):
    if maior_valor > 0:
        return 1
    elif maior_valor < 0:
        return -1
    else:
        return 0

if __name__ == '__main__':
    matriz = []
    somatorio = 0
    maior_valor = None 

    for i in range(3):
        linha = []
        for j in range(3):
            elemento = int(input())

            if maior_valor is None or elemento > maior_valor:
                maior_valor = elemento

            linha.append(elemento)

        somatorio += sum(linha)
        matriz.append(linha)

    media = somatorio / 9
    delta = calculaDelta(maior_valor)
    soma_diag = somaDiagonalPrincipal(matriz)

    print(f'{media:.2f} {maior_valor} {delta} {soma_diag}')
