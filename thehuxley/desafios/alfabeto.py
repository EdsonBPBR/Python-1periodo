# escreva um programa que receba letras separadas por espaço até o eof e então printe todas elas ordenadas!

entrada = str(input()).split()
entrada.sort()

for elemento in range(len(entrada)):
    if elemento + 1 == len(entrada) + 1:
        print(f'{entrada[elemento]}', end='')
        
    print(f'{entrada[elemento]}', end=' ')

print()