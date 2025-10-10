
n_aprovados_filosofia = 0
pessoa_mais_jovem = ''
n_aprovados = 0
n_n_sociologia = 0

i = 0
while True:
    media = float(input())
    if media < 0:
        break
    nome = str(input())
    idade = int(input())
    curso = str(input())
    
    if i == 0:
        mais_jovem = idade
        pessoa_mais_jovem = f'{nome}'
    else:
        if idade < mais_jovem:
            mais_jovem = idade
            pessoa_mais_jovem = f'{nome}'
        
    if curso == 'f' and media >= 70:
        n_aprovados_filosofia += 1

    if idade >= 18 and curso == 's' and media < 70:
        n_n_sociologia += 1
        
    if media >= 70:
        n_aprovados += 1
    
    i += 1
    
print(f'Quantidade de aprovados em filosofia : {n_aprovados_filosofia}')
if i > 0:
    print(f'O nome da pessoa mais jovem : {pessoa_mais_jovem}')
print(f'Quantidade de aprovados : {n_aprovados}')
print(f'Quantidade pessoas maiores de idade nao aprovadas em sociologia : {n_n_sociologia}')