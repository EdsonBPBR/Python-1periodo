matriz = {
    (0,0): 1,
    (0,1): 2,
    (1,0): 3,
    (1,1): 4
}

chaves = matriz.keys()

for c in chaves:
    print(f'a({c[0]}, {c[1]}) : {matriz[c]}')