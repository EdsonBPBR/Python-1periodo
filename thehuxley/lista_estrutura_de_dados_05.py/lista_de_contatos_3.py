def cadastraContato(nome, celular, cod):
    relacao = {1: 'Familia', 2: 'Faculdade', 3: 'Amigo'}
    registros.append((nome, celular, relacao[cod]))    

def exibirSaida(registros):
    print(f'Nome: {registros[i][0]}')
    print(f'Numero: {registros[i][1]}')
    print(f'Vinculo: {registros[i][2]}\n')
            
if __name__ == '__main__':
    registros = []
    
    n = int(input())
    for i in range(n):
        nome = str(input()).strip()
        celular = str(input())
        cod = int(input())
        cadastraContato(nome, celular, cod)
        
    while True:
        nome = str(input()).strip()
        if nome == '#':
            break
        
        freq = 0
        for i in range(len(registros)):
            if nome in registros[i][0]:
                exibirSaida(registros)
                freq += 1
                
        if freq == 0:
            print(f'{nome} nao foi cadastrado\n')