#utilizando SOMENTE estrutura de decisão:

# try:
#     numero = int(input('Informe um número: '))
#     # N (1<=N<=12), utilizando estrutura de decisão:
#     if numero == 1:
#         print('Janeiro')

#     elif numero == 2:
#         print('Fevereiro')

#     elif numero == 3:
#         print('Março')

#     elif numero == 4:
#         print('Abril')

#     elif numero == 5:
#         print('Maio')

#     elif numero == 6:
#         print('Junho')

#     elif numero == 7:
#         print('Julho')

#     elif numero == 8:
#         print('Agosto')

#     elif numero == 9:
#         print('Setembro')

#     elif numero == 10:
#         print('Outubro')

#     elif numero == 11:
#         print('Novembro')

#     elif numero == 12:
#         print('Dezembro')

#     else:
#         print('Não Corresponde a Nenhum Mês')
        
# except ValueError as erro:
#     print(f'Valor de Entrada Inválido: {erro}')

#utilizando MATCH:
# mes = int(input('Informe um número do mês (1-12): '))
# match mes:
#     case 1:
#         print('Janeiro')
#     case 2:
#         print('Fevereiro')
#     case 3:
#         print('Março')
#     case _ :
#         print('E assim sucessivamente...')

#utilizando listas:
meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

try:
    numero = int(input('Informe um número: '))
    if 1<=numero<=12:
         print(meses[numero-1])
    else:
        print('Não Corresponde a Nenhum Mês')

except ValueError as erro:
    print(f'Entrada Inválida: {erro}')