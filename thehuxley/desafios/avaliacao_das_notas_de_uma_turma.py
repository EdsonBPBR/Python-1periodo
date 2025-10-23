registros = {}
pontuacoes = []

while True:
    try:
        entrada = str(input()).upper().split()
        if entrada == '*':
            break
        else:
            registros[entrada[0]] = entrada[1]
    except:
        break

gabarito = str(input()).upper().strip()
for chave in registros.keys():
    c = 0
    for i in range(5):
        if registros[chave][i] == gabarito[i]:
            c += 1
    pontuacoes.append(c)

print(f'Maior: {max(pontuacoes)}')
print(f'Menor: {min(pontuacoes)}')
media = sum(pontuacoes) / len(registros)
print(f'Media: {media:.2f}')