# Calcule o comprimento do arco de uma circunferência (a curva AB na figura) e a área do seu setor (delimitado pelo arco e hachurado de cinza na figura) usando os seguintes parâmetros:

def tamanhoArco(angulo, raio, pi = 3.14):
    tamanho_arco = (angulo / 360) * 2 * pi * raio
    
    return tamanho_arco

def areaSetor(angulo, raio, pi = 3.14):
    area_setor = (angulo * pi * (raio**2)) / 360
    
    return area_setor

if __name__ == '__main__':
    raio = float(input())
    angulo = float(input())
    print(f'{tamanhoArco(angulo, raio):.2f}')
    print(f'{areaSetor(angulo, raio):.2f}')
