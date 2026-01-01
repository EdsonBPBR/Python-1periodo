def verifica_primo(n):
    if n == 2:
        status = True
        return status
    
    if n <= 1 or n % 2 == 0:
        return False
    
    for k in range(3, int(n**0.5) + 1, 2): 
        if n % k == 0:
            return False
    return True

def monta_matriz(n):
    matriz = []    
    for i in range(n):
        linha = []
        entrada = str(input()).split()
        for caractere in entrada:
            linha.append(int(caractere))
        matriz.append(linha)
    return matriz

def verifica_lutas(matriz, n, m):
    primos = 0
    n_primo = 0
    
    for i in range(n):
        somatorio = 0
        for j in range(m):
            somatorio += matriz[i][j]
        if verifica_primo(somatorio):
            primos += 1
        else:
            n_primo += 1
    return primos, n_primo

def main():
    n, m = map(int, input().split())
    if (n > 0 and n <= 10) and (m > 0 and m <= 10):
        matriz = monta_matriz(n)
        primos, n_primo = verifica_lutas(matriz, n, m)
                
        if primos > n_primo:
            print('Chama')
        else:
            print('Não chama')
    else:
        print('Han??')

if __name__ == '__main__':
    main()