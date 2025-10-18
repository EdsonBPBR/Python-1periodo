n = int(input())
registro = []
registro_datas = []
notas = []
idades = []

somatorio_notas = 0
somatorio_idades = 0

for _ in range(n):
    entrada = str(input()).split()
    nome = entrada[0]
    idade = int(entrada[1])
    nota = float(entrada[2])
    somatorio_notas += nota
    somatorio_idades += idade
    
    registro.append([nota, nome, idade])
    registro_datas.append([idade, nome, nota])
    notas.append(nota)
    idades.append(idade)

registro.sort()
registro_datas.sort()

print()
print('-'*3+'Notas'+'-'*3)
for i in range(n):
    print(f'{registro[i][1]} {registro[i][0]:.2f}')
print('---------')

media = (somatorio_notas/n)

notas.sort()
if len(notas) % 2 == 0:
    x = (len(notas)// 2) - 1
    y = len(notas)//2
    mediana_notas = (notas[x] + notas[y])/2
else:
    posicao = len(notas)//2
    mediana_notas = notas[posicao]

print(f'Media Nota: {media:.2f}')
print(f'Mediana Nota: {mediana_notas:.2f}\n')

print('-'*3+'Idade'+'-'*3)
for i in range(n):
    print(f'{registro_datas[i][1]} {registro_datas[i][0]}')
print('---------')

idades.sort()
if len(idades) % 2 == 0:
    x = (len(idades) // 2) - 1
    y = len(idades) // 2
    mediana_idade = (idades[x] + idades[y]) / 2
else:
    posicao = len(notas)//2
    mediana_idade = idades[posicao]
    
media_idade = (somatorio_idades/n)

print(f'Media Idade: {(media_idade):.2f}')
print(f'Mediana Idade: {mediana_idade:.2f}\n')