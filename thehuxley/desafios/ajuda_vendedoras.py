# Escreva um programa de ajuda para vendedores. A partir do valor do produto digitado pelo usuário, mostre:
# • o total a pagar com desconto de 10%
# • o valor de cada parcela, no parcelamento de 3× sem juros;
# • a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
# • a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)

valor = int(input())

a_vista = valor * 0.9
parcelamento = valor / 3
comissao_vendedor_a_vista = a_vista * 0.05
comissao_vendedor_a_prazo = valor * 0.05

print(f'A vista com desconto de 10%: {a_vista:.2f}')
print(f'Valor da parcela em 3x sem juros: {parcelamento:.2f}')
print(f'Comissao do vendedor a vista: {comissao_vendedor_a_vista:.2f}')
print(f'Comissao do vendedor a prazo: {comissao_vendedor_a_prazo:.2f}')