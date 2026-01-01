registros = []

while True:
    try:
        entrada = input().split()
        if not entrada: 
            continue
        if entrada[0] == 'INSERIR':
            registros.append(entrada[1])
        elif entrada[0] == 'REMOVER':
            registros.remove(entrada[1])
        elif entrada[0] == 'IMPRIMIR':
            print('Atualmente trabalhando:')
            for nome in registros:
                print(nome)
            print()
    except EOFError:
        break
    except ValueError:
        continue