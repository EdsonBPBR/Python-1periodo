# #Utilizando SOMENTE laço de repetição
# mes = int(input('Informe o número do mês (1-12): '))
# ano = int(input('Informe o ano: '))

# if mes == 1:
#     print('Janeiro - 31 dias')
# elif mes == 2:
#     if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:    
#         print('Fevereiro - 29 dias')
#     else:
#         print('Fevereiro - 28 dias')
# elif mes == 3:
#     print('Março - 31 dias')
# elif mes == 4:
#     print('Abril - 30 dias')
# elif mes == 5:
#     print('Maio - 31 dias')
# elif mes == 6:
#     print('Junho - 30 dias')
# elif mes == 7:
#     print('Julho - 31 dias')
# elif mes == 8:
#     print('Agosto - 31 dias')
# elif mes == 9:
#     print('Setembro - 30 dias')
# elif mes == 10:
#     print('Outubro - 31 dias')
# elif mes == 11:
#     print('Novembro - 30 dias')
# elif mes == 12:
#     print('Dezembro - 31 dias')
# else:
#     print('Não Corresponde a Nenhum Mês')

#Utilizando listas e dicionário:
meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
dias_meses = {
    'Janeiro':31,
    'Fevereiro':28, #considerando, inicialmente, ano "normal"
    'Março':31,
    'Abril':30,
    'Maio':31,
    'Junho':30,
    'Julho':31,
    'Agosto':31,
    'Setembro':30,
    'Outubro':31,
    'Novembro':30,
    'Dezembro': 31
}

mes_2 = int(input('Informe o mês (1-7): '))
ano = int(input('Informe o ano: '))

#bissexto:
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    dias_meses['Fevereiro'] = 29
else:
    pass

if 1<=mes_2<=12:
    print(f'{meses[mes_2-1]} - {dias_meses[meses[mes_2-1]]} dias')
else:
    print('Não Corresponde a Nenhum Mês')
