# Crie um problema em Linguagem C que preenche dois vetores com dez números inteiros. E seguida, seu programa deverá armazenar em um terceiro vetor a soma dos dois vetores lidos.

array_1 = str(input()).split()
array_2 = str(input()).split()
soma = []

for posicao in range(len(array_1)):
    e = int(array_1[posicao]) + int(array_2[posicao])
    soma.append(str(e))
    
print(' '.join(soma))