# (Aumento dos Trabalhadores) Devido `a proximidade com o Dia do Trabalho, uma
# empresa resolveu conceder aumentos salariais a seus funcion ́arios. Aqueles com
# sal ́ario superior a R$ 500, ter ̃ao aumento de 10%, enquanto os que ganham mais de
# R$ 300 ter ̃ao aumento de 7%. Os demais funcion ́arios ter ̃ao aumento de apenas
# 5%. Escreva um programa que receba como entrada o sal ́ario atual de um
# funcion ́ario, calcule e exiba o valor de seu novo sal ́ario j ́a com o aumento concedido.

salario = float(input("Informe o valor do seu salário BRUTO: "))

if salario > 300 and salario <= 500:
    novo_salario = salario * 1.07
elif salario > 500:
    novo_salario = salario * 1.1
else:
    novo_salario = salario * 1.03
    
print(f'Novo Valor do Salário Bruto: R$ {novo_salario}')