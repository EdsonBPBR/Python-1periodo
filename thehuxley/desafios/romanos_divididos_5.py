def calcula_romano(entrada, romanos):
    somatorio = 0
    for posicao, caractere_romano in enumerate(entrada):
        if romanos[entrada[posicao]] < romanos[entrada[(posicao+1)%len(entrada)]] and posicao+1 != len(entrada):
            somatorio -= romanos[caractere_romano]
        else:
            somatorio += romanos[caractere_romano]
        
    return somatorio

def imprimir_saida(resto):
    if resto == 0:
        return ('O numero e multiplo de 5!')
    else:
        return (f'O resto pela divisao por 5 do numero dado e igual a {resto}!')

def main():
    romanos = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    entrada = list(str(input()).strip())
    resto = calcula_romano(entrada, romanos) % 5
    print(imprimir_saida(resto))

if __name__ == '__main__':
    main()