# Neste problema deve-se ler o código de uma "peça 1", o número de "peças 1", o valor unitário de cada "peça 1", o código de uma "peça 2", o número de "peças 2", o valor unitário de cada "peça 2", calcular e mostrar o valor a ser pago.

cod_peca_1, n_peca_1, preco_peca_1 = map(float, input().split())
cod_peca_2, n_peca_2, preco_peca_2 = map(float, input().split())

total = (n_peca_1 * preco_peca_1) + (n_peca_2 * preco_peca_2)
print(f'VALOR A PAGAR: R$ {total:.2f}')