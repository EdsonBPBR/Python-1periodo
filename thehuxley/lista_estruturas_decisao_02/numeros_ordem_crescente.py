#Faça um programa que leia 3 números inteiros e os imprima em ordem crescente.

# from random import randint

# n1 = randint(1, 5)
# n2 = randint(1, 5)
# n3 = randint(1, 5)

# print(n1, n2, n3)

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        print(n3)
        print(n2)
        print(n1)
    else:
        print(n2)
        print(n3)
        print(n1)

elif n2 >= n1 and n2 >= n3:
    if n1 >= n3:
        print(n3)
        print(n1)
        print(n2)
    else:
        print(n1)
        print(n3)
        print(n2)

else:
    if n1 >= n2:
        print(n2)
        print(n1)
        print(n3)
    else:
        print(n1)
        print(n2)
        print(n3)