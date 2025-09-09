# Eu sou fanático pela letra a. Para mim, é muito importante saber quantas vezes a letra a aparece em qualquer texto. Você pode me ajudar? Crie um programa que leia um texto qualquer e me diga quantas vezes a letra a aparece nele.

frase = str(input()).upper()
lista_frase = list(frase)
n_letras_a = 0

for k in lista_frase:
    if k == 'A':
        n_letras_a += 1
        
print(n_letras_a)