n_chamadas = 0

def Pell(n):
    global n_chamadas # o barbosa falo isso em sals
    n_chamadas += 1
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        return 2 * Pell(n-1) + Pell(n-2) # tá informando que tem um erro mas tá rodando normal toda vez que eu defino um elif n >=2  ao invés do else

def main():
    m = int(input('Informe o valor de N: '))
    print(f'O {m}-ésimo termo é {Pell(m)}')
    print(f'Número de chamadas da função: {n_chamadas}')

if __name__ == '__main__':
    main()