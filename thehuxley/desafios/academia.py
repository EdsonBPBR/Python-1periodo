
#problema ainda não resolvido
clientes = 0

while clientes <= 100:
    nome = str(input()) #máximo de 50 caracteres
     #limite de 100 clientes

    if nome == 'SAIR':
        break
    else:
        senha = int(input())
        situacao = str(input()) #P: pago, F: devendo
    
    print(f'Nome: {nome}, Senha: {senha}, Situação: {situacao}')
    clientes += 1
    