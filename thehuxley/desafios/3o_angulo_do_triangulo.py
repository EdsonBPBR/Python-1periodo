# Escreva um programa em C que o usuário entre com dois ângulos internos de um triângulo e o programa calcule o 3o ângulo do triângulo.

alfa = float(input())
beta = float(input())
teta = 180 - (alfa + beta)

print(f'3o angulo={teta:.6f}')