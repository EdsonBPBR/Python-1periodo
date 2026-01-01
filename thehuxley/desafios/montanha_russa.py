registros = []
while True:
    n = int(input())
    if n == -1:
        break
    registros.append(n)
m = int(input())

try:
    print(f'O bilhete sorteado e o {m} e esta no carrinho {registros.index(m)+1}')
except:
    print('Nenhum carrinho foi sorteado')