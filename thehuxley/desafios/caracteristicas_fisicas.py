def contador(registros):
    freq = 0
    for registro in registros:
        if (registro[0] >= 18 and registro[0] <= 35) and (registro[1] == 'f') and (registro[2] == 'l') and (registro[3] == 'v'):
            freq += 1
    return freq

def main():
    registros = []
    total = 0
    while True:
        try:
            idade = int(input())     
            if idade == -1:
                break
            dados = str(input()).split()
            registros.append((idade, dados[0], dados[1], dados[2]))
            total += 1
        except ValueError:
            print('Entrada Inválida!')

    print(f'Mais velho: {max(registros)[0]}')
    print(f'Mulheres com olhos verdes, loiras com 18 a 35 anos: {(100*contador(registros))/total:.2f}%')
    
if __name__ == '__main__':
    main()