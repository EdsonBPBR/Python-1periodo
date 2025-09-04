#teroura corta papel
#papel cobre pedra
#pedra esmaga largato ---------
#largato envenena spock  ---------
#spock derrete tesoura ---------
#tesoura decapita largato ---------
#largato come papel ------
#papel refuta spock
#spock vaporiza pedra
#pedra quebra tesoura

#iniciei fazendo o pedra papel tesoura normal:
import random, os

while True:
    print('''
    [1] - Pedra, 
    [2] - Papel, 
    [3] - Tesoura, 
    [4] - Largato, 
    [5] - Spock,
    [0] - Sair'''
    )

    jogador1 = int(input('Jogador 1 [1-5]: '))
    jogador2 = random.randint(1, 5)

    os.system('clear')

    match jogador2:
        case 1:
            print('Computador escolheu PEDRA')
        case 2:
            print('Computador escolheu PAPEL')
        case 3:
            print('Computador escolheu TESOURA')
        case 4:
            print('Computador escolheu LARGATO')
        case _:
            print('Computador escolheu SPOCK')

    #todos os casos em que o jogador 1 irá vencer:
    if (jogador1 == 1 and jogador2 == 3) or (jogador1 == 3 and jogador2 == 2) or (jogador1 == 2 and jogador2 == 1) or (jogador1 == 1 and jogador2 == 4) or (jogador1 == 5 and jogador1 == 1) or (jogador1 == 4 and jogador2 == 2) or (jogador1 == 2 and jogador2 == 5) or (jogador1 == 5 and jogador2 == 3) or (jogador1 == 4 and jogador2 == 5):
        print('PARABÉNS! VOCÊ VENCEU!')

    elif jogador1 == jogador2:
        print('Ocorreu um EMPATE!')
    
    elif jogador1 == 0:
        print('SAINDO... ')
        break

    else:
        print('COMPUTADOR VENCEU!')

    input("Pressione ENTER para continuar...")
    os.system('clear')