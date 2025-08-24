# (Mais velho e mais novo) Crie um programa em Python para ler e imprimir a idade
# de um grupo de 10 pessoas. Ao final, o programa deve informar a pessoa mais velha
# e a mais jovem

for u in range(3):
    idade = int(input('Informe sua idade: '))

    if u == 0:
        mais_velho = mais_novo = idade
    else:
        if idade >= mais_velho:
            mais_velho = idade
        else:
            mais_novo = idade

print(f'O mais velho tem {mais_velho} anos')
print(f'O mais novo tem {mais_novo} anos')