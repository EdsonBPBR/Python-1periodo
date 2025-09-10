import os
from colored import fore, back, style

def menu():
    print('1 - Calcular Nova Média')
    print('2 - Sair')

def calculaMedia(n1, n2):
    return (n1 + n2)/2

def limparTerminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def coresTerminal():
    cor_normal: str = f'{fore('white')}'
    cor_1: str = f'{fore('red')}{back('black')}'
    cor_2: str = f'{fore('light_gray')}{back('blue')}'
    return cor_normal, cor_1, cor_2