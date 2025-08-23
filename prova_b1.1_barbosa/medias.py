nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))
nota3 = float(input('Informe a nota 3: '))

media = (nota1 + nota2 + nota3) / 3
media_ponderada_1 = ((nota1 * 2) + (nota2 * 2) + (nota3 * 3)) / 7

media_ponderada_2 = ((nota1 * 1) + (nota2 * 2) + (nota3 * 2)) / 5

print(f'Média: {media:.3f}')
print(f'Média Ponderada 1: {media_ponderada_1:.3f}')
print(f'Média Ponderada 2: {media_ponderada_2:.3f}')

print(f'{media:.3f} {media_ponderada_1:.3f} {media_ponderada_2:.3f}')