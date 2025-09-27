# Crie um programa que receba dois números inteiros, A e B (A<=B), e exiba os números inteiros no intervalo fechado [ A..B ] pulando de três em três.

A = int(input())
B = int(input())

for i in range(A, B+1, 3):
    print(i)