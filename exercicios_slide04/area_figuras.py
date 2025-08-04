#calculo àrea do triangulo:
base = float(input('Base do Triângulo: '))
altura = float(input('Altura do Triângulo: '))
#print(f'Área Triângulo: {(base*altura)/2}')

#calculo àrea do quadrado:
lado = float(input('Lado do Quadrado: '))
#print(f'Área do Quadrado: {lado**2}')

#calculo àrea do retangulo:
largura = float(input('Largura do Retângulo: '))
h = float(input('Altura do Retângulo: '))
#print(f'Área do Retângulo: {largura*h}')


def AreaFiguras(base, altura, lado, largura, h):
    return f'{base * altura} {lado ** 2} {largura * h}'

print(AreaFiguras(base, altura, lado, largura, h))