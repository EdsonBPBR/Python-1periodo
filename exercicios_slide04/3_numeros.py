# obs: não utilizar array (listas)

n1 = int(input('n1: '))
n2 = int(input('n2: '))
n3 = int(input('n3: '))

menor = maior = meio = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
    
if menor < n2 < maior:
    meio = n2

if menor < n3 < maior:
    meio = n3

print(menor, meio, maior)