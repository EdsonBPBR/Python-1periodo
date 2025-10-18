m = int(input())
registro = {}

for i in range(m):
    entrada = str(input()).split()
    
    posicao = int(entrada[0])
    caractere = str(entrada[1])
    registro[posicao] = caractere

for i in range(m):
    if i+1 in registro.keys():
        print(registro[i+1], end='')