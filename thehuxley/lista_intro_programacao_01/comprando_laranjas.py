# 1 duzia, 12 laranjas por - 8,35
# se for maior que 12, 13 larajnas é necessário 2 duzias - 16,7

qnt_laranjas = int(input("Informe a Quantidade de Laranjas: "))
n_duzias = qnt_laranjas // 12 #nº de dúzias
resto = qnt_laranjas % 12 #resto 

# n_duzia x 8,35 + valor unitário x resto
#23: 1 dúzia = 8,25, resto 11: 11 x 0,7 (preco unitário)
calculo = (n_duzias * 8.35) + (resto * 8.35/12)
print(n_duzias)
print(f'{calculo:.2f}')