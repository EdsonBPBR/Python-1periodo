while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    fitas_dna = []

    for i in range(n):
        fita = str(input()).upper().strip()
        fitas_dna.append(fita)
        
    t = len(fitas_dna)

    # núclo, estrutura de dados principal da questão que criei a parte
    registros = {}
    for i in range(1, t+1):
        if not(fitas_dna[i-1] in registros):
            freq = 0
            for j in range(t):
                soma = j + i
                
                if fitas_dna[i-1] == fitas_dna[soma%t]:
                    freq += 1
                    
                registros[f'{fitas_dna[i-1] }'] = freq-1

    # a lógica da saída agora será aqui
    registro_copias = []
    copia = 0
    for i in range(1,n+1):
        copiados = 0
        for chave in registros.keys():
            if registros[chave] == copia:
                copiados += 1
                
        registro_copias.append(copiados)
        copia += 1

    for resul in registro_copias:
        print(resul)