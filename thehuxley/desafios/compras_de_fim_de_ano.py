registros = {}
while True:
    entrada = str(input())
    if entrada[0] == '*':
        break
    nome = ''
    for caractere in entrada:
        if not(caractere in '1234567890'):
            nome += f'{caractere}'
        else:
            break
    registros[nome.strip()] = float(entrada.split()[-1])

while True:
    entrada = str(input()).split()

    if entrada[0] == 'total':
        total = 0
        for valores in registros.values():
            total += valores
        print(f'{total:.2f}')
        break
    
    elif entrada[0] == 'retire':
        nome = ''
        for posicao in range(1, len(entrada), 1):
            nome += f'{entrada[posicao]} '
        registros.pop(nome.strip())
    
    elif entrada[0] == 'quantidade':
        print(len(registros))