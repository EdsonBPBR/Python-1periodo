import os
import random

def menu():
    print('''
    [1] - Pedra, 
    [2] - Papel, 
    [3] - Tesoura, 
    [4] - Largato, 
    [5] - Spock,
    [0] - Sair'''
    )

    jogador1 = int(input('Jogador 1 [1-5]: '))
    return jogador1

def limpar_tela():
    os.system('cls')
    
def verifica_vencedor(jogador1, jogador2):
    if (jogador1 == 1 and jogador2 == 3) or (jogador1 == 3 and jogador2 == 2) or (jogador1 == 2 and jogador2 == 1) or (jogador1 == 1 and jogador2 == 4) or (jogador1 == 5 and jogador1 == 1) or (jogador1 == 4 and jogador2 == 2) or (jogador1 == 2 and jogador2 == 5) or (jogador1 == 5 and jogador2 == 3) or (jogador1 == 4 and jogador2 == 5):
        return 'PARABÉNS! VOCÊ VENCEU!'

    elif jogador1 == jogador2:
        return 'Ocorreu um EMPATE!'

    else:
        return 'COMPUTADOR VENCEU!'

def escolha_computador():
    escolha = random.randint(1, 5)
    match escolha:
        case 1:
            return 'Computador escolheu PEDRA'
        case 2:
            return 'Computador escolheu PAPEL'
        case 3:
            return 'Computador escolheu TESOURA'
        case 4:
            return 'Computador escolheu LARGATO'
        case _:
            return 'Computador escolheu SPOCK'