n = int(input())
x = 0
y = 0
freq = 0
lado_atual = None  

for i in range(n):
    direcao = str(input()).strip().upper()
    
    x_antes = x
    y_antes = y

    if direcao == 'D':
        x += 1
    elif direcao == 'C':
        y += 1
    
    if y_antes > x_antes:
        lado_antes = 'cima'
    elif y_antes < x_antes:
        lado_antes = 'baixo'
    else:
        lado_antes = 'na_muralha'
        
    if y > x:
        lado_depois = 'cima'
    elif y < x:
        lado_depois = 'baixo'
    else:
        lado_depois = 'na_muralha'
    
    if lado_antes != 'na_muralha' and lado_depois != 'na_muralha' and lado_antes != lado_depois:
        freq += 1

print(freq)