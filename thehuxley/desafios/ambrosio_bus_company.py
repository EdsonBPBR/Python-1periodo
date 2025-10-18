# Os ônibus possuem 44 lugares numerados de 1 a 44.
# registro de passageiros, com os valores dos campos número da passagem, data, de, para, horário, poltrona, idade e nome do passageiro,
# Ao final imprima o nome de todos os passageiros que estiverem acima da média das idades e que estiverem sentados nas poltronas pares.
registros = []
somatorio_idades = 0
c = 0
while c < 44:
    c += 1
    n_passagem = int(input())
    if n_passagem == -1:
        break
    
    data = str(input())
    de = str(input())
    para = str(input())
    horario = str(input())
    poltrona = int(input())
    idade = int(input())
    nome = str(input())
    
    registros.append((idade, poltrona, nome))
    somatorio_idades += idade

media_idades = somatorio_idades / len(registros)

c = 0
for posicao in range(len(registros)):
    if registros[posicao][0] > media_idades and registros[posicao][1] % 2 == 0:
        print(registros[posicao][2])
        c += 1

if c == 0:
    print('SEM RESPOSTA')