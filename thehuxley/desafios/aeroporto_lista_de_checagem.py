# você é um segurança com uma lista checagem, o seu trabalho é checar cada um do passageiros e ver se eles tem
#     RG;
#     Passagem
# Após isso você deve checar se as datas de nascimento no RG e na passagem são iguais, qual é o assento do passageiro e informa-lo qual é o seu assento
# se o passageiro não tiver um RG ele deve ser direcionado para a saída;
# se o passageiro não tiver uma passagem ele deve ser direcionado para a recepção do aeroporto;
# se a data de nascimento do RG e da Passagem não baterem você deve chamar a policia. 

quant = int(input())

c = 0
while c < quant:
    c += 1
    situacao_rg = str(input()).upper() 
    data_rg = str(input()) #dd/mm/aaaa
    situacao_passagem = str(input()).upper()
    data_passagem = str(input()).upper()
    cadeira = str(input()).upper()
    
    if situacao_rg == 'NAO POSSUI' or situacao_rg != 'RG':
        print('a saida e nessa direção')
    else:
        if situacao_passagem == 'NAO POSSUI' or situacao_passagem != 'PASSAGEM':
            print('a recepição e nessa direção')
        else:
            if data_rg != data_passagem:
                print('190')
            else:
                print(f'o seu assento e {cadeira} tenha um bom dia')

    