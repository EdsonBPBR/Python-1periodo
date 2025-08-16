# (Eleitor) Fa ̧ca um programa que leia a idade (valor inteiro) de uma pessoa e informe
# sua classe eleitoral:
# nao eleitor (abaixo de 16 anos)
# eleitor obrigat ́orio (maior e igual a 18 ou menor e igual a 65 anos)
# eleitor facultativo (entre 16 e 18 anos ou acima dos 65 anos)

idade = int(input('Informe sua idade: '))

if idade < 16:
    print('NÃO ELEITOR')
elif 16 <= idade < 18 or idade > 65:
    print('ELEITOR FACULTATIVO')
else:
    print('ELEITOR OBRIGATÓRIO')