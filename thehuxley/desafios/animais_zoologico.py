n_macacos = 0
somatorio_peso_tigres = 0
n_tigres = 0
quant_cobras_venez = 0

while True:
    nome = str(input())

    if nome.upper() == 'MACACO':
        n_macacos += 1

    peso = float(input())

    if nome.upper() == 'TIGRE':
        somatorio_peso_tigres += peso
        n_tigres += 1

    pais = str(input())

    if nome.upper() == 'COBRA' and pais.upper() == 'VENEZUELA':
        quant_cobras_venez += 1

    status = str(input())
    if status.upper() == 'CONTINUAR':
        continue
    else:
        if status.upper() == 'PARAR':
            break

print(n_macacos)

if n_tigres > 0:
    print(f"{(somatorio_peso_tigres/n_tigres):.2f}")
else:
    print(0.00)

print(quant_cobras_venez)