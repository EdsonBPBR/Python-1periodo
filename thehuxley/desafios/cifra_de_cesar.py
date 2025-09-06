# O método de César é um dos sistemas de encriptação mais antigos do mundo, consiste na substituição de uma letra N do alfabeto para uma letra (N + K) onde K é um número inteiro constante (César utilizava K = 3). 
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

def cifraCesar(palavra, chave):
    cifrado = ''
    lista_frase = list(palavra)
    
    for x in lista_frase:
        b = (alfabeto.index(f'{x}'))
        cifrado += alfabeto[b+chave]
        
    return cifrado
    
if __name__ == '__main__':
    frase = str(input()).lower()
    k = int(input())

    print(cifraCesar(frase, k))