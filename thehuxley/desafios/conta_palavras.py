# Fazer um programa para ler uma string e calcular o número de palavras que ele contém. Exemplo: casa amarela, o número de palavras é 2. 

frase = str(input()).split()
lista_frase = list(frase)

print(len(lista_frase))