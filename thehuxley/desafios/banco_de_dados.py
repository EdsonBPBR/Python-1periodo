# O dono da empresa é muito amigo seu, e sabe que você é um ótimo programador, logo, te chamou para implementar esse banco de dados.
# As informações dos usuários que você deve guardar são:
# Idade.
# Nome.
# Sexo.
# Estado civil.
# Quantidade de amigos.
# Quantidade de fotos.

if __name__ == '__main__':
    n = int(input())
    registro = []

    for _ in range(n):
        idade = int(input())
        nome = str(input())
        sexo = str(input()) # M ou F
        estado_civil = str(input()) # S, C, N, D
        quant_amigos = int(input())
        quant_fotos = int(input())

        tupla = []
        tupla.append(idade)
        tupla.append(nome)
        tupla.append(sexo)
        tupla.append(estado_civil)
        tupla.append(quant_amigos)
        tupla.append(quant_fotos)

        registro.append(tupla)

    for linha in range(len(registro)):
        print(f'Idade: {registro[linha][0]}')
        print(f'Nome: {registro[linha][1]}')
        print(f'Sexo: {registro[linha][2]}')
        print(f'Estado Civil: {registro[linha][3]}')
        print(f'Numero de amigos: {registro[linha][4]}')
        print(f'Numero de fotos: {registro[linha][5]}')
        print()