registro = []
while True:
    try:
        entrada = str(input()).strip().split()
        opcao = entrada[0].upper()
        
        if opcao == 'INSERIR':
            nome = entrada[1]
            valor = float(entrada[2])
            quant = int(entrada[3])
            registro.append({
                'nome': nome, 
                'valor': valor,
                'quantidade': quant,
                })
            
        elif opcao == 'CONSULTAR':
            somatorio = 0
            for dado in registro:
                somatorio += dado['valor'] * dado['quantidade']
            print(f'Atualmente a lista esta em R${somatorio:.1f}\n')
        
        elif opcao == 'REMOVERGRUPO':
            valor = float(entrada[1])
            # eu fiquei em dúvida se é necessário checar o produto, mas creio que a questão não solicita
            freq = []
            for chave, dado in enumerate(registro):
                if dado['valor'] > valor:
                    freq.append(dado)
                
            for dado in freq:
                registro.remove(dado)
                
        elif opcao == 'REMOVER':
            nome = str(entrada[1])
            quant = int(entrada[2])
            # eu fiquei em dúvida se é necessário checar o produto também, pois a questão não especificou para esse caso
            for chave, dado in enumerate(registro):
                if dado['nome'] == nome:
                    item = chave
            registro[item]['quantidade'] = registro[item]['quantidade'] - quant
            
        elif opcao == 'PROCURAR':
            nome = str(entrada[1])
            cadastrado = False
            for chave, dado in enumerate(registro):
                if dado['nome'] == nome:
                    item = chave
                    cadastrado = True
                    
            if cadastrado:
                print(f"{registro[item]['nome']}")
                print(f"- {registro[item]['valor']}")
                print(f"- {registro[item]['quantidade']}\n")
            else:
                print(f'{nome} nao foi encontrado.\n')
    except:
        break