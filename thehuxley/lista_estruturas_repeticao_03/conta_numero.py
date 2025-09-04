# Você deve fazer um programa para contar a quantidade de vezes que um determinado número Y aparece entre uma sequência de números lidos. Primeiro, você deve ler o número inteiro Y, depois você deve ler, no máximo, mais 20 números inteiros.

# Caso o valor -1 seja lido, você deve interromper a entrada.

# Ao final, você deve informar:

#     Quantas vezes o número Y apareceu entre os números lidos;
#     A média dos valores lidos que forem maiores que zero e que estejam fora do intervalo fechado [15,20].

valor_comparativo = int(input())
freq_valor_igual = 0
c = 0
denominador = 0
soma = 0

while True:
    c += 1
    
    if c > 20:
        break
    
    numero = int(input())
    
    if numero == -1:
        break
    
    #contar os números iguais ao número informado pelo usuário
    if numero == valor_comparativo:
        freq_valor_igual += 1
    
    #calcular a média dos números maiores que 0 e fora do intervalo fechado [15,20]
    if (numero > 0) and (not(numero >= 15 and numero <= 20)):
        denominador += 1
        soma += numero
    
print(f'O número {valor_comparativo} apareceu {freq_valor_igual} vez(es)')

if denominador != 0:
    media = soma / denominador
    print(f'A média dos números foi de: {media:.2f}')
else:
    print('Sem valores para calcular a média')
