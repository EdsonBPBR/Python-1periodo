# Escreva um programa que receba o raio (R) de uma esfera e forneça:
# a) A área da superfície esférica,sabendo que Área Superfície=4πR2
# b) O volume de uma esfera, sabendo que Volume = (4πR3)/3
# Observação: Considere π como tendo o valor 3.1416.
pi = 3.1416

r = float(input("Informe o Raio: "))
area = 4 * pi* r**2
volume = (4 * pi * r**3 ) / 3

print(f'{area:.2f}')
print(f'{volume:.2f}')