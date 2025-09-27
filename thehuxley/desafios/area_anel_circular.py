# Escreva um programa para calcular e mostrar a área de um anel circular cujos raios interno e externo são dados de entrada.
def areaCircular(dados):
    pi = 3.141594
    raio_interno = float(dados[0])
    raio_externo = float(dados[1])

    area = pi*((raio_externo**2)-(raio_interno**2))

    return f'{area:.2f}'

if __name__ == '__main__':
    dados = str(input()).split()
    print(areaCircular(dados))
