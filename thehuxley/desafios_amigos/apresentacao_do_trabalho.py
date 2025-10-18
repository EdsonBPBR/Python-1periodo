entrada_dados = str(input()).split()
print(entrada_dados)

ig = int(entrada_dados[0])
ia = int(entrada_dados[1])
encap = int(entrada_dados[2])
ident = int(entrada_dados[3])
structs = int(entrada_dados[4])

if (ig or ia) and (encap) and (ident) and (structs):
    print('AVALIADO')
else:
    print(0)