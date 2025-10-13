# Joãozinho está criando uma lista de contatos e precisa de sua ajuda. Ele precisa que para cada contato você crie uma estrutura com os seguintes itens:
#     Nome e sobrenome;
#     Número no formato (00)01234-5678;
#     Código informando a relação que João tem com a pessoa, sendo: 
#         1 para família;  #         2 para faculdade;  #         3 para amigo;

n = int(input())
registro = {}

for i in range(n):
    nome_completo = str(input()).split()
    numero = str(input())
    cod = int(input())
    primeiro_nome = nome_completo[0]
    segundo_nome = nome_completo[1]
    
    registro[segundo_nome] = (primeiro_nome, cod, numero) # testa se o segundo nome for igual? Pois estou usando como PK o segundo nome
  
while True:
    nome = str(input())
    if nome == '#':
        break
    
    n_pesquisa = 0 # n_pesquisa também é suspeito
    for chave, linha in registro.items():
        if linha[1] == 1: # sistema de decisão ao invés de imprimir salvar logo na estrutura de dados? 
            vinculo = 'Familia'
        elif linha[1] == 2:
            vinculo = 'Faculdade'
        elif linha[1] == 3:
            vinculo = 'Amigo'
        else:
            vinculo = 'Invalido'
        
        if linha[0] == nome:
            print(f'Nome: {linha[0]} {chave}')
            print(f'Numero: {linha[2]}')
            print(f'Vinculo: {vinculo}')
            print()
            
            n_pesquisa += 1

    if n_pesquisa == 0:
        print(f'{nome} nao foi cadastrado')
