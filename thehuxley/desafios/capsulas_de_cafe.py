#1 capsula - 2 xícaras
#1 p - 10 capsulas
#1 g - 16 capsulas


c = 0
total_capsulas = 0
while c < 7:
    c += 1
    n_caixas = int(input())
    tipo_caixa = str(input())
    
    if tipo_caixa.upper() == 'G':
        total_capsulas += n_caixas * 16
    
    elif tipo_caixa.upper() == 'P':
        total_capsulas += n_caixas * 10
    
    else:
        break

print(total_capsulas)
n_xicaras = (total_capsulas * 2)/7
print(int(n_xicaras))
    