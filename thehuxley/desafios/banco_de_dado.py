def montaSaida(registros, posicoes):
    print(f'Idade: {registros[posicoes][0]}') 
    print(f'Nome: {registros[posicoes][1]}')
    print(f'Sexo: {registros[posicoes][2]}')
    print(f'Estado Civil: {registros[posicoes][3]}')
    print(f'Numero de amigos: {registros[posicoes][4]}')
    print(f'Numero de fotos: {registros[posicoes][5]}')
    print()
    
if __name__ == '__main__':
    print('Digite a quantidade de usuarios:')
    registros = []
    try:
        n = int(input())
        i = 0
        while i < n:
            i += 1    
            print(f'Digite os dados do usuario {i}:')
            
            idade = int(input())
            nome = str(input())
            sexo = str(input())
            estado_civil = str(input())
            n_amigos = int(input())
            n_fotos = int(input())
            registros.append((idade, nome, sexo, estado_civil, n_amigos, n_fotos))
    
    except ValueError:
        print('Dado de entrada inválido!')
        
    for posicoes in range(len(registros)):
        montaSaida(registros, posicoes)