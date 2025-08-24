# (Fibonnaci) Crie um programa em Python que retorne a sequencia de Fibonnaci at ́e
# um valor N fornecido pelo usu ́ario. A sequencia de Fibonnaci inicia com os valores 0
# e 1 e ent ̃ao o en ́esimo valor corresponde a soma dos dois valores anteriores (0 1 1 2
# 3 5 8 13 ...)

N = int(input('Comprimento da frequência: '))

termo_anterior = 1
for k in range(N):
    if k == 0:
        soma = k + termo_anterior
        print(k, end=' ')
    else:
        soma += termo_anterior
        print(termo_anterior, end=' ')

        termo_anterior = soma - termo_anterior
print()
    