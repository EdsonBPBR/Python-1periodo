# Faça um programa que leia três notas (valores reais) de um aluno, calcule sua média aritmética e imprima uma mensagem dizendo se o aluno foi aprovado, reprovado ou deverá fazer prova final. O critério de aprovação é o seguinte:
# Aprovado (média >= 7);
# Reprovado (média < 3);
# Prova final ( 3 <= média < 7).

n1 = float(input('Informe a nota n1: '))
n2 = float(input('Informe a nota n2: '))
n3 = float(input('Informe a nota n3: '))

media = (n1 + n2 + n3) / 3

if media >= 7:
    print('aprovado')
elif media >= 3 and media < 7:
    print('prova final')
else:
    print('reprovado')