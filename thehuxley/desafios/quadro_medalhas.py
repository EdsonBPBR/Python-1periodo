# # Lembre-se de que o número de medalhas de ouro é mais importante que o de prata e este que o de bronze
# empate, compara-se o número de medalhas de prata. Caso ainda assim haja empate, o número das de bronze será considerado.
registro = []

while True:
    entrada = str(input()).split(',')
    if entrada[0] == '*':
        break
    
    pais = entrada[0]
    medalha = entrada[1]

    cadastrado = False
    for chave, dado in enumerate(registro):
        if dado['pais'] == pais:
            cadastrado = True
            item = chave

    if cadastrado: # para o país já cadastrado, só incrementar a medalha
        registro[item]['medalhas'].append(medalha)
        
    else: # senão, se o pais não estiver cadastrado, cadastrar o país e incrementar a primeira medalha
        registro.append({
            'pais': pais,
            'medalhas': [medalha]
        })
        
# montagem do placar e resultados
resultado = []
for dado in registro:
    somatorio = 0
    ouro = 0
    prata = 0
    bronze = 0
    for medalha in dado['medalhas']:
        if medalha == 'ouro':
            ouro += 1
        elif medalha == 'prata':
            prata += 1
        elif medalha == 'bronze':
            bronze += 1
    resultado.append([ouro, prata, bronze, dado['pais']])
    
resultado.sort(reverse=True)

for i in range(len(resultado)):
    print(f'{i+1}){resultado[i][3]} ouro:{resultado[i][0]} prata:{resultado[i][1]} bronze:{resultado[i][2]}')