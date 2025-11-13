from math import fabs

somatorio = 0
produtorio = 1

for _ in range(5):
    nome = str(input()).strip()
    idade = int(fabs(float(input())))
    
    print(f'Pessoa: {nome} , {idade}')
    somatorio += idade
    produtorio *= idade
    
print(somatorio)
print(f'{(somatorio/5):.1f}')
print(int(produtorio**(1/5)))