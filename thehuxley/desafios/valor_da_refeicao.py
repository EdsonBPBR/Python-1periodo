# O restaurante a quilo ComaBem cobra R$ 20,00 por cada quilo de refeição. Escreva um programa que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. Assuma que a balança já desconte o peso do prato.

peso = float(input())
print(f'O valor do prato será: R$ {(peso*20):.2f}')