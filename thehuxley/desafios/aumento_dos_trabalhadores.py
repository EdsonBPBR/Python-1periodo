# Devido à proximidade com o Dia do Trabalho, uma empresa resolveu conceder aumentos salariais a seus funcionários. Aqueles com salário superior a R$ 500, terão aumento de 10%, enquanto os que ganham mais de R$ 300 terão aumento de 7%. Os demais funcionários terão aumento de apenas 5%. Escreva um programa que receba como entrada o salário atual de um funcionário, calcule e exiba o valor de seu novo salário já com o aumento concedido.

salario = float(input())

if salario > 300 and salario < 500:
    print(f'{(salario * 1.07):.2f}')

elif salario > 500:
    print(f'{(salario * 1.1):.2f}')

else:
    print(f'{(salario * 1.05):.2f}')