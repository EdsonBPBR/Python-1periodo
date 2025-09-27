# Escreva um programa que calcula a distância d entre dois pontos A e B no espaço, isto é, com coordenadas (x, y, z) e calcule a distância entre eles usando a fórmula: 

def distanciaPontoEspacial(xa, ya, za, xb, yb, zb):
    dAB = ((xb-xa)**2 + (yb-ya)**2 + (zb-za)**2) ** (1/2)

    return dAB

xa = float(input())
ya = float(input())
za = float(input())

xb = float(input())
yb = float(input())
zb = float(input())

print(f'{distanciaPontoEspacial(xa, ya, za, xb, yb, zb):.16f}')