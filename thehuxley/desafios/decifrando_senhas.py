def calculaBinario(fragmento):
    somatorio = 0 
    i = 0
    for posicao in range(len(fragmento)-1,-1,-1):
        somatorio += int(fragmento[posicao]) *2**i
        i += 1
    return somatorio

def CalculaNumCod(binario):
    codigo_entrada = 0
    k = 0
    c = 4
    num = ''
    for _ in range(len(binario)//4):
        frag = binario[k:c]
        
        if calculaBinario(frag) > 9:
            print('Numero invalido!')
        else:
            num += f'{calculaBinario(frag)}' 
        
        codigo_entrada += calculaBinario(frag)
        k = c
        c += 4
    return num, codigo_entrada

def imprimeSaida(binario, palavras):
    num, codigo_entrada = CalculaNumCod(binario)
    print(f"O codigo de entrada eh: {codigo_entrada}")
    palavras.sort()
    for palavra in palavras:
        print(f'{palavra}{num}')

def main():
    m = int(input())
    palavras = list(str(input()).strip().split())
    try:
        binario = str(input())
        imprimeSaida(binario, palavras)
    except:
        print('Sem bits no momento...')
        
if __name__ == '__main__':
    main()