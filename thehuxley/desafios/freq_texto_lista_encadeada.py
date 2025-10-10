# hoje esta quente, logo esta umido.
# j 1
# i 1
# h 1
# g 1
# e 5
# d 1
# a 2
# . 1
# , 1
#   5

elementos = {}

entrada_texto = str(input())
texto = list(entrada_texto)

for posicoes in range(len(texto)):
    if not(texto[posicoes] in elementos):
        elementos[texto[posicoes]] = texto.count(texto[posicoes])
        
# print(elementos)
list_chaves = list(elementos.keys())
list_chaves.sort(reverse=True)

for chaves in list_chaves:
    print(chaves, elementos[chaves])
    