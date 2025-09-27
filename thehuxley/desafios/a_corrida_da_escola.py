# A primeira linha da entrada contém dois inteiros N e M representando o número de competidores e o número
# de voltas da corrida, respectivamente.

if __name__ == '__main__':
    n, m = map(int, input().split())
    registro = []

    for a in range(n):
        soma = 0
        dados = str(input()).split()
        for elementos in dados:
            soma += int(elementos)
        registro.append(soma)

    print((registro.index(min(registro)))+1)