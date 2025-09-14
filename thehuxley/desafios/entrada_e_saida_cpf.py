# seu professor gostaria de fazer um programa com as seguintes características:
# • Leia os dados de um CPF no formato XXX.YYY.ZZZ-DD;
# • Imprima os quatro números, sendo um valor por linha.

cpf = str(input()).split('.')
final = cpf[2].split('-')
print(cpf[0])
print(cpf[1])
print(final[0])
print(final[1])