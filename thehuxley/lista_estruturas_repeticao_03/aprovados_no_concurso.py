# O IBGE realizou um concurso para contratar pessoas para trabalhar no censo. Cada candidato fez uma prova de português com 50 questões, outra de matemática com 35 questões, e uma prova de redação.
# Para ser aprovado, era necessário acertar pelo menos 80% da prova de português, 60% da prova de matemática, e ter nota igual ou superior a 7 na redação.
# Escreva um programa que receba como entrada, para cada candidato, a quantidade de questões certas em português e em matemática, e também a nota na redação, e depois exiba quantos candidatos foram aprovados.

# precisa acertar, no mínimo, 40 questões de portugues e 21 questões de matemática e redação >= 7

aprovados = 0
while True:
    n_acertos_port = int(input())
    
    if n_acertos_port < 0:
        break
    
    n_acertos_matem = int(input())
    redacao = float(input())
    
    if n_acertos_port >= 40 and n_acertos_matem >= 21 and redacao >= 7:
        aprovados += 1

print(aprovados)