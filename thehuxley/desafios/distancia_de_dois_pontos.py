coordenadas = str(input()).split()

xa = int(coordenadas[0])
ya = int(coordenadas[1])
xb = int(coordenadas[2])
yb = int(coordenadas[3])

d = ((xb-xa)**2 - (yb-ya)**2)**(0.5)
print(f'{int(d)}')