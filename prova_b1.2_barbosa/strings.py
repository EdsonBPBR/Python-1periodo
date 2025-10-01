import os
import doctest

def menu():
    print('1) fornecer texto')
    print('2) substituir caractere')
    print('3) procurar caractere')
    print('4) inverter texto')
    print('5) verificar se é palíndromo')
    print('6) sair') 

def cadastrarTexto():
    texto = str(input('Digite seu texto: '))

    return texto

def substituirCaractere(texto, caractere_atualizar, caractere_substituir):
    """
    >>> substituirCaractere('Ponciuncula', 'P', 'p')
    'ponciuncula'
    """
    
    texto = texto.replace(f'{caractere_atualizar}', f'{caractere_substituir}')

    return texto

def buscarCaractere(caractere):
    freq = 0
    for elemento in range(len(texto)):
        if texto[elemento] == caractere:
            freq += 1

    return freq

def inverteTexto(texto):
    return texto[::-1]

def verificaPalindromo(texto):
    texto_invertido = texto[::-1]
    if texto == texto_invertido:
        print(f'Sim, o texto fornecido é um palindromo!')
    else:
        print(f'{texto} NÃO, o texto fornecido não é um palíndromo, pois sua palavra invertida é {texto_invertido}')

if __name__ == '__main__':
    while True:
        menu()

        opc = int(input(':'))
        os.system('clear')

        if opc == 1:
            texto = cadastrarTexto()
        
        elif opc == 2:
            caractere_atualizar = str(input('Informe qual CARACTERE deseja atualizar: '))
            caractere_substituir = str(input('Informe por qual CARACTERE deseja substituir: '))
            print(substituirCaractere(texto, caractere_atualizar, caractere_substituir))

        elif opc == 3:
            caractere = str(input('Informe qual CARACTERE deseja procurar: '))
            freq = buscarCaractere(caractere)

            print(f'O caractere informado apareceu {freq} no texto cadastrado')

        elif opc == 4:
            print(inverteTexto(texto))

        elif opc == 5:
            print(verificaPalindromo(texto))

        elif opc == 6:
            print('Saindo do programa....')
            break
    
    doctest.testmod()