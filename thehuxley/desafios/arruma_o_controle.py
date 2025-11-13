registros = []# mudei a estrutura para ver se dá certo, inicalmente em lista com dicionário dentro, agora a lista puro
while True:
    try:
        entrada = str(input()).split()
        if entrada[0] == 'INSERIR':
            nome = str(entrada[1])
            registros.append(nome)
    
        elif entrada[0] == 'REMOVER':
            nome = str(entrada[1])
            if nome in registros:
                registros.pop(registros.index(nome))
            
        elif entrada[0] == 'IMPRIMIR':
            print('Atualmente trabalhando:')
            for i in range(len(registros)):
                if len(registros) - 1 == i:
                    print(f"{registros[i]}\n")
                else:
                    print(f"{registros[i]}")
    except:
        break