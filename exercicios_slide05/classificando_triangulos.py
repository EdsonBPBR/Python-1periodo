# (Classifica ̧c ̃ao de triˆangulos) Os triˆangulos mais simples s ̃ao classificados de acordo
# com os limites das propor ̧c ̃oes relativas de seus lados. Um triˆangulo equil ́atero
# possui todos os lados iguais, um triˆangulo is ́osceles possui pelo menos dois lados
# iguais e um triˆangulo escaleno as medidas dos trˆes lados s ̃ao diferentes. Crie um
# programa que recebe trˆes valores, correspondendo as medidas dos lados de um
# triˆangulo e informe sua classifica ̧c ̃ao. (Obs.: verifique se os valores fornecidos s ̃ao
# v ́alidos como lados de um triˆangulo)

#1. a + b > c
#2. a + c > b
#3. b + c > a

a = float(input("Informe a medida do lado1: "))
b = float(input("Informe a medida do lado2: "))
c = float(input("Informe a medida do lado3: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print('TRIÂNGULO EQUILÁTERO: possui os três lados iguais')

    elif a == b or a == c or b == c:
        print('TRIÂNGULO ISÓSCELES: possui dois lados iguais')

    else:
        print('TRIÂNGULO ESCALENO: possui todos os lados distintos')
else:
    print('TRIÂNGULO INVÁLIDO')
    