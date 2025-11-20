if __name__ == '__main__':
    lista_numeros = []
    for i in range(101):
        numero = float(input())
        lista_numeros.append(numero)

    posicoes = []
    for numero in lista_numeros:
        if numero == lista_numeros[-1]:
            posicoes.append(lista_numeros.index(numero))
            lista_numeros[lista_numeros.index(numero)] = -1
            
    if len(posicoes) > 0:
        print('Digite a sequencia de numero:')
        print('Indice no qual o numero desejado aparece:')
        for i in range(len(posicoes)):
            if len(posicoes) - 1 != i:
                print(posicoes[i])