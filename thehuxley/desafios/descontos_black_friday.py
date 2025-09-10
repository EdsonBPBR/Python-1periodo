# Por isso, ele resolveu fazer uma pesquisa numa loja online. Ele anotou o preço de 5 produtos uma semana antes e no dia da promoção para ver se o desconto de 20% anunciado tinha sido realmente aplicado.

# Escreva um programa que receba como entrada os preços original e com desconto de cada produto, e exiba ao final quantos realmente tiveram abatimento de pelo menos 20%.

c = 0 
n_produtos_descontos = 0
while c < 5:
    preco_original = float(input())
    preco_promocional = float(input())
    
    if preco_promocional > (preco_original * 0.8):
        pass
    else:
        n_produtos_descontos += 1

    c += 1
print(n_produtos_descontos)