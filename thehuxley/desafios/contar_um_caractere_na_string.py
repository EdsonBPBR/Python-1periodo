# Faça um programa para ler uma string e um caracter qualquer e calcule o número de ocorrências desse caracter na string. Exemplo: Seja a string "maracatu" e o caracter 'a', então o número de ocorrências é 3.

texto = str(input())
busca = str(input())

c = 0
for posicao in range(len(texto)):
    if texto[posicao] == busca:
        c += 1

print(c)