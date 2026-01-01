registros = []
while True:
    entrada = str(input()).split()
    if entrada[0] == '9999':
        break
    
    contagem_n_T = 0
    for fita in entrada[1]:
        if fita == 'T':
            contagem_n_T += 1
    registros.append((contagem_n_T, entrada[0]))
    
print(max(registros)[1])