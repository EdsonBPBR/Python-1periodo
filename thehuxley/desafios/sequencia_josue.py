entrada = str(input()).split()

vogais = 'AEIOU'
consoantes = 'BCDFGHJKLMNPQRSTVWXYZ'

for index in range(len(entrada)):
    print(entrada[index] in vogais)
    