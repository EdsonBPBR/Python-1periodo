atomo_1 = 'Q'
atomo_2 = 'P'
atomo_3 = 'R'

print('='*30)
print(f'{atomo_1: ^10}|{atomo_2: ^10}|{atomo_3: ^10}|{'~ '+atomo_1: ^10}')
print('='*30)

c1 = 0
for a in range(8):
    if a % 2 != 0:
        x = 'F'
        x_logico = False
    else:
        x = 'V'
        x_logico = True

    if c1 % 2 == 0:
        y = 'V'
        y_logico = True
    else:
        y = 'F'
        y_logico = False
        
    if (a // 4) % 2 == 0:
        z = 'V'
        z_logico = True
    else:
        z = 'F'
        z_logico = False
    
        
    c1 += a    
    print(f'{z: ^10}|{y: ^10}|{x: ^10}|')
