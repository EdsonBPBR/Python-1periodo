# Faça um programa para corrigir provas de múltipla escolha. Cada prova tem 10 questões, cada questão valendo um ponto. O primeiro conjunto de dados a ser lido é o gabarito para a correção da prova. Depois serão dados os números dos alunos e suas respectivas respostas. O programa encerra a entrada quando o número de um aluno dado for igual a 9999

gabarito = str(input())


#estava tentando sem lista para entrada, mas estava conflitando quando era 9999, que era necessário dois valores, para 9999 tentarei utilizando listas
# while True:
#     aluno, gabarito_aluno = map(str, input().split())
    
#     if aluno == 9999 and gabarito_aluno == None:
#         break
    
#     nota = 0
    
#     for questao in range(len(gabarito)):
#         if gabarito[questao] == gabarito_aluno[questao]:
#             nota += 1
    
#     print(f'{aluno} {nota}')