# A locadora de carros SAI DA FRENTE está fazendo uma promoção e está alugando carros no período junino por R$ 30,00 a diária. Além disso, a locadora cobra R$ 0,01 por quilômetro rodado. Como é período de São João, a locadora quer fidelizar os clientes e está dando 10% de desconto no valor total do aluguel de qualquer carro.

dias = int(input("Quantidade de Dias Alugados: "))
distancia = int(input("Quilometros rodados (KM): "))

# 0,01 x distancia + 30 x dias
valor_total = 0.01* distancia + 30 * dias
print(f'{valor_total * 0.9:.2f}')