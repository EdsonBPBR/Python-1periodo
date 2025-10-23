avioes = str(input()).strip().split()

for indices, valores in enumerate(avioes):
    print(f'{valores}({indices+1}) = {avioes[int(valores)-1]}({avioes[indices]})')