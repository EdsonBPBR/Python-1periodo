valor = float(input())

notas_cem = valor // 100
resto_cem = valor % 100

notas_cinquenta = resto_cem // 50
resto_cinquenta = resto_cem % 50

notas_vinte = resto_cinquenta // 20
resto_vinte = resto_cinquenta % 20

notas_dez = resto_vinte // 10
resto_dez = resto_vinte % 10

notas_cinco = resto_dez // 5
resto_cinco = resto_dez % 5

notas_dois = resto_cinco // 2
resto_dois = resto_cinco % 2

moedas_um = resto_dois // 1
resto_moedas_um = resto_dois % 1

moedas_cinquenta = resto_moedas_um // 0.5
resto_moedas_cinquenta = resto_moedas_um % 0.5

moedas_vintecinco = resto_moedas_cinquenta // 0.25
resto_moedas_vintecinco = resto_moedas_cinquenta % 0.25

moedas_dez = resto_moedas_vintecinco // 0.10
resto_moedas_dez = resto_moedas_vintecinco % 0.10

moedas_centavos = resto_moedas_dez // 0.05
resto_moedas_centavos =  resto_moedas_dez % 0.05

moedas_centavos2 = resto_moedas_dez // 0.01

print('NOTAS:')
print(f'{int(notas_cem)} nota(s) de R$ 100.00')
print(f'{int(notas_cinquenta)} nota(s) de R$ 50.00')
print(f'{int(notas_vinte)} nota(s) de R$ 20.00')
print(f'{int(notas_dez)} nota(s) de R$ 10.00')
print(f'{int(notas_cinco)} nota(s) de R$ 5.00')
print(f'{int(notas_dois)} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{int(moedas_um)} moeda(s) de R$ 1.00')
print(f'{int(moedas_cinquenta)} moeda(s) de R$ 0.50')
print(f'{int(moedas_vintecinco)} moeda(s) de R$ 0.25')
print(f'{int(moedas_dez)} moeda(s) de R$ 0.10')
print(f'{int(moedas_centavos)} moeda(s) de R$ 0.05')
print(f'{int(moedas_centavos2)} moeda(s) de R$ 0.01')