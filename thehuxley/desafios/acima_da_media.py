# Dados três números em ponto flutuante queremos saber quantos deles estão acima da média aritmética.
n1 = float(input('Informe 1º número: '))
n2 = float(input('Informe 2º número: '))
n3 = float(input('Informe 3º número: '))

media = (n1 + n2 + n3) / 3
acima_da_media = 0

if n1 > media:
    acima_da_media += 1

if n2 > media:
    acima_da_media += 1

if n3 > media:
    acima_da_media += 1

print(acima_da_media)

#utilizando laco de repeticao:
# contador = 0
# soma = 0
# acima_da_media = 0
# while contador < 3:
#     n = float(input())
#     soma += n
#     contador += 1

#     media = soma / contador
#     print(media)
    
#     if n > media:
#         acima_da_media += 1
#     else:
#         continue
# print(acima_da_media)

