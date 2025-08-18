# Faça um programa que indique se um número que o usuário digitou é divisível por 4 e por 7 ao mesmo tempo mas não divisível por 5.

# A saída deve ser um mensagem 'sim' ou 'nao' (minúsculos e sem o til).

numero = int(input('Informe um número: '))
if (numero % 4 == 0 and numero % 7 == 0) and (numero % 5 != 0):
    print('sim')
else:
    print('nao')