dia = int(input('Dia: '))

if not(dia>= 1 and dia <=31):
    print('Dia inexistente')
else:
    mes = int(input('Mês: '))
    if not(mes>= 1 and mes<= 12):
        print('Mês inexistente') 
    else:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8  or mes == 10 or mes == 12:
            if dia > 31:
                print('Esse dia não existe nesse mês')
            else:
                ano = int(input('Ano: '))
                if not(ano >= 1900 and ano  <= 2020):
                    print('Ano inexistente')
                else:
                    print('Data Validada')
            
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia > 30:
                print('Esse dia não existe nesse mês')
            else:
                ano = int(input('Ano: '))
                if not(ano >= 1900 and ano <= 2020):
                    print('Ano inexistente')
                else:
                    print('Data Validada')

        elif mes == 2:
            if dia > 29:
                print('Esse dia não existe nesse mês')
            else:
                ano = int(input('Ano: '))
                if not(ano >= 1900 and ano <= 2020):
                    print('Ano inexistente')
                else:
                    if ((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0) and (dia >= 1 and dia <= 29):
                        print('Data Validada')
                    else:
                        print('Esse ano não é bissexto')

        else:
            print('Mês inexistente')