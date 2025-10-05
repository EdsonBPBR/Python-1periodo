# Repare a seguinte característica do número 3025:
# 30 + 25 = 55 e 55^2 = 3025

while True:
    n = int(input())
    
    if n < 1000 or n > 9999:
        break
    
    a = n // 100
    b = n % 100
    c = a + b
    
    if c ** 2 == n:
        print('propriedade do 3025!')
    else:
        print('numero comum')
    