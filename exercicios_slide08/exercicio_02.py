import math

angulo = float(input('Informe o valor em graus: '))
radianos = math.radians(angulo)

print(round(math.cos(radianos), 2))
print(round(math.sin(radianos), 2))