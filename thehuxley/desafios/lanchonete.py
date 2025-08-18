# O cardápio de uma lanchonete é dado abaixo. Prepare um algoritmo que leia a quantidade de cada item da tabela respectivamente e calcule a conta final.

# Hambúrguer................. R$ 3,00 
# Cheeseburger .............. R$ 2,50 
# Fritas............................ R$ 2,50 
# Refrigerante ................. R$ 1,00 
# Milkshake..................... R$ 3,00

h = int(input())
c = int(input())
f = int(input())
r = int(input())
m = int(input())

total = (h * 3) + (c * 2.5) + (f * 2.5) + (r * 1) + (m * 3)
print(f'conta final: {total:.1f}')
