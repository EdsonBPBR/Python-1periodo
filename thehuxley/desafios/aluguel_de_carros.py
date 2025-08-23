# A locadora de carros SAI DA FRENTE está fazendo uma promoção e está alugando carros no período junino por R$ 30,00 a diária. Além disso, a locadora cobra R$ 0,01 por quilômetro rodado. Como é período de São João, a locadora quer fidelizar os clientes e está dando 10% de desconto no valor total do aluguel de qualquer carro.

print('Digite a quantidade de dias de locacao:')
dias = int(input())

print('Digite a quantidade de km rodados:')
km = int(input())

valor_total = (dias * 30) + (km * 0.01)
valor_promocional = 0.9 * valor_total

print(f'Valor a pagar pelo aluguel: R$ {valor_promocional:.6f}')