#(Zerinho ou um) Crie um programa que determine se existe vencedor para uma
#partida de ’zerinho ou um’ disputada entre três pessoas:
from random import randint

#para dois jogadores: (1,0), (0, 1), (0, 0) ou (1, 1)

# a = int(input('1º JOGADOR (1-0): '))
# b = int(input('2º JOGADOR (1-0): '))

# a = randint(0,1)
# b = randint(0,1)

#print(a, b)
# print('-'*20)

# if a != b:
#     if a ==1:
#         print('1º JOGADOR')
#     elif b == 1:
#         print('2º JOGADOR')
#     else:
#         print('VALOR INVÁLIDO')
# else:
#     print('EMPATE')

#para três jogadores
a = randint(0,1)
b = randint(0,1)
c = randint(0,1)

# válidos: (0,0,1), (1,0,0), (0,1,0), inválidos: (1,1,0), (1,0,1), (0,1,1), (1,1,1), (0,0,0)
print(a, b, c)

if a == b == 1 or b == c == 1 or a == c == 1:
    print('TENTAR NOVAMENTE')
elif a == b == c:
    print('EMPATE, TENTAR NOVAMENTE')
else:
    if a == 1:
        print('JOGADOR 1 VENCEU!')
    elif b == 1:
        print('JOGADOR 2 VENCEU!')
    elif c == 1:
        print('JOGADOR 3 VENCEU!')
    else:
        print('VALOR INVÁLIDO!')