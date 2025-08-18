# Escreva um programa que recebe 3 notas de prova e calcula:

# - A média delas

# - A média ponderada delas, considerando pesos 2, 2 e 3

# - A média ponderada delas, considerando pesos 1, 2 e 2

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3
media_ponderada_1 = ((nota1*2) + (nota2*2) + (nota3*3)) / 7
media_ponderada_2 = ((nota1*1) + (nota2*2) + (nota3*2)) / 5

print(f'{media:.2f}')
print(f'{media_ponderada_1:.2f}')
print(f'{media_ponderada_2:.2f}')