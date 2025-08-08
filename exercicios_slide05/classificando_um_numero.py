numero = int(input('Informe um número: '))

if (numero % 2 == 1) and (numero > 0):
    print(f'{numero} é ímpar e é positivo')

elif (numero % 2 == 1) and (numero < 0):
    print(f'{numero} é ímpar e é negativo')

elif (numero % 2 == 1) and (numero == 0):
    print(f'{numero} é ímpar e nulo')

elif (numero % 2 == 0) and (numero > 0):
    print(f'{numero} é par e positivo')

elif (numero % 2 == 0) and (numero < 0):
    print(f'{numero} é par e negativo')

else:
    print(f'{numero} é par e nulo')