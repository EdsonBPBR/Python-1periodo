# A Locadora de Veículos Eudora lançou uma grande promoção esse mês: pagando apenas R$ 90 por diária, o cliente pode alugar um carro de passeio. Para cada diária, o cliente recebe uma cota de quilometragem de 100 Km. Cada quilômetro a mais custará uma taxa extra de R$ 12.

# Escreva um programa que receba como entrada a quantidade de dias e a quilometragem total rodada por um cliente dessa locadora e exiba o valor total a ser pago com duas casas decimais.

dias = int(input('Dias: '))
km_total = int(input('Km: '))

if km_total > (dias * 100):
    taxa = (km_total - (dias * 100)) * 12
else:
    taxa = 0

valor_final = taxa + (dias * 90)
print(f'{valor_final:.2f}')