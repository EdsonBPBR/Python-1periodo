# nota1 = float(input('Informe a primeira nota: '))
# nota2 = float(input('Informe a segunda nota: '))

# def calcula_media(a, b):
#     media = (a+b) / 2
#     if media >= 7 and media <= 9.9 :
#         return 'Aprovado'
#     elif media == 10:
#         return 'Aprovado com Destinção!'
#     else: 
#         return 'Reprovado'

# print(calcula_media(nota1, nota2))


# a = int(input('Informe um número: '))
# b = int(input('Informe outro número: '))
# c = int(input('Informe outra fuck número: '))

# def maior_numero(n1, n2, n3):
#     maior = None
#     if n1 > n2 and n1 > n3:
#         maior = n1
#     elif n2 > n1 and n2 > n3:
#         maior = n2
#     else:
#         maior = n3
        
#     return maior
    
# print(f'Maior número informado foi: {maior_numero(a, b, c)}')


#07
a = int(input(': '))
b = int(input(': '))
c = int(input(': '))

maior  = None
menor = None

if a > b and a > c :
    maior = a
elif b > a and b > c:
    maior = b
else:
    maior = c
    
print(maior)