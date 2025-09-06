# Este mês ocorre o Mundial de Tiro Ao Alvo e as competições ocorrem em duas etapas. Para se classificar para a segunda etapa, cada competidor precisa somar pelo menos 100 pontos ao longo de 6 partidas. Escreva um programa que receba como entrada os pontos feitos por um competidor em cada uma das partidas da primeira etapa, e exiba uma mensagem informando se ele foi classificado ou não.

def somapontos():
    c = 0
    soma_pontos = 0
    while c < 6:
        pontos = int(input())
        soma_pontos += pontos
        c += 1
        
    return soma_pontos

def verifica_resultado(soma_pontos):
    if soma_pontos >= 100:
        return 'Classificado'
    else:
        return 'Eliminado'

if __name__ == '__main__':
    print(verifica_resultado(somapontos()))
