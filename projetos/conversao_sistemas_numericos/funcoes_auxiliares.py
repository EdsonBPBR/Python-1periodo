import os
# funções auxiliares, visando facilitar a manutenção e reduzir o nº de linhas do arquivo principal
def menu():
    print('| "1" - DECIMAL PARA BINÁRIO       |')
    print('| "2" - OCTAL PARA BINÁRIO         |')
    print('| "3" - HEXADECIMAL PARA BINÁRIO   |')
    print('| "4" - DECIMAL PARA OCTAL         |')
    print('| "5" - BINÁRIO PARA OCTAL         |')
    print('| "6" - HEXADECIMAL PARA OCTAL     |')
    print('| "7" - DECIMAL PARA HEXADECIMAL   |')
    print('| "8" - OCTAL PARA HEXADECIMAL     |')
    print('| "9" - BINÁRIO PARA HEXADECIMAL   |')
    print('| "0" - SAIR                       |')
    
def limparTerminal(): # futuro update: checar o Sistema Operacional que o software está rodando.
    os.system('cls')

def continuarOperacao(): # futuro update: inserir para repetir novamente na mesma conversão, sem a necessidade de retornar ao menu principal
    print('Pressione ENTER para continuar...')
    input()
    limparTerminal()
    
def saidaPersonalizada(resultado): #personalizar para mostrar uma tabela, em que o número de entrada equivale a: resultado na base numérica, ex: (5)10 = (101)2
    print('='*35)
    print(f'{resultado: ^35}')
    print('='*35)