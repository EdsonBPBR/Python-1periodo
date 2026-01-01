x, y = map(float, input().split())
n = int(input())
input()

registros = []
sequencia = []

for _ in range(n):
    entrada = str(input()).split()
    
    registros.append([float(entrada[1]), 
                     float(entrada[2]), 
                     float(entrada[4]), 
                     entrada[3], 
                     entrada[0]])

print(registros)
lista = []
for posicao, i in enumerate(registros):
    d = ((i[0]-x)**2 + (i[1]-y)**2) ** (1/2) # fórmula de GA para calcular distância entre dois pontos
    p = i[2]
    lista.append((posicao, d, p))
