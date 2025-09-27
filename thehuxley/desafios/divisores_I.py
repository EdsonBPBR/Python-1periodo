# Ler um número inteiro N e calcular todos os seus divisores.
def divisoresNumero(numero):
    c = 1
    while c <= numero:
        if numero % c == 0:
            print(c)
        
        c += 1

if __name__ == '__main__':
    numero = int(input())
    divisoresNumero(numero)
