# Ele participou de uma reunião recente em que foi informado de que deveria entregar pelo menos 100 correspondências por dia para dar conta do grande fluxo de envios na época de Natal.
# Escreva um programa que receba como entrada a quantidade de correspondências entregues por ele em cada um dos sete dias da semana, e exiba em quantos dias ele cumpriu a meta, e a média de entregas diárias que ele fez no período.

k = 0
somatorio_semanal = 0
n_dias_metas = 0

while k < 7:
    n_encomendas_diarias = int(input())

    if n_encomendas_diarias >= 100:
        n_dias_metas += 1

    somatorio_semanal += n_encomendas_diarias
    k += 1

print(n_dias_metas)
print(somatorio_semanal//7)