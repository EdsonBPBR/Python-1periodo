c = 0
registros = {}

while True:
    opc = int(input())
    
    if opc == 1:
        nome = str(input()).strip()
        salario = float(input())
        
        registros[c] = [nome, salario]
        c += 1
        
    elif opc == 2:
        for posicao in range(len(registros)):
            print(f'{posicao+1}. {registros[posicao][0]}')
            
            if len(registros)-1 == posicao:
                print(f'{registros[posicao][1]:.2f}\n')
            else:
                print(f'{registros[posicao][1]:.2f}')
        
    elif opc == 3:
        nome = str(input()).strip()
        
    elif opc == 4:
        nome = str(input()).strip()
        novo_salario = float(input())
        
        for posicao in range(len(registros)):
            if nome in registros[posicao]:
                print(registros[posicao])
        
    elif opc == 0:
        break
    
    else:
        print('Opcao invalida')