# Lissandra comprou vários quadros novos para seu apartamento e agora precisa de pregos para pendurá-los. Pesquisando, ela descobriu que uma caixa com 12 pregos custa R$ 7,89.
# Escreva um programa que receba a quantidade de pregos necessários para cada quadro, até que seja informada uma quantidade ímpar, e exiba o valor total que será gasto e a quantidade de pregos que vão sobrar.

quant_total_pregos = 0

while True:
    pregos = int(input())
    
    if pregos % 2 != 0:
        break
    quant_total_pregos += pregos

if quant_total_pregos >= 12:
    n_caixas = quant_total_pregos // 12  
     
    if quant_total_pregos % 12 != 0:    
        n_caixas += 1
        
    resto = (12 * n_caixas) - quant_total_pregos
    preco_final = n_caixas * 7.89
    
    print(f'{preco_final:.2f}')
    print(resto)
else:
    resto = 12 - quant_total_pregos
    preco_final = 1 * 7.89
    
    print(f'{preco_final:.2f}')
    print(resto)
