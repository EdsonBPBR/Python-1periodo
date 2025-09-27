# Desenvolva um procedimento chamado "amadoProfessor" que recebe um número e imprime sua tabuada do 1 ao 10.

n = int(input())

for i in range(1, 11):
    print(f'{n} x {i} =  {n*i}')