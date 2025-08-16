dia = int(input('Dia: '))
mes = int(input('Mês [1-12]: '))
ano = int(input('Ano: '))

if not(ano >= 1900 and ano <= 2020):
    print('Ano inexistente')

elif not(mes >= 1 and mes <= 12):
    print('Mês inexistente')

elif not(dia >= 1 and dia <= 31):
    print('Dia inexistente')

else:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia <= 31:
            print('Data Validada')
        else:
            print('Esse dia não existe nesse mês')
        
    elif mes == 4 or mes == 6 or mes == 9 or mes == 1:
        if dia <= 30:
            print('Data Validada')
        else:
            print('Esse dia não existe nesse mês')
    
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            if dia <= 29:
                print('Data Validada')
            else:
                print('Esse dia não existe nesse mês')
        else:
            if dia <= 28:
                print('Data Validada')
            elif dia == 29:
                print('Esse ano não é bissexto')
            else:
                print('Esse dia não existe nesse mês') 

# # #começando pelo ano -> mes -> dia:
# if ano >= 1900 and ano <= 2020:
#     if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0: #condicional ano bissexto ou não
#         if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
#             if dia >= 1 and dia <= 31:
#                 print('Data Validada')
#             else:
#                 print('Dia inexistente') #atenção aqui,pois substituí por "Esse dia não existe nesse mês" 

#         elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
#             if dia == 31:
#                 print('Esse dia não existe nesse mês')
#             elif dia >= 1 and dia <= 30:
#                 print('Data Validada')
#             else:
#                 print('Dia inexistente')

#         elif mes == 2:
#             if dia >= 1 and dia <= 29:
#                 print('Data Validada')
#             else:
#                 print('Esse dia não existe nesse mês')  #atenção aqui, pois substituí por "Esse dia não existe nesse mês" 

#         else:
#             print('Mês inexistente')

#         #print(f'{ano} é bissexto')
#     else:
#         if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
#             if dia >= 1 and dia <= 31:
#                 print('Data Validada')
#             else:
#                 print('Dia inexistente') #atenção aqui,pois substituí por "Esse dia não existe nesse mês" 

#         elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
#             if dia == 31:
#                 print('Esse dia não existe nesse mês')
#             elif dia >= 1 and dia <= 30:
#                 print('Data Validada')
#             else:
#                 print('Dia inexistente')

#         elif mes == 2:
#             if dia >= 1 and dia <= 28:
#                 print('Data Validada')
#             elif dia == 29:
#                 print('Esse ano não é bissexto')
#             else:
#                 print('Esse dia não existe nesse mês')  #prestar atenção aqui
            
#         else:
#             print('Mês inexistente')

#         #print(f'{ano} NÃO é bissexto')
# else:
#     print('Ano inexistente')



