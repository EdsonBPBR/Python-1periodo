# Tendo em vista que todos os computadores trabalham na base binária e nós utilizamos usualmente a base decimal, faz-se necessário saber converter binário para decimal e vice-versa. 

def binario_para_decimal(binario, lista_binario = [], decimal = 0):
    c = 0
    for elementos in binario:
        lista_binario.append(elementos)    

    lista_binario.reverse()
    for b in lista_binario:
        numero = int(b)
        decimal += (numero * 2 ** c)
        
        c+= 1
    return decimal

if __name__ == '__main__':
    binario = str(input())
    print(binario_para_decimal(binario))
