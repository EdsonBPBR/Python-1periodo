# Escreva um programa que leia um caractere especificando o gênero (M, m, F, f) e imprima o gênero por extenso. Caso o caractere não represente um gênero, imprimir uma mensagem de erro.

x = str(input())

if x.upper() == 'M':
    print('Masculino')

elif x.upper() == 'F':
    print('Feminino')

else:
    print('Genero nao especificado')