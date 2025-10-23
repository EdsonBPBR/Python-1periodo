registro = []
while True:
    opc = int(input())
    
    if opc == 0:
        break
    
    elif opc == 1:
        nome = str(input()).strip()
        salario = float(input())
        registro.append({'nome': nome, 'salario': salario}) # eu poderia inserir uma lista alinhas, tentarei inicialmente o dict entro da lista
        
    elif opc == 2:
        for i in range(len(registro)):
            print(f"{i+1}. {registro[i]['nome']}")
            print(f"{registro[i]['salario']:.2f}") # se ligar aqui vum, é necessário printar espaços em branco 
        print()
        
    elif opc == 3:
        nome = str(input()).strip() # seria foda se fosse o strip de estivesse atrapalhando
        cadastrado = False
        
        for i, valores in enumerate(registro):
            if valores['nome'] == nome:
                cadastrado = True
                posicao = i
        
        if not(cadastrado):
            print('Funcionario nao encontrado.')
        else:
            registro.pop(posicao)
        
    elif opc == 4:
        nome = str(input()).strip() # fiquei em dúvida, após o nome já vem a variável do novo salário ou só dps de verificar que o registro realmente existe? 
        cadastrado = False
        
        for i, valores in enumerate(registro):
            if valores['nome'] == nome:
                cadastrado = True
                posicao = i
                
        if not(cadastrado):
            print('Funcionario nao encontrado.')
        else:
            registro[posicao]['salario'] = float(input())
            
    else:
        print('Opcao invalida')

