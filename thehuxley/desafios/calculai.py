for _ in range(5):
    caracteres_senha = []
    dados = {
        1: '', # nome
        2: '', # data
        3: '' # cidade
    }

    dados_saida = {
        1: '', # nome,
        2: '', # data,
        3: ''
    }
    continuar = True
    
    for i in dados.keys():
        entrada = str(input()).strip()
        if entrada == 'SAIR':
            continuar = False
            break
        
        dados_saida[i] = entrada
        for k in entrada.split():
            if '/' in k:
                p = ''
                for c in k.split('/'):
                    p += f'{c}'
                    
                dados[i] += f'{p}'
            else:
                dados[i] += f'{k}'
                
    if continuar:
        idade = int(input())
        c = 0
        
        for k in range(5):
            for i in dados.keys():
                caracteres_senha.append(dados[i][c]) 
            c += 1
        caracteres_senha.pop(-1)
        caracteres_senha.pop(-1)

        senha = ''
        for caractere in caracteres_senha:
            senha += f'{caractere}'
        senha += f'{idade}'

    
        print(f'Nome: {dados_saida[1]}')
        print(f'Data de Nascimento: {dados_saida[2]}')
        print(f'Cidade Natal: {dados_saida[3]}')
        print(f'Idade: {idade} anos')
        print(f'Senha: {senha}')
    else:
        break