# No próximo fim-de-semana, Cristina vai sair com seus 6 primos, mas eles ainda não resolveram se vão ao cinema ou ao boliche. Escreva um programa que receba como entrada o passeio escolhido por cada um e exiba ao final aquele que teve mais votos.

if __name__ == '__main__':
    c = 0
    cinema = 0
    boliche = 0

    while c < 7:
        escolha = str(input()).upper()

        if escolha == 'CINEMA':
            cinema += 1
        elif escolha == 'BOLICHE':
            boliche += 1
        else:
            print('VALOR DE ENTRADA INVÁLIDO!')

        c += 1

    if cinema > boliche:
        print('CINEMA')

    else:
        print('BOLICHE')