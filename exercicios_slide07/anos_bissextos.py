# Sabe-se que anos bissextos são os anos que possuem 366 dias no calendário, esse dia representa o acrescimo de 1 dia em Fevereiro, que deixa de ter 28 dias, e passa a ter 29.
# Para calcular os anos bissextos, utilizam-se estas regras:
# - A cada quatro anos, há um ano bissexto;
# - São bissextos todos os anos múltiplos de 400, exceto se for múltiplo de 100, mas não de 400, por exemplo: 1996, 2000, 2004, 2008, 2012, 2016, 2020;
# - Não são bissextos os anos múltiplos de 100.
# De acordo com o cálculo, os próximos anos bissextos divisíveis por 4 serão: 2024, 2028, 2032, 2036, 2040, 2048, 2052.


# ano = int(input())

# if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#     print(f'{ano} é bissexto')
# else:
#     print(f'{ano} NÃO é bissexto')

ano_inicial, ano_final = map(int, input().split())
n_anos_bissextos = 0

while ano_inicial < ano_final:
    if (ano_inicial % 4 == 0 and ano_inicial % 100 != 0) or (ano_inicial % 400 == 0):
        print(ano_inicial)
        n_anos_bissextos += 1
    
    ano_inicial += 1

if n_anos_bissextos == 0:
    print('-1')
else:
    pass