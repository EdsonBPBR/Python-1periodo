# Faça um programa que imprima todos os números ímpares entre dois números dados.

def verificaNumero(numero):
    if numero % 2 != 0:
        print(numero) 
    else:
        pass

if __name__ == '__main__':
    inicio = int(input())
    fim = int(input())

    for numero in range(inicio, fim+1):
        verificaNumero(numero)