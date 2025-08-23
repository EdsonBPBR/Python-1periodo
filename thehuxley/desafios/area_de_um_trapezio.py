# Faça um programa que calcule e mostre a área de um trapézio. Sabendo-se que:

basemaior = int(input())
basemenor = int(input())
altura = int(input())

area = ((basemaior + basemenor) * altura)/2
print(f'{area:.1f}')