# Crie um programa que solicite as dimens ̃oes de uma matriz 2x2 e realize a impress ̃ao
# desta de forma organizada


matriz = [
    
]

# entrada elementos lista
for i in range(2):
    linha = []
    for j in range(2):
        elemento = int(input(f"a({i},{j}): "))
        linha.append(elemento)
    matriz.append(linha)

# impressao da matriz
for i in range(2):
    linha = "|"
    for j in range(2):
        linha += " " + str(matriz[i][j])
    linha += " |"

    print(linha)