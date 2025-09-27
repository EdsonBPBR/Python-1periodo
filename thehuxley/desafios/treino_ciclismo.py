# Eloi decidiu se dedicar à prática de ciclismo para manter a forma. Ele traçou como meta percorrer pelo menos 8 km por dia todos os dias.

# Escreva um programa que receba como entrada a distância percorrida por Eloi em cada um dos sete dias da semana e, de acordo com seu desempenho, exiba uma das seguintes mensagens:

# - Desempenho otimo, caso a meta seja cumprida em cinco ou mais dias
# - Desempenho razoavel, caso a meta só seja cumprida em três ou quatro dias
# - Desempenho ruim, caso a meta seja cumprida em menos de três dias

n_dia = 0

c = 0
while c < 7:
    distancia = float(input())
    
    if distancia >= 8:
        n_dia += 1

    c += 1

if n_dia < 3:
    print('Desempenho ruim')

elif n_dia >= 3 and n_dia <= 4:
    print('Desempenho razoavel')

elif n_dia >= 5:
    print('Desempenho otimo')