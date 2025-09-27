# Genival é ascensorista da Prefeitura Municipal e todos os dias conduz os passageiros para cima e para baixo. O elevador que ele opera tem capacidade para no máximo 7 pessoas e no máximo 560 quilos.
# Escreva um programa que receba como entrada o peso de várias pessoas que estão entrando no elevador e exiba quantas poderão ser transportadas com segurança e o peso total carregado, respeitando os limites do elevador.

somatorio_peso = 0
n_pessoas = 0

while True:
    peso = int(input())

    if peso == 0:
        break

    if n_pessoas + 1 <= 7 and somatorio_peso + peso <= 560:
        n_pessoas += 1
        somatorio_peso += peso

    else:
        break

print(n_pessoas)
print(f'{somatorio_peso:.1f}')
