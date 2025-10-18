# Você deve ler uma sequência de caracteres e imprimir na ordem inversa da leitura.
# Formato de entrada
# Consiste de um inteiro n, indicando quantos caracteres devem ser lidos e uma sequencia de n caracteres. A entrada termina quando n=0.
# Considere que n é sempre n<=100000.

while True:
    tamanho = int(input())
    if tamanho == 0:
        break
    texto = str(input())
    print(texto[::-1])
