# Marcos é um professor muito organizado e quer guardar as notas dos alunos que ficaram em recuperação. Para isso você deve desenvolver um programa que leia a quantidade de alunos que ficaram em recuperação e guarde cada uma em um vetor simples. 

n = int(input())
if n > 0:
    i = 0
    notas = []

    while i < n:
        m = float(input())
        notas.append(m)
        
        i += 1
        
    print(notas)
    print(f'{sum(notas):.2f}')
else:
    print('Nenhuma nota informada!')