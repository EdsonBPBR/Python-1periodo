#nome completo, data, cidade, idade
#primeiraletranome, 
#primeiro numero data de aniversario
#primeria letra da cidade

# ate
 
#5 primeiras letras do nome, 
# dia e mes do aniversari
# 4 primeiras letras do nome da cidade
#terminar com idade

c = 0  # contador de funcionários

while c < 5:
    try:
        nome_completo = input().strip()
        if nome_completo == 'SAIR':
            break

        entrada_data = input().strip()
        entrada_lista_data = entrada_data.split('/')
        data = f'{entrada_lista_data[0]}{entrada_lista_data[1]}'
        cidade = input().strip()
        idade = int(input().strip())
        senha = ''

        lista_nome = list(nome_completo[:4])
        lista_data = list(data[:4])
        lista_cidade = list(cidade[:4])

        for i in range(4):
            senha += f'{lista_nome[i]}{lista_data[i]}{lista_cidade[i]}'

        senha += f'{nome_completo[4]}{idade}'

        print(f'Nome: {nome_completo}')
        print(f'Data de Nascimento: {entrada_data}')
        print(f'Cidade Natal: {cidade}')
        print(f'Idade: {idade} anos')
        print(f'Senha: {senha}\n')

        c += 1

    except EOFError:
        break
