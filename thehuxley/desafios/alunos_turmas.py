registros = []
while True:
    try:
        nome = str(input())
        turma = int(input())
        
        registros.append((nome, turma))
    except EOFError:
        break

for n in range(1,4):
    print(f'Turma {n}:')
    for i in range(len(registros)):
        if registros[i][1] == n:
            print(registros[i][0])
    print()