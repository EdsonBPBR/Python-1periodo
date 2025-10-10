# Crie um programa que solicite as dimens ̃oes de uma matriz 4x4 e realize a impress ̃ao
# desta de forma organizada

matriz = []

# receber os elementos
for i in range(4):
    linha = []
    for j in range(4):
        elemento = int(input(f"a({i+1},{j+1}): ")) 
        linha.append(elemento)
    matriz.append(linha)

# impressao da lista
for i in range(4):
    linha = "|"
    for j in range(4):
        linha += " " + f"{matriz[i][j]}"
    linha += " |"

    print(linha)