n = int(input())
registros = {}

def defineVinculo(cod):
    if cod == 1: 
        vinculo = 'Familia'
        return vinculo
    elif cod == 2:
        vinculo = 'Faculdade'
        return vinculo
    elif cod == 3:
        vinculo = 'Amigo'
        return vinculo
    else:
        vinculo = 'Invalido'
        return vinculo

# cadastro dos contatos
for i in range(n):
    nome_completo = str(input()).split()
    numero = str(input())
    cod = int(input())
    
    registros[i] = (nome_completo, numero, defineVinculo(cod))
    
# pesquisa e impressao dos contatos
while True:
    busca_nome = str(input()) # eu identifiquei um problema, quando é pressionado o enter ele mostra todos os registros cadastados
    if busca_nome == '#': 
        break
    
    freq = 0
    for i in range(len(registros)):
         
        if busca_nome in registros[i][0][0]: # só é possível realizar a busca pelo primeiro nome? Aqui se eu pesquisa usando o sobrenome aparece
            if len(registros[i][0]) > 1:
                print(f'Nome: {registros[i][0][0]} {registros[i][0][1]}')
            else:
                print(f'Nome: {registros[i][0][0]}')
            print(f'Numero: {registros[i][1]}')
            print(f'Vinculo: {registros[i][2]}')
            print()
            freq += 1
            
    if freq == 0:
        print(f'{busca_nome} nao foi cadastrado')