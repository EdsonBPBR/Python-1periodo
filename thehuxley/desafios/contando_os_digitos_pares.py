# Escreva uma função recursiva chamada ContaDigitosPares que receba como entrada um número e retorne a quantidade de dígitos pares que o compõem.
# Ex: 234 tem 3 dígitos, mas apenas 2 são pares

def digitosPares(numero):
    numero_listados = list(numero)
    n_pares = 0

    for a in numero_listados:
        elemento_lista = int(a)
        
        if elemento_lista % 2 == 0:
            n_pares += 1

    return n_pares

if __name__ == '__main__':
    n = str(input())
    print(digitosPares(n))