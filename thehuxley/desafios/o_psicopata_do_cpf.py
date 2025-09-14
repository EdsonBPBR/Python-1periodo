# Exemplo: liz 12345678911 ➔ l desloca 1 posição, i desloca 2 posições e z desloca 3 posições  ➔ senha: mkc11
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

def gerarSenha(primeiro_nome, cpf):
    c = 0
    senha = ''
    
    while c < len(primeiro_nome):
        posicao_inicial = alfabeto.index(primeiro_nome[c])
        k = int(cpf[c])
        senha += f'{alfabeto[(posicao_inicial+k) % 26]}'
        
        c += 1

    senha += f'{cpf[9]}{cpf[10]}'
    return senha

if __name__ == '__main__':
    n_cadastro = int(input())
    registros = []

    for _ in range(n_cadastro):
        dados = str(input()).split()
        primeiro_nome = str(dados[0])
        cpf = str(dados[1])

        senha = gerarSenha(primeiro_nome, cpf)
        
        linha_registro = f'{primeiro_nome} {senha}' # inserir em outra lista para poder ordenar pelo primeiro nome
        registros.append(linha_registro)

    registros.sort()
    # remover os registros da lista:
    for elementos in registros:
        print(elementos)