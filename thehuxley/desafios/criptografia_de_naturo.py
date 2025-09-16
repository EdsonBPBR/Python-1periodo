# Naruto está desenvolvendo um sistema de criptografia que consiste em mapear cada letra do alfabeto naquela referente à sua posição de trás para frente.
# Vamos ajuda-lo a escrever esse sistema. Para isso vamos escrever uma função que recebe uma frase de tamanho não-nulo e retorna uma frase.  

entrada = str(input())
frase = list(entrada)
frase_criptografada = ''

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

for posicao in range(len(frase)):
    index = int(alfabeto.index(f'{frase[posicao % 26]}'))

    novo_caractere = f'{alfabeto[index-1]}'
    if novo_caractere == ' ':
        continue

    frase_criptografada += novo_caractere

print(frase_criptografada)