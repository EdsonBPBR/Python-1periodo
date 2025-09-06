# Escreva um programa que leia os valores (reais) dos raios de dois círculos diferentes e informe qual dos dois possui área maior ou se possuem a mesma área.

def area_circulo(raio, pi = 3.14):
    area = (raio ** 2) * pi
    return area

r1 = float(input())
r2 = float(input())

if area_circulo(r1) > area_circulo(r2):
    print('Primeiro circulo')

elif area_circulo(r1) < area_circulo(r2):
    print('Segundo circulo')

else:
    
    print('Iguais')