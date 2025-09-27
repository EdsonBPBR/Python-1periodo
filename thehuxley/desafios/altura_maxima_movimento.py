# Um objeto é lançado a um ângulo (theta) em relação ao solo, com uma velocidade inicial v (em m/s), num planeta com gravidade g. Construa um programa que leia o ângulo (theta) em graus, a velocidade v e a gravidade g e calcule a altura máxima h em metros alcançada pelo objeto, e em seguida exiba (imprima) o resultado h na saída do programa.

from math import sin,radians #sin trabalha com radianos, é necessário antes converter o ângulo para graus

def alturaMaxima(angulo, velocidade, gravidade):
    h = ((velocidade**2)*(sin(radians(angulo)))**2)/ (2*gravidade)
    return h

if __name__ == '__main__':
    angulo = float(input())
    velocidade = float(input())
    gravidade = float(input())
    print(alturaMaxima(angulo, velocidade, gravidade))