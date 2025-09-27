# Vinicius é um ótimo programador, mas é meio doido também. Certo dia ele foi desafiado por seu amigo a escrever um programa que gerasse um triangulo, como o abaixo, dado uma letra do alfabeto que representa até onde ele deve ir.

letra = str(input())
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

sla = int(alfabeto.index(f'{letra.upper()}'))
print(sla)

for a in range(sla+1):
    print(alfabeto[a], end='')

print()