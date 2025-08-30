# Fernanda tem um projeto de extensão e precisa selecionar alunos. Escreva um programa para que ela possa informar matrícula e CRE dos vários inscritos, e ver, ao final, a matrícula do aluno com menor CRE e o CRE médio de todos os candidatos.
c = 0
soma_cre = 0

while True:
    matricula = str(input())
    
    if matricula == '999':
        break
    
    cre = float(input())
    soma_cre += cre
    
    if c == 0:
        menor_cre = cre
        matricula_menor_cre = matricula
    else:
        if cre < menor_cre:
            menor_cre = cre
            matricula_menor_cre = matricula
    c += 1

media = soma_cre / c
    
print(matricula_menor_cre)
print(f'{media:.2f}')
