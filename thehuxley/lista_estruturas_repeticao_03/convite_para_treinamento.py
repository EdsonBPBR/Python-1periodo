# O principal prêmio da Olimpíada de Informática é o convite para os cursos de programação oferecidos no Instituto de Computação da Unicamp, com todas as despesas pagas. São convidados apenas os competidores que atingem um certo número mínimo de pontos, consideradas as duas fases de provas.
# Você foi contratado para fazer um programa que, dados os números de pontos obtidos por cada competidor em cada uma das fases, e o número mínimo de pontos para ser convidado, determine quantos competidores serão convidados para o curso na Unicamp. Você deve considerar que
#     todos os competidores participaram das duas fases;
#     o total de pontos de um competidor é a soma dos pontos obtidos nas duas fases;
#     o competidor não pode zerar em nenhuma das fases. ATENÇÃO AQ

n_participantes_convidados = 0

n_participantes = int(input())
pontuacao_minima = int(input())

for competidor in range(n_participantes):
    pontos_1fase = int(input())
    pontos_2fase = int(input())
    
    if pontos_1fase == 0 or pontos_2fase == 0:
        pontos_1fase = pontos_2fase = 0
    
    if (pontos_1fase + pontos_2fase) >= pontuacao_minima:
        n_participantes_convidados += 1

print(n_participantes_convidados)
    