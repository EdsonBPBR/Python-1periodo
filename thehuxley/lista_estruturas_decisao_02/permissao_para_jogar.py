# Uma plataforma online oferece 4 tipos de jogos, onde Cada um desses tipos de jogo tem uma faixa etária para que o jogador possa participar.

#     Jogos de azar - Apostas esportivas, blackjack, roleta e afins.
#         21 anos ou mais
#     MMORPG - Massively Multiplayer Online Role-Playing Game
#         14 anos ou mais
#     MOBA - Multiplayer Online Battle Arena
#         10 anos ou mais
#     Casual
#         Sem limite de idade

# Faça um programa que receba a idade do jogador e o tipo de jogo que ele deseja jogar e informe se ela pode jogar. Caso a idade do jogador caia fora do intervalo válido ou seja informado um tipo de jogo que não existe, deve ser emitida uma mensagem de erro de acordo com o que aconteceu.

idade = int(input('Informe sua idade: '))
jogo = input('Informe o jogo: ')

if idade >= 0 and idade <= 130:
    if jogo == 'azar' or jogo == 'mmorpg' or jogo == 'moba' or jogo == 'casual':

        if (jogo == 'azar' and idade >= 21) or  (jogo == 'mmorpg' and idade >= 14) or (jogo == 'moba' and idade >= 10) or (jogo == 'casual'):
            print('Pode entrar!')
        else:
            print('Volte daqui há alguns anos.')
        
    else:
        print('Jogo invalido.')
else:
    print('Idade invalida.')