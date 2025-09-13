# A tabela de penalizações para quem ultrapassar esse limite é:
# Velocidade até 20% superior ao permitido: multa de R$ 85.13 e 4 pontos na carteira;
# Velocidade maior que 20% e até 50% acima do permitido: multa de R$ 127.69 e 5 pontos na carteira;
# Velocidade acima de 50% do permitido: multa de R$ 574.62 , 7 pontos na carteira, apreensão da carteira e suspensão do direito de dirigir.

def multaPunicao(velocidade_minima_permitida, velocidade_veiculo):
    if velocidade_minima_permitida < velocidade_veiculo <= velocidade_minima_permitida * 1.2:
        multa = 85.13
        pontos = 4

    elif velocidade_minima_permitida * 1.2 < velocidade_veiculo <= velocidade_minima_permitida * 1.5:
        multa = 127.69
        pontos = 5

    elif velocidade_veiculo > velocidade_minima_permitida * 1.5:
        multa = 574.62
        pontos = 7

    else:
        multa = 0.00
        pontos = 0
        
    return multa, pontos


if __name__ == '__main__':
    velocidade_minima_permitida = float(input())
    velocidade_veiculo = float(input())
    
    multa, pontos = multaPunicao(velocidade_minima_permitida, velocidade_veiculo)
    
    print(f'{multa:.2f}')
    print(f'{pontos}')
