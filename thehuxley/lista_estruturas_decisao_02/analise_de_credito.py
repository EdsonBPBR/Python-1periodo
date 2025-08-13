# Escreva um programa que determine qual é o valor mensal da parcela do empréstimo que um banco pode autorizar. Para isso, o programa precisa do valor do salário e de quanto a renda mensal já está comprometida com outros empréstimos. Considere que o limite de comprometimento do salário é de 30%. O programa deve calcular e mostrar na tela qual o limite disponível da parcela mensal do novo empréstimo.  Fique atento porque a renda mensal comprometida já pode exceder os 30% e neste caso o limite disponível da parcela mensal será zero. 


salario = float(input('Informe seu salário: '))
comprometido = float(input('Informe o comprometimento: '))

# print(salario * 0.3)
limite_max = salario * 0.3

if limite_max  > comprometido:
    print(f'{(limite_max  - comprometido):.2f}')
else:
    print('0.00')