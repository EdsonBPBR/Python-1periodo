# Fazer um programa que armazene nomes e notas das AB1 e AB2 de n alunos. Calcular e armazenar a média aritmética desses alunos e a situação de cada um: 'AP' ou 'RP', sem aspas. Imprimir uma listagem contendo nome, notas, média e situação de cada aluno. Considere média maior ou igual a 7,00 para a aprovação.

n = int(input())
i = 0

registros = {}

while i < n:
    nome = str(input())
    nota_ab1 = float(input())
    nota_ab2 = float(input())
    media = (nota_ab1 + nota_ab2) / 2
    
    if media >= 7:
        situacao = 'AP'
    else:
        situacao = 'RP'
        
    registros[nome] = (nota_ab1, nota_ab2, media, situacao)
    
    i += 1
    
for elementos in registros.keys():
    print(f'Nome:  {elementos}')
    print(f'AB1: {registros[elementos][0]:.2f}')
    print(f'AB2: {registros[elementos][1]:.2f}')
    print(f'Media: {registros[elementos][2]:.2f}')
    print(f'Situacao:  {registros[elementos][3]}')