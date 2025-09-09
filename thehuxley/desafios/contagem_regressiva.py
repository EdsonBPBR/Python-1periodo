# Crie um programa que tenha apenas uma função, além do programa principal, que receberá como parâmetro um número natural estritamente positivo n e que exiba, conforme o exemplo de saída, n linhas em que a primeira tem n valores n com hifens entre eles; a linha seguinte tem n-1 valores n-1 (novamente com hifens entre eles) e assim por diante até n-(n-1). O PROGRAMA PRINCIPAL deverá ler o valor de n e a FUNÇÃO deverá exibir as linha

def contagemregressiva(n = 0):
    while n >= 1:
        c = 0
        while c < n:
            if c + 1 == n:
                print(n, end='')
            else:
                print(n, end = '-')
            c += 1
        print()
        n -= 1
    
if __name__ == '__main__':
    numero = int(input())
    contagemregressiva(numero)
