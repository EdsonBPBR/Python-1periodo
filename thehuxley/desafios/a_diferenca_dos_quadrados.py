# Bernardo é um garoto que adora números e curiosidades matemáticas. Certo dia, enquanto tomava banho (ocasião essa que costuma ser propícia para ter boas ideias), lhe ocorreu uma epifania matemática: todo número ímpar é a diferença de dois quadrados consecutivos.
# Terminada sua sessão de higiene, Bernardo começou a rabiscar suas ideias, observando as propriedades interessantes que os números carregavam:
# 1 - 0 = 1
# 4 - 1 = 3
# 9 - 4 = 5
# 16 - 9 = 7
# 25 - 16 = 9

# repeticao = True
# while repeticao:
#     numero = int(input())
#     if 1 <= numero <= 10000 and numero % 2 != 0 and not(0):
#         contador = 1
#         while contador > 0: #utilizar o while
#             a = contador
#             b = a + 1
            
#             if ((b**2) - (a**2) ) == numero:
#                 print(f'{b**2} - {a**2}')
#                 contador = -1
#             else:
#                 contador += 1
#     else:
#         repeticao = False
            
#utitlizando fóruma matemática:
repeticao = True
while repeticao:
    numero = int(input())
    if numero == 0:
        repeticao = False
    else:
        a = (numero - 1) // 2
        b = a + 1
        print(f"{b**2} - {a**2}")
