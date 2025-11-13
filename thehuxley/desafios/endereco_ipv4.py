endereco = list(str(input("Endereço: ")).strip().split('.'))

# validar endereço:
def validarEndereco(entrada_endereco):
    if len(entrada_endereco) == 4:
        for i in range(len(entrada_endereco)):
            if int(entrada_endereco[i]) >= 0 and int(entrada_endereco[i]) <= 255:
                continue
            else: 
                return False
        return True
    else:
        return False

if validarEndereco(endereco):
    mascara = int(input('Máscara: '))
    
    # calculo endereços por subrede
    n_sub_redes = 2**(mascara % 4)
    n_end_brutos_sub = 2**(32-mascara)
    print(n_sub_redes)
    print(n_end_brutos_sub)
    
    # ainda falta fazer a distribuição de endereços IP
    
    
    

    # print(endereco[mascara // 8])
    
    
    
else:
    print('Endereço IPv4 Inválido!')