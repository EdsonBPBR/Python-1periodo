# (Somatorio) Crie um programa em Python para receber valores e informar o
# somat ́orio destes valores. Caso o valor 0 (zero) seja informado o programa deve
# finalizar sua execu ̧c ̃ao.

soma = 0
while True:
    n = float(input('Informe um número: '))

    if n == 0:
        break
    else:
        pass
    soma += n

print(f'O somatório dos valores informado é {soma}')