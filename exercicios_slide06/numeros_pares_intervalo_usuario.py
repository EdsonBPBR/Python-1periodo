# (Numeros pares no intevalo [2,M]) Crie um programa em Python para imprimir
# todos os n ́umeros pares no intevalo [2,M], sendo M informado pelo usuário

limite = int(input('Informe o limite: '))

for pares in range(2, limite, 2):
    print(pares)