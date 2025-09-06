# Faça um programa para ler os coeficiente A, B e C de uma equação do segundo grau na forma Ax² + Bx + C e calcular as suas raízes, levando em consideração a existência de raízes reais (∆ > 0, a equação possui duas raízes reais e distintas; ∆ = 0, a equação possui raízes reais iguais; ∆ < 0, a equação não possui raízes reais). Se ∆ < 0, deve ser informado ao usuário que a função não tem raízes reais.

print('Digite o coeficiente A:')
a = float(input())

print('Digite o coeficiente B:')
b = float(input())

print('Digite o coeficiente C:')
c = float(input())

delta = (b ** 2) - 4 * a * c

if delta < 0:
    print('A funcao nao tem raizes reais')
else:
    raiz_delta = delta ** 0.5

    x1 = (-b + raiz_delta) / (2 * a)
    x2 = (-b - raiz_delta) / (2 * a)

    print(f'Primeira raiz: {x1:.6f}')
    print(f'Segunda raiz: {x2:.6f}')
