def recebe_valores():
    numeros = []
    entrada = str(input()).split()
    for inteiro in entrada:
        numeros.append(int(inteiro))
    return numeros

def calcula_moda():
    k = []
    c = 0
    numeros = recebe_valores()
    for valor in numeros:
        if not (valor in k):
            k.append(valor)
            if c == 0:
                maior = numeros.count(valor)
                moda = valor
            else:
                if numeros.count(valor) > maior:
                    maior = numeros.count(valor)
                    moda = valor
        c += 1
    return moda

def main():
    print(f'Moda = {calcula_moda()}')
    
if __name__ == '__main__':
    main()