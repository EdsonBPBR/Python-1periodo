def maior_numero(n1, n2):
    if n1 >= n2:
        return n1
    else:
        return n2
    
n1 = float(input())
n2 = float(input())

resultado = maior_numero(n1, n2)

print(f'O maior valor informado foi: {resultado}')
