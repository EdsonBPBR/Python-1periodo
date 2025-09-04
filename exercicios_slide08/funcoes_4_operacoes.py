import os

def menu():
    print('1) Soma')
    print('2) Subtração')
    print('3) Divisão')
    print('4) Multiplicação')
    print('0) Sair')
    opcao = int(input('Informe uma das opções acima: '))
    return opcao

def soma(n1, n2):
    return f'{n1} + {n2} = {n1 + n2}'

def subtracao(n1, n2):
    return f'{n1} - {n2} = {n1 - n2}'

def multiplicacao(n1, n2):
    return f'{n1} x {n2} = {n1 * n2}'

def divisao(n1, n2):
    if n2 == 0:
        return 'O denominador não pode ser 0'
    else:
        return f'{n1} / {n2} = {n1 / n2}'
    
def limpar_terminal():
    os.system('cls')