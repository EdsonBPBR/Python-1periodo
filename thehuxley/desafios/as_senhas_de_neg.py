# A quantidade de senhas que vão ser inseridas , seguido pelas senhas, uma em cada linha. As plataformas requerem que a senha seja composta por letras maiúsculas e digitos, exclusicamente.

# n = int(input())
cod = {
    '0' : '6',
    '1' : '7',
    '2' : '9',
    '3' : '8',
    '4' : 'A',
    '5' : '2',
    '6' : 'B',
    '7' : 'F',
    '8' : '1',
    '9' : 'C',
    'A' : '0',
    'B' : 'D',
    'C' : 'E',
    'D' : '3',
    'E' : '5',
    'F' : '4'
}

digitos = '0123456789'
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = int(input())
senha_completa = ''
contador = 0

for i in range(n):
    fragmento_senha = ''
    entrada_senha = str(input())
    senha = list(entrada_senha)

    for posicoes in range(len(senha)):
        # print()
        if (senha[posicoes] in digitos) or (senha[posicoes] in alfabeto):
            if senha[posicoes] in cod:
                senha[posicoes] = cod[senha[posicoes]]
            situacao = True
        else:
            print('Alguma senha eh invalida!')
            situacao = False
            break
            
    for caracteres in senha:
        fragmento_senha += f'{caracteres}'
        contador += 1
    
    senha_completa += f'-{fragmento_senha}'

if situacao:
    print(f'{senha_completa} {contador}')
