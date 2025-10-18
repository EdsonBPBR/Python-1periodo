# primeiramente eu vou começar calculando um log
def calculaLog(log):
    c = 0
    while True:
        c += 1
        if 2**c == log:
            return (c)

registros = {}

n = int(input())
for i in range(n):
    binario = str(input()).strip()
    log = len(binario)

    tamanho_posicao = calculaLog(log)
    tamanho_id = len(binario)-tamanho_posicao
    c = 0
    somatorio = 0
    for a in (binario[:tamanho_posicao])[::-1]:
        somatorio += int(a) * 2 ** c
        c += 1
        
    posicao = somatorio

    id = binario[tamanho_posicao:(len(binario))]

    if not(posicao in registros.keys()):
        registros[posicao] = id    
    else:
        c = 0
        while (c in registros.keys()):
            c += 1
        registros[c] = id

    # print(registros)
    # print(registros.keys())
    # converter de id de binário para decimal
    
m = int(input())
for m in range(m):
    posicao = int(input())
    
    if (posicao in registros.keys()):
        print(registros[posicao])
    else:
        print('Nao tem ninguem')
