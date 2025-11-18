while True:
    n = int(input())
    if n == 0:
        break
    agrupado = {}

    for _ in range(n):
        nome = input().strip()
        entrada = input().split()
        cor = entrada[0]
        tamanho = entrada[1]
        
        if cor not in agrupado:
            agrupado[cor] = []
        agrupado[cor].append((tamanho, nome))

    cores_ordenadas = sorted(agrupado.keys())

    for cor in cores_ordenadas:
        agrupado[cor].sort(key=lambda x: ({'P': 1, 'M': 2, 'G': 3}[x[0]], x[1]))
        
        for tamanho, nome in agrupado[cor]:
            print(f"{cor} {tamanho} {nome}")
    
    print()
    