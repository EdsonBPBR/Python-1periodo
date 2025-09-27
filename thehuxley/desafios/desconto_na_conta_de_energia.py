# bairro. O programa deve imprimir uma mensagem de erro caso o bairro digitado seja inválido. Além disso, caso a renda da pessoa caia fora das faixas da tabela, não haverá desconto. Se a renda OU o consumo forem valores negativos, deve ser emitida uma mensagem de erro.

# O programa deve ler o código do bairro (S: Santa Ana; I: Industriários; T: Tabatinga), a renda da família e o consumo em reais e obter o desconto de acordo com a tabela abaixo:
def calculaDesconto(bairro, renda, consumo):
    if bairro == 'S' and (50 <= renda <= 500):
        return consumo - 50
    
    elif bairro == 'S' and (500 < renda <= 1000):
        return consumo - 25
    
    elif bairro == 'I' and (240 < renda <= 1000):
        return consumo - 240
    
    elif bairro == 'I' and (1000 < renda <= 5000):
        return consumo - 120
    
    elif bairro == 'T' and (5000 < renda <= 10000):
        return consumo - 720
    
    elif bairro == 'T' and (10000 < renda <= 20000):
        return consumo - 360
    
    else:
        return consumo 


if __name__ == '__main__':
    bairro = str(input()).upper()

    if bairro == 'S' or bairro == 'I' or bairro == 'T':
        renda = int(input())
        consumo = int(input())

        if renda >= 0 and consumo >= 0:
            print(calculaDesconto(bairro, renda, consumo))
        else:
            print('Renda e consumo nao podem ser negativos.')
    else:
        print('Bairro invalido.')
