# Escreva um programa que leia o sexo e o salário de 10 pessoas e calcule:
# -       a quantidade de homens;
# -       a quantidade de mulheres;
# -       a média do salário de homens e de mulheres;
# -       o sexo da pessoa com o maior salário;
# -       a média de salário dos homens;

if __name__ == '__main__':
    k = 0

    quant_homens = 0
    quant_mulheres = 0

    somatorio_salario = 0
    somatorio_salario_homens = 0
    maior_salario = 0

    while k < 10:
        salario = float(input())
        sexo = str(input()).upper()

        # obter o sexo do maior salário
        if k == 0:
            maior_salario = salario
            sexo_maior_salario = f'{sexo.lower()}'
        else:
            if salario > maior_salario:
                maior_salario = salario
                sexo_maior_salario = f'{sexo.lower()}'

        somatorio_salario += salario

        if sexo == 'M':
            somatorio_salario_homens += salario
            quant_homens += 1
        elif sexo == 'F':
            quant_mulheres += 1
        else:
            print('Sexo Inválido! Seu AUTISTA!')

        k += 1

    media_total = somatorio_salario / 10
    media_homens = somatorio_salario_homens / quant_homens

    print(quant_homens)
    print(quant_mulheres)
    print(f'{media_total:.1f}')
    print(sexo_maior_salario)
    print(f'{media_homens:.1f}')