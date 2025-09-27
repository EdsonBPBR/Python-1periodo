# Você recebe um vetor contendo a altura de cada um dos N prédios que serão construídos e a partir dele vai extrais as seguintes informações:
# - Quantas alturas distintas de prédios existem no total.
# - Quantos prédios são altos, médios e baixos.
# - A diferença de altura do maior e do menor prédio.
# OBS: Um prédio é considerado alto se tem altura >= 100, médio se tem altura >= 50 e pequeno se tem altura < 50.

n = int(input())
entrada = str(input()).split()

n_altos = 0
n_medios = 0
n_baixos = 0
n_diferentes = 0

valores = []

for index in range(n):
    valores.append(int(entrada[index]))

for posicoes in range(n):
    if (valores[posicoes-1]) != valores[posicoes]:
        n_diferentes += 1

    if (valores[posicoes]) >= 100:
        n_altos += 1
    elif (valores[posicoes]) >= 50:
        n_medios += 1
    else:
        n_baixos += 1

maior_predio = max(valores)
menor_predio = min(valores)

if n_diferentes == 0:
    n_diferentes = 1

print(n_diferentes)
print(n_altos)
print(n_medios)
print(n_baixos)
print(maior_predio-menor_predio)