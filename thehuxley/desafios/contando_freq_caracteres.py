# Escreva um programa que receba um texto em uma única linha e imprima cada caractere e o número de vezes que ocorre no texto, na ordem inversa à alfabética.

if __name__ == '__main__':
    texto = str(input())
    frequencia = {}

    for caractere in texto:
        if caractere in frequencia:
            pass
        else:
            frequencia[caractere] = texto.count(caractere)
        
    b = list(frequencia.keys())
    b.sort(reverse=True)

    for elemento in b:
        print(f'{elemento} {frequencia[elemento]}')