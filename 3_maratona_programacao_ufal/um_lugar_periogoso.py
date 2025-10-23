n = int(input())
for _ in range(n):
    somatorio = 0
    for i in range(10):
        linha = str(input()).strip()
        for indice, valor in enumerate(linha): # linha
            if valor == 'X':
                if (i == 0 or i == 9) or (indice == 0 or indice == 9) :
                    somatorio += 1
                elif (i == 1 or i == 8) or (indice == 1 or indice == 8):
                    somatorio += 2
                elif (i == 2 or i == 7) or (indice == 2 or indice == 7):
                    somatorio += 3
                elif (i == 3 or i == 6) or (indice == 3 or indice == 6):
                    somatorio += 4
                elif (i == 4 or i == 5) or (indice == 4 or indice == 5):
                    somatorio += 5
            else:
                somatorio += 0
    print(somatorio)