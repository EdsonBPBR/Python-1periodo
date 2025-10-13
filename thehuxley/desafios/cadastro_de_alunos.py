registros = {}
while True:
    opc = int(input())
    
    if opc == 0:
        break
    
    elif opc == 1:
        nome = str(input())
        salario = float(input())
        registros[nome] = [salario] 

    elif opc == 2:
        funcionarios = list(registros.keys())
        for i in range(len(funcionarios)):
            print(f'{i+1}. {funcionarios[i]}')
                   
            if i == len(funcionarios)-1:
                print(f'{registros[funcionarios[i]][0]:.2f}\n')
            else:
                print(f'{registros[funcionarios[i]][0]:.2f}')
                
    elif opc == 3:
        nome = str(input())
        
        if nome in registros:
            registros.pop(nome)
        else:
            print('Funcionario nao encontrado.')
    
    elif opc == 4:
        nome = str(input())
        
        if nome in registros:
            novo_salario = float(input())
            registros[nome][0] = novo_salario
        else:
            print('Funcionario nao encontrado.')

    else:
        print('Opcao invalida')