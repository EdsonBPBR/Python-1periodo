# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.
#células notas: 100, 50, 20, 10, 5, 2 e 1
valor = int(input("Informe o valor: "))

cem = valor // 100 #divisão inteira 
resto_cem = valor % 100 #resto da divisão 

cinquenta = resto_cem // 50
resto_cinquenta = resto_cem % 50

vinte = resto_cinquenta // 20
resto_vinte = resto_cinquenta % 20

dez = resto_vinte // 10
resto_dez = resto_vinte % 10

cinco = resto_dez // 5
resto_cinco = resto_dez % 5

dois = resto_cinco // 2
um = resto_cinco % 2

print(valor)
print(f'{cem} nota(s) de R$ 100,00')
print(f'{cinquenta} nota(s) de R$ 50,00')
print(f'{vinte} nota(s) de R$ 20,00')
print(f'{dez} nota(s) de R$ 10,00')
print(f'{cinco} nota(s) de R$ 5,00')
print(f'{dois} nota(s) de R$ 2,00')
print(f'{um} nota(s) de R$ 1,00')

# valor = int(input())

# cem = valor // 100
# resto_cem = valor % 100 

# cinquenta = resto_cem // 50
# resto_cinquenta = resto_cem % 50

# vinte = resto_cinquenta // 20
# resto_vinte = resto_cinquenta % 20

# dez = resto_vinte // 10
# resto_dez = resto_vinte % 10

# cinco = resto_dez // 5
# resto_cinco = resto_dez % 5

# dois = resto_cinco // 2
# um = resto_cinco % 2

# print(valor)
# print(f'{cem} nota(s) de R$ 100,00')
# print(f'{cinquenta} nota(s) de R$ 50,00')
# print(f'{vinte} nota(s) de R$ 20,00')
# print(f'{dez} nota(s) de R$ 10,00')
# print(f'{cinco} nota(s) de R$ 5,00')
# print(f'{dois} nota(s) de R$ 2,00')
# print(f'{um} nota(s) de R$ 1,00')
