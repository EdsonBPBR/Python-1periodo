#z1 = a + b.i

def calculaSoma(a,b,c,d):
    e = (a+c)
    f = (b+d)
    return e, f

def calculaMulti(a,b,c,d):
    e = (a*c) - (b*d)
    f = (a*d) + (b*c)
    return e, f

def main():
    entrada_n1 = str(input()).split()
    #z1 
    a = int(entrada_n1[0])
    b = int(entrada_n1[1])

    #z3
    entrada_n2 = str(input()).split()
    c = int(entrada_n2[0])
    d = int(entrada_n2[1])


    k, j = calculaSoma(a,b,c,d)
    h, o = calculaMulti(a,b,c,d)
    print(f'Soma: {k}+{j}i')
    print(f'Multi: {h}+{o}i')
    
if __name__ == '__main__':
    main()