while True:
    try: 
        nome_arquivo = str(input())
        with open(nome_arquivo, "r") as arquivo:
            s = arquivo.read()
            print(s)
    except:
        print('Arquivo não encontrado')
    