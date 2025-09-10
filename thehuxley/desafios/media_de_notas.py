# Escreva um programa que receba um número inteiro n.
# Receba notas que n indicou e faça a sua média
# Mostre na tela a media dos números

def mediadasnotas(n):
    c = 0 
    soma = 0
    while c < n:
        c += 1
        nota = float(input())
        soma += nota

    media = soma / c
    return media

if __name__ == '__main__':
    nota = int(input())
    print(mediadasnotas(nota))

    