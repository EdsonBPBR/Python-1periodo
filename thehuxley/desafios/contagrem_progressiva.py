# Crie um programa que tenha apenas uma função, além do programa principal, que receberá como parâmetro um número natural estritamente positivo n e que exiba, conforme o exemplo de saída, n linhas em que a primeira tem n-n+1 valores n-n+1 com hifens entre eles; a linha seguinte tem n-n+2 valores n-n+2 (novamente com hifens entre eles) e assim por diante até n-n+n. O PROGRAMA PRINCIPAL deverá ler o valor de n e a FUNÇÃO deverá exibir as linhas.

def contagremProgressiva(n):
    for k in range(1,n+1):
        for b in range(1,k+1):
            if b == k:
                print(k, end='')
            else:
                print(k, end='-')
        print()

if __name__ == '__main__':
    n = int(input())
    contagremProgressiva(n)

