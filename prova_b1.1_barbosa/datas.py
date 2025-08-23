dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

match mes:
    case 1:
        nome_mes = 'Janeiro'
        mes_abreviado = 'Jan.'
    case 2:
        nome_mes = 'Fevereiro'
        mes_abreviado = 'Fev.'
    case 3:
        nome_mes = 'Março'
        mes_abreviado = 'Mar.'
    case 4:
        nome_mes = 'Abril'
        mes_abreviado = 'Abr.'
    case 5:
        nome_mes = 'Maio'
        mes_abreviado = 'Mai.'
    case 6:
        nome_mes = 'Junho'
        mes_abreviado = 'Jun.'
    case 7:
        nome_mes = 'Julho'
        mes_abreviado = 'Jul.'
    case 8:
        nome_mes = 'Agosto'
        mes_abreviado = 'Ago.'
    case 9:
        nome_mes = 'Setembro'
        mes_abreviado = 'Set.'
    case 10:
        nome_mes = 'Outubro'
        mes_abreviado = 'Out.'
    case 11:
        nome_mes = 'Novembro'
        mes_abreviado = 'Nov.'
    case 12:
        nome_mes = 'Dezembro'
        mes_abreviado = 'Dez.'

if dia > 10:
    dia = dia
else:
    dia = f'0{str(dia)}'

if mes > 10:
    mes = mes
else:
    mes = f'0{str(mes)}'

print(f'{dia}/{mes}/{ano%1000}')
print(f'{dia} de {nome_mes} de {ano}')
print(f'{dia}/{mes_abreviado}/{ano%1000}') 