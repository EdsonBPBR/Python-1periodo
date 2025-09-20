# 2 números X,Y onde X indica a quantidade de números da sequência e Y o número procurado.

# uma sequência de X números.

if __name__ == '__main__':
    dados = str(input()).split()
    x = int(dados[0])
    y = int(dados[1])

    freq = 0
    for k in range(x):
        n = int(input())

        if n == y:
            freq += 1

    print(freq)