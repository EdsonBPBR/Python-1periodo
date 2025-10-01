# Faça um programa que leia 3 números inteiros e imprima o valor intermediário (entre o menor e o maior número). Suponha que os números são diferentes.
lista = []

n1 = int(input())
n2 = int(input())
n3 = int(input())

lista.append(n1)
lista.append(n2)
lista.append(n3)

lista.remove(max(lista))
lista.remove(min(lista))

print(lista[0])