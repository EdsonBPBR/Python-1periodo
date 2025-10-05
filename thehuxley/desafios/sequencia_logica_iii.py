# Escreva um programa que lê 3 números X, Y e Z (X < Y e Z >= 1). Em seguida, o programa exibe uma seqüência de 1 a Y, com valores incrementados pelo valor de Z, passando para a próxima linha a cada X números serem impressos na linha.

dados = str(input()).split()

x = int(dados[0])
y = int(dados[1])
z = int(dados[2])
c = 0

for a in range(1, y+1, z):
    
    if c == x - 1:
        print(a, end='')
    else:
        print(a, end=' ')
    
    c += 1
    
    if c == x:
        print()
        c = 0