notas = []

n_vagas = int(input())
n_periodo_cursado = int(input())
entrada_medias = str(input()).split()
somatorio = 0
for valor in entrada_medias:
    somatorio += float(valor)
notas.append((somatorio/n_periodo_cursado, n_periodo_cursado, 'E'))

n_concorrentes = int(input())
for i in range(n_concorrentes):
    try:
        n_periodo = int(input())
        entrada_medias = str(input()).split()
        somatorio = 0
        for valor in entrada_medias:
            somatorio += float(valor)
        notas.append((somatorio/n_periodo, n_periodo, 'C'))
    except:
        break
    
x = sorted(notas, reverse=True, key=lambda x: (x[0], x[1]))
for posicao in range(len(notas)):
    if x[posicao][2] == 'E':
        if posicao+1 <= n_vagas:
            print(f'Matriculado, seu ranking é {posicao+1} dentre as {n_vagas} vagas')
        else:
            print(f'Se não tivesse pago Dominó {n_periodo_cursado}, teria entrado...')