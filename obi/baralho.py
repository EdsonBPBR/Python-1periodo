# 52 cartas
# 4 naipes (Copas, Espadas, Ouros e Paus),
# treze cartas em cada naipe (Ás, 2, 3, 4, 5, 6, 7, 8, 9, 10, Valete 11, Dama 12 e Rei 13 ).
# Cada carta é descrita usando três caracteres, no formato ddN onde dd são dois dígitos decimais (de 01, representando a carta Ás, a 13, representanto a carta Rei) e N é um caractere entre C, E, U e P, representando respectivamente os naipes Copas, Espadas, Ouros e Paus).  
entrada = str(input()).strip()
k = 0
c = 3
cartas = []

copas = 0
espadas = 0
ouros = 0
paus = 0
repetidos = []

for _ in range(len(entrada)//3):
    l = (entrada[k:c])
    k = c
    c += 3
    # print(l)
    if l in cartas:
        repetidos.append(l[2]) # eu ainda não sei como tratar o caso de erro, como eu irei fazer isso?
    else:
        cartas.append(l)

for i in range(len(cartas)):
    if (cartas[i][2]) == 'C':
        copas += 1
    
    if (cartas[i][2]) == 'E':
        espadas += 1
    
    if (cartas[i][2]) == 'U':
        ouros += 1
        
    if (cartas[i][2]) == 'P':
        paus += 1

if not('C' in repetidos):
    print(13-copas)
else:
    print('erro')

if not('E' in repetidos):
    print(13-espadas)
else:
    print('erro')

if not('U' in repetidos):
    print(13-ouros)
else:
    print('erro')

if not('P' in repetidos):
    print(13-paus)
else:
    print('erro')