# Faça um programa para corrigir provas de múltipla escolha. Cada prova tem 10 questões, cada questão valendo um ponto. O primeiro conjunto de dados a ser lido é o gabarito para a correção da prova. Depois serão dados os números dos alunos e suas respectivas respostas. O programa encerra a entrada quando o número de um aluno dado for igual a 9999


gabarito = str(input())
n_aprovados = 0
n_provas_corrigidas = 0
notas = []

while True:
    pontuacao = 0
    aluno = str(input()).split()
        
    if aluno[0] == '9999':
        break

    
    c = 0
    while c < len(gabarito):
        if gabarito[c] == aluno[1][c]:
            pontuacao += 1
        c += 1
    
    # necessário para calcular a porcentagem de aprovação
    if pontuacao >= 6:
        n_aprovados += 1
    
    n_provas_corrigidas += 1
    notas.append(pontuacao) # adiciona a nota do aluno para poder obter o número da nota com maior frequência
    print(f'{aluno[0]} {pontuacao:.1f}')

print(f'{((n_aprovados/n_provas_corrigidas) * 100):.1f}%')

mais_frequente = notas[0]
maior_contagem = notas.count(mais_frequente)

for nota in notas:
    contagem = notas.count(nota)
    if contagem > maior_contagem:
        maior_contagem = contagem
        mais_frequente = nota
        
print(f'{mais_frequente:.1f}') # implementar função para o código ficar mais legível e boa manutenção 