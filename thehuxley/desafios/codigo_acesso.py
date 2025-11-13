def calculoC(entrada):
    somatorio_indices_pares = 0
    somatorio_indices_impares = 0

    for i in range(len(entrada)):
        if i % 2 == 0:
            somatorio_indices_pares += int(entrada[i])
        else:
            somatorio_indices_impares += int(entrada[i])

    c = (somatorio_indices_pares * 3 + somatorio_indices_impares) % 10
    return c

def calculoR(entrada):
    maior_bloco = 1
    atual = 1

    for i in range(1, len(entrada)):
        if entrada[i] == entrada[i - 1]:
            atual += 1
            if atual > maior_bloco:
                maior_bloco = atual
        else:
            atual = 1
    return maior_bloco

def palavraBase(palavra):
    vogais = 'AEIOU'
    base = ''

    for letra in palavra:
        if letra not in vogais:
            base += letra

    if base == '':
        return 'VOID'
    return base

def main():
    n = int(input())
    entrada = str(input())
    palavra = list(str(input()).strip().upper())

    print(calculoC(entrada), calculoR(entrada))
    print(f'codigo: {palavraBase(palavra)}{calculoC(entrada)}{calculoR(entrada)}')
    
if __name__ == '__main__':
    main()