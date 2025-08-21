# (Numeros pares no intevalo [N,M]) Crie um programa em Python para imprimir
# todos os n ́umeros pares no intevalo [N,M], sendo N e M informados pelo usu ́ario

n = int(input('Informe o inicio: '))
m = int(input('Informe o limite: '))

for pares in range(n, m, 2):
    print(pares)