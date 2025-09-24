def verificaPrimo(n):
    c = 0
    
    if n == 0 or n == 1:
        status = False
        
    else:
        if n > 2:
            if n % 2 == 0:
                c = 1
            else:
                for k in range(3, n):
                    if n % k == 0:
                        c += 1
        if c > 0:
            status = False
        else:
            status = True

    return status

n = int(input())
c = 0

placar_jogador1 = 0
placar_jogador2 = 0

while n > c:
    entrada = str(input()).split()
    jogador1 = int(entrada[0])
    jogador2 = int(entrada[1])

    if verificaPrimo(jogador1):
        ocp_jog1 = 'papel'
    else:
        if jogador1 % 2 == 0:
            ocp_jog1 = 'pedra'
        else:
            ocp_jog1 = 'tesoura'

    if verificaPrimo(jogador2):
        ocp_jog2 = 'papel'
    else:
        if jogador2 % 2 == 0:
            ocp_jog2 = 'pedra'
        else:
            ocp_jog2 = 'tesoura'


    if (jogador1 == 'papel' and jogador2 == 'pedra') or (jogador1 == 'pedra' and jogador2 == 'tesoura') or (jogador1 == 'tesoura' and jogador2 == 'papel'):
        placar_jogador1 += 1
    
    elif jogador1 == jogador2 == 'papel' or jogador1 == jogador2 == 'pedra' or jogador1 == jogador2 == 'tesoura':
        placar_jogador1 = placar_jogador1
        placar_jogador2 = placar_jogador2

    else:
        placar_jogador2 += 1
    c += 1

if placar_jogador1 > placar_jogador2:
    print('Testemunhe a verdadeira forca!')

elif placar_jogador1 == placar_jogador2:
    print('Impending doom approaches...')

else:
    print('Sapo sopa esta de boa na lagoa!')
    