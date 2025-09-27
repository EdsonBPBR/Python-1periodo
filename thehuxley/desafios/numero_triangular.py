#  Por exemplo: 120 é triangular, pois 4*5*6 = 120. O número 2730 é triangular, pois 13*14*15 = 2730. Dado um número natural (inteiro não-negativo) n, verifique se ele é triangular ou não. 

if __name__ == '__main__':
    n = int(input())

    c = 1
    while True:
        k = c * (c + 1) * (c + 2)
        if k == n:
            print(f'{c} * {c + 1 } * {c + 2} = {n}')
            print('Verdadeiro')
            break
        else:
            if k >= n:
                print('Falso')
                break
        c += 1
