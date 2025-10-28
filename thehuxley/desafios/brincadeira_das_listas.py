lista_original = []
lista_inversa = []
lista_par_imp = []

entrada = input().split()
for caracteres in entrada:
    lista_original.append(int(caracteres))

lista_inversa = lista_original[::-1]

pares = []
impares = []

for i in range(len(lista_original)):
    if i % 2 == 0:  
        pares.append(lista_original[i])  
    else:  
        impares.append(lista_original[i])  

lista_par_imp = pares + impares  

soma = []
for i in range(len(lista_original)):
    somatorio = lista_inversa[i] + lista_par_imp[i]
    soma.append(somatorio)
    
print('Invert:', ' '.join(map(str, lista_inversa)))
print('ParImp:', ' '.join(map(str, lista_par_imp)))
print('Soma:', ' '.join(map(str, soma)))