def cadastrar_palavras(n, registros):
    for _ in range(n):
        entrada = str(input()).split(' => ')
        registros[entrada[0]] = entrada[1]

def tradutor(registros):
    while True:
        frase = str(input()).strip().split()
        if frase[0] == '*':
            break
        
        for posicao, palavra in enumerate(frase):
            if posicao + 1 == len(frase):
                print(registros[palavra] + '\n', end='')
            else:
                print(registros[palavra], end=' ')
                
def main():
    registros = {}
    try:
        n = int(input())
        cadastrar_palavras(n, registros)
        tradutor(registros)
    except ValueError:
        print('Dado de entrada inválido')
    except Exception as erro:
        print(f'Erro: {erro}')
    
if __name__ == '__main__':
    main()