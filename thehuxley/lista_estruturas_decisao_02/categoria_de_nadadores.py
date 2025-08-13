# Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:

#     Infantil A: [5; 7]
#     Infantil B: [8; 10]
#     Juvenil A: [11;13]
#     Juvenil B: [14;17]
#     Adulto: [18;40]
#     Master: A partir de 41 e sem limite superior

# Caso a idade informada esteja fora dos limites, emita uma mensagem de erro: "Idade invalida."

idade = int(input("Informe sua idade: "))

if 5 <= idade <= 7:
    print('Infantil A')

elif 8 <= idade <= 10:
    print('Infantil B')

elif 11 <= idade <= 13:
    print('Juvenil A')

elif 14 <= idade <= 17:
    print('Juvenil B')

elif 18 <= idade <= 40:
    print('Adulto')

elif idade >= 41:
    print('Master')

else:
    print('Idade invalida.')