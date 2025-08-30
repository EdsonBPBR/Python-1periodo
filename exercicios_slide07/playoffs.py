# O campeonato de basquete norte americano (NBA)  ́e definido em uma
# s ́erie de melhor de sete jogos, ou seja quando um time vence 4 partidas ele  ́e o
# campe ̃ao. Escreva um programa Python que receba como entrada o nome de dois
# times e pergunte a cada jogo qual foi o vencedor e exiba o nome do time campe ̃ao.

nome_time1 = str(input('Nome do Time 1: '))
nome_time2 = str(input('Nome do Time 2: '))

vitorias_time1 = 0
vitorias_time2 = 0

c = 0
while c < 7:
    c += 1
    vencedor_partida = int(input(f'{c}ª partida, [1] - {nome_time1}, [2] - {nome_time2}: '))
    
    if vencedor_partida == 1:
        vitorias_time1 += 1
        
    elif vencedor_partida == 2:
        vitorias_time2 += 1
        
    else:
        print('Entrada Inválida! Anulada!')
        
    #fiquei em ´duvida, é para criar uma estrutura de decisão onde, quando o primeiro time completar os 4 pontos parar o laço de repetição e mostrar o vencedor? Ou aguardar todas as partidas acontecerem?
    
if vitorias_time1 >= 4 or vitorias_time1 > vitorias_time2:
    print(f'{nome_time1} venceu o campeonato!')
    print(f'O time {nome_time1} venceu {vitorias_time1}')
    
elif vitorias_time1 == vitorias_time1:
    print(f'{nome_time1} empatou com {nome_time2}')
    
else:
    print(f'{nome_time2} venceu o campeonato!')
    print(f'O time {nome_time2} venceu {vitorias_time2}')