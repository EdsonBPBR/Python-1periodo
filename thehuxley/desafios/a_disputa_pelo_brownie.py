pontuacao_corin, pontuacao_flame = 0,0

c, f = 0, 0
entrada_vitorias = str(input()).strip().split()
for caractere in entrada_vitorias:
    if caractere == 'c':
        c += 1
    else:
        f += 1
if c > f:
    pontuacao_corin += 40
else:
    pontuacao_flame += 40

entrada_escalacao = str(input()).strip().split()
if int(entrada_escalacao[1]) == 1:
    pontuacao_corin += 20
if int(entrada_escalacao[0]) == 1:
    pontuacao_flame += 20

entrada_gols = str(input()).strip().split()
if int(entrada_gols[0]) > int(entrada_gols[1]):
    pontuacao_flame += 15
else:
    pontuacao_corin += 15

entrada_medias = str(input()).strip().split()
if float(entrada_medias[1]) >= 2:
    pontuacao_flame += 10
if float(entrada_medias[0]) >= 2:
    pontuacao_corin += 10

if pontuacao_flame > pontuacao_corin:
    print('Luiza tem mais chances de comer o brownie')
    print(f'Pontos:{pontuacao_flame}')
    
else:
    print('Pedro tem mais chances de comer o brownie')
    print(f'Pontos:{pontuacao_flame}')