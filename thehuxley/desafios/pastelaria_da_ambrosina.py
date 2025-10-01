def precoPastel(dados_pastel, preco_ingredientes):
    preco_pastel = (float(dados_pastel[0]) * float(preco_ingredientes[0])) + (float(dados_pastel[1]) * float(preco_ingredientes[1])) + (float(dados_pastel[2]) * float(preco_ingredientes[2])) + (float(dados_pastel[3]) * float(preco_ingredientes[3]))
    
    return preco_pastel

def precoEmpada(dados_empada, preco_ingredientes):
    preco_empada = (float(dados_empada[0]) * float(preco_ingredientes[0])) + (float(dados_empada[1]) * float(preco_ingredientes[1])) + (float(dados_empada[2]) * float(preco_ingredientes[2])) + (float(dados_empada[3]) * float(preco_ingredientes[3]))
    
    return preco_empada

def precoKibe(dados_kibe, preco_ingredientes):
    preco_kibe = (float(dados_kibe[0]) * float(preco_ingredientes[0])) + (float(dados_kibe[1]) * float(preco_ingredientes[1])) + (float(dados_kibe[2]) * float(preco_ingredientes[2])) + (float(dados_kibe[3]) * float(preco_ingredientes[3]))
    
    return preco_kibe

if __name__ == '__main__':
    dados_pastel = str(input()).split()
    dados_empada = str(input()).split()
    dados_kibe = str(input()).split()
    preco_ingredientes = str(input()).split()

    print(f'{precoPastel(dados_pastel, preco_ingredientes):.2f}')
    print(f'{precoEmpada(dados_empada, preco_ingredientes):.2f}')
    print(f'{precoKibe(dados_kibe, preco_ingredientes):.2f}')