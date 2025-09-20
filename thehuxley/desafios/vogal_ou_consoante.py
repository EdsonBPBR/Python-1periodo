# Escreva um programa em C que receba uma letra do alfabeto e imprima uma mensagem indicando se ela é uma vogal ou uma consoante. 
# Informar se a entrada não for nem vogal nem consoante.

if __name__ == '__main__':
    vogais = 'aeiouAEIOU'
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHIKLMNPQRSTVWXYZ'

    letra = str(input())

    if not(letra in vogais or letra in consoantes):
        print(f'O caractere {letra} nao eh nem consoante nem vogal')

    for a in range(len(vogais)):
        if vogais[a] == f'{letra}':
            print(f'A letra {letra} eh uma vogal')
            break

    for b in range(len(consoantes)):
        if consoantes[b] == f'{letra}':
            print(f'A letra {letra} eh uma consoante')
            break
