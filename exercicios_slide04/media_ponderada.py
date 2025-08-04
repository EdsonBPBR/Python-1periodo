numero1 = float(input())
numero2 = float(input())
numero3 = float(input())
numero4 = float(input())

media = (numero1 * 1 + numero2 * 2 + numero3 * 3 + numero4 * 4) / 10
print(media)

#utilizando laço de repetição:
# soma = 0
# contador = 0
# for i in range(1,5):
#     numero = float(input(f'Informe o número {i}:'))
#     soma += numero * i
#     contador += i
# print(f'Média Ponderada: {soma/contador}')

#utilizando funções;

# def MediaPonderada(*numero):
#     soma = 0
#     for numeros in numero:
#         soma += numeros
#     media = soma / len(numero)
#     return soma, media

# print(MediaPonderada(1,2,3,4))
