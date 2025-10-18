texto = list(str(input()).strip())
indices = []
texto_interno = ''
primeira_parte = ''

for i in range(len(texto)):
    if texto[i] == '[':
        c = i+1
        indices.append(i)
        indices.append(c)
        while texto[c] != ']':
            if texto[c] == ']' or texto[c] == '[':
                c += 1
            else:
                texto_interno += f'{texto[c]}'
                c += 1
                indices.append(c)
                
for j in range(len(texto)):
    if texto[j] == '[' or texto[j] == ']':
        pass
    else:
        if not(j in indices):
            primeira_parte += f'{texto[j]}'

print(texto_interno+primeira_parte)