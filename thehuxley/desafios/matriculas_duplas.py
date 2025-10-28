matri_prog_ii = []
entrada_prog_ii = str(input()).split()
for matricula in entrada_prog_ii:
    matri_prog_ii.append(int(matricula))

matri_prog_iii = []
entrada_prog_iii = str(input()).split()
for matricula in entrada_prog_iii:
    matri_prog_iii.append(int(matricula))

indices = []
for i in range(len(matri_prog_ii)):
    for j in range(len(matri_prog_iii)):
        if matri_prog_ii[i] == matri_prog_iii[j]:
            indices.append(i)

for posicao in indices:
    print(matri_prog_ii[posicao], end = ' ')