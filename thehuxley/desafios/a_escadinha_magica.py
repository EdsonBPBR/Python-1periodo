# Zelda e seus amigos tiveram uma brilhante ideia durante as aulas da monitoria da cadeira de introdução a programação: que tal fazer um programa que, dado um número n (1 <= n <= 40) printa na tela os numeros de 1 até o número da iteração atual, sendo que serão feitas n iterações, como demonstrado no exemplo a seguir:

n = int(input())

for a in range(1, n+1):
    for b in range(1, a+1):
        if b == a:  
            print(b, end="")
        else:
            print(b, end=" ")
    print() 