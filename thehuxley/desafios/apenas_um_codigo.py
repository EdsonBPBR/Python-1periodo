# Sapo sopa e Shuas são novos desenvolvedores da empresa de alta tecnologia Pi Lagoon e eles foram designados a fazer um serviço braçal por falta de mão de obra, porém como eles queriam na verdade codar, decidiram criar um jogo de pedra, papel e tesoura em um dos computadores da empresa com o intuito de quem perder vai fazer aquele serviço sozinho enquanto o outro apenas relaxa.Para isso foram estabelecidos regras:

#     Eles teriam que escolher quantas rodadas seriam;
#     Números pares seriam equivalente a pedra, ímpares equivalente a tesoura e primos equivalente a papel;

# Obs: sendo o número primo par ou ímpar não importa, ele vai ser considerado papel!
# porém eles não sabiam que quando estabelecido uma repetição algo terrível aconteceria, uma vez que aquele computador utilizado era um protótipo de criação de entidades cósmicas...
def verificaPrimo(n):
    if n <= 1:
        status = False
        return status
    
    if n == 2:
        status = True
        return status
    
    if n % 2 == 0:
        status = False
        return status
    
    c = 0
    for k in range(3, int(n**0.5) + 1, 2): 
        if n % k == 0:
            c = 1
            break
    
    if c > 0:
        status = False
        return status
    else:
        status = True
        return status

if __name__ == '__main__':
    n = int(input())

    c = 0
    placar_jogador_A = 0
    placar_jogador_B = 0

    while n > c:
        entrada = str(input()).split()

        jogador_A = int(entrada[0])
        jogador_B = int(entrada[1])

        # verificar as jogadas do jogador A
        if verificaPrimo(jogador_A):
            A = 'papel'
        
        else: 
            if jogador_A % 2 == 0:
                A = 'pedra'
            else:
                A = 'tesoura'

        # verificar as jogadas do jogador B
        if verificaPrimo(jogador_B):
            B = 'papel'
        
        else: 
            if jogador_B % 2 == 0:
                B = 'pedra'
            else:
                B = 'tesoura'

        # sistema de pontuação
        if (A == 'papel' and B == 'pedra') or (A == 'pedra' and B == 'tesoura') or (A == 'tesoura' and B == 'papel'):
            placar_jogador_A += 1
        
        elif A == B:
            placar_jogador_A = placar_jogador_A
            placar_jogador_B = placar_jogador_B
        
        else:
            placar_jogador_B += 1
            
        c += 1

    if placar_jogador_A > placar_jogador_B:
        print('Sapo sopa esta de boa na lagoa!')

    elif placar_jogador_B > placar_jogador_A:
        print('Testemunhe a verdadeira forca!')

    else:
        print('Impending doom approaches...')