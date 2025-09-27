# Escreva um programa em C que leia o valor do mês e imprima o total de dias deste mês.

if __name__ == '__main__':
    mes = int(input())

    if mes >= 1 and mes <= 12:
        if mes == 1:
            dias = 31
        elif mes == 2:
            dias = 28
        elif mes == 3:
            dias = 31
        elif mes == 4:
            dias = 30
        elif mes == 5:
            dias = 31
        elif mes ==6:
            dias = 30
        elif mes == 7:
            dias = 31
        elif mes == 8:
            dias = 31
        elif mes == 9:
            dias = 30
        elif mes == 10:
            dias = 31
        elif mes ==11:
            dias = 30
        else:
            dias = 31
            
        print(f'Numero de dias do mes {mes}  : {dias} dias')
    else:
        print('Voce entrou com um mes invalido !')