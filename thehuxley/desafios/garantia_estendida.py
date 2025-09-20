# A Favorita vende eletrodomésticos e eletroeletrônicos, e oferece a seus clientes a opção de comprar também a garantia estendida. Se quiserem apenas a garantia simples, os clientes não pagam nada a mais, apenas o valor do produto. Caso optem pela garantia estendida de um ano, deverão pagar uma taxa extra de 3% do valor do produto. Já a garantia estendida de dois anos custa 5% do valor do produto.

valor = float(input())
garantia = int(input())

if garantia == 1:
    valor_final = valor * 1.03

elif garantia == 2:
    valor_final = valor * 1.05

else:
    valor_final = valor

print(f'{valor_final:.2f}')