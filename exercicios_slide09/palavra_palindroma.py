# Seja fornecida uma string, informe se ela  ́e um pal ́ındromo (leitura de frente para
# tr ́as e de tr ́as para frente  ́e a mesma)

texto = str(input())
texto_invertido = ''

for elemento in range(len(texto)-1, -1, -1):
    texto_invertido += f'{texto[elemento]}'

if texto == texto_invertido:
    print(f'É um palíndromo, pois: {texto} = {texto_invertido}')
else:
    print(f'NÃO é um palíndromo, pois: {texto} != {texto_invertido}')